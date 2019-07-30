import os

import nox


source_files = ("source/", "noxfile.py")


@nox.session(reuse_venv=True)
def lint(session):
    session.install("black")

    session.run("black", *source_files)

    check(session)


@nox.session(reuse_venv=True)
def check(session):
    session.install("black")

    session.run("black", "--check", *source_files)


@nox.session(reuse_venv=True)
def build(session):
    session.install("-rrequirements.txt")

    session.run("rm", "-rf", "build/html/", external=True)
    session.run(
        "sphinx-build", "-W", "-n", "-a", "-b", "html", "source/", "build/html/"
    )

    for root, _, files in os.walk("build/html/"):
        for filename in files:
            if filename.endswith(".html"):
                filepath = os.path.join(root, filename)
                session.run("htmlmin", "-s", "-c", filepath, filepath)
