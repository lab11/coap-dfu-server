#!/bin/sh

cd $APP_PATH
git fetch
git fetch --tags -f
git reset --hard origin/master
git submodule update --init --recursive
make clean
make pkg_signed
exit 0
