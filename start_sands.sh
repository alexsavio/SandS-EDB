#!/bin/bash

export WORKON_HOME=~/envs
source /usr/local/bin/virtualenvwrapper.sh

workon sands
echo python ~/projects/sands-edb/sands-esn/start_server.py | at now
