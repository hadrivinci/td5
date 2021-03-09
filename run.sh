#!/bin/bash

if [[ ! -f ./virtualenv ]]
then
    pip3 install virtualenv
	python -m venv ./virtualenv
	source ./virtualenv/script/activate
	pip3 install -r ./requirements.txt
else
	source ./virtualenv/Scripts/activate
fi

python ./main.py
