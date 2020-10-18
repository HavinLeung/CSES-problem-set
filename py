#!/bin/bash

mkdir -p $1 && cp templates/template.py $1/$1.py && vim $1/$1.py
