python-http.org
===============

 .. image:: https://img.shields.io/travis/python-http/python-http.org/master.svg
    :target: https://travis-ci.org/python-http/python-http.org

This repository is the source code for the website found at https://python-http.org.
All changes are automatically deployed to cloud hosting.

Building the Website
--------------------

To build the website we currently use `Sphinx`_. All the source code for each page can be
found within ``source/``. Once you've finished making your updates you can test them locally
by running the ``nox -s build`` with ``nox`` installed which will rebuild all HTML and static resources.

 .. _Sphinx: http://www.sphinx-doc.org/en/master/
