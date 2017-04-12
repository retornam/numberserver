#!/bin/bash

function source_venvp() {
  source venvp/bin/activate
  if [ $?==0 ]; then
    echo "successfully setup virtualenv"
  else
    echo "There was a problem setting up virtualenv. Exiting..."
    exit 1
  fi
}

command -v virtualenv >/dev/null  || \
 { echo >&2 "I require virtualenv  but it's not installed.  Aborting."; exit 1; }


if [ -d venvp ]; then
  echo "Directory venvp already exists."
  echo "Trying to source venvp"
  source_venvp
else
  virtualenv venvp
  pip install -r requirements.txt
  source_venvp
fi
