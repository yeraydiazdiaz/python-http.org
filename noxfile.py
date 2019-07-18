import nox


@nox.session(reuse_venv=True)
def lint(session):
    session.install("black")

    session.run("black", "noxfile.py", "source/conf.py")


@nox.session(reuse_venv=True)
def build(session):
    session.install("sphinx")

    session.run("rm", "-rf", "build/html/")
    session.run(
        "sphinx-build", "-W", "-n", "-a", "-b", "html", "source/", "build/html/"
    )
