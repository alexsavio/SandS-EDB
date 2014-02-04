#!/bin/bash

export WORKON_HOME=~/envs
source /usr/local/bin/virtualenvwrapper.sh

workon sands
echo python ~/projects/sands-edb/src/start_server.py | at now
