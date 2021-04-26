#!/bin/bash -e

cd $APP_PATH
pwd
git fetch
git fetch --tags -f
git reset --hard origin/${BRANCH}
git submodule update --init --recursive
make clean
make pkg_signed

wait
