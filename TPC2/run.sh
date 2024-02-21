#!/bin/bash

cat example.md | ./mdToHTML.py | tee res.html
