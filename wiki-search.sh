#!/bin/bash
echo $1 
elinks "https://en.wikipedia.org/w/index.php?search=$1"
