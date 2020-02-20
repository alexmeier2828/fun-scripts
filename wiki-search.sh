#!/bin/bash
echo $1 
w3m "https://en.wikipedia.org/w/index.php?search=$1&title=Special%3ASearch&fulltext=1&ns0=1"
