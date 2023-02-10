#!/bin/bash

echo "input: "
cat input 
echo "output: "
gcc $1 && ./a.out < input
echo ""
