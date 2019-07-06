#!/bin/bash

set -ex

rm -rf build/html/
sphinx-build -W -n -a -b html source/ build/html/
