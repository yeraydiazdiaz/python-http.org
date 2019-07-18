import os

import nox


@nox.session(reuse_venv=True)
def lint(session):
    session.install("black")

    session.run("black", "noxfile.py", "source/conf.py", "source/_ext/")


@nox.session(reuse_venv=True)
def build(session):
    session.install("sphinx", "htmlmin")

    session.run("rm", "-rf", "build/html/")
    session.run(
        "sphinx-build", "-W", "-n", "-a", "-b", "html", "source/", "build/html/"
    )

    for root, _, files in os.walk("build/html/"):
        for filename in files:
            if filename.endswith(".html"):
                filepath = os.path.join(root, filename)
                session.run("htmlmin", "-s", "-c", filepath, filepath)
