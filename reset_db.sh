#!/bin/bash

fd -t d -HI __pycache__ -X rm -r 
fd -t d -HI .mypy_cache -X rm -r 
