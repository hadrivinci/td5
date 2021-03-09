#!/bin/bash

if [[ ! -f ./virtualenv ]]
then
    python -m pip install virtualenv
	python -m venv ./virtualenv
	source ./virtualenv/script/activate
	python -m pip install -r ./requirements.txt
else
	source ./virtualenv/Scripts/activate
fi

python ./main.py
