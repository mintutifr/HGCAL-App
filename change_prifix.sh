#!/bin/bash
# Usage: addprefix <prefix> <files>

prefix=$1
echo $1
$shift
#echo `ls Hex*`
for f in `ls Hex*`
do
   mv "$f" "$prefix$f"
done

