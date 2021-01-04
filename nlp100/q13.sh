#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i1="$PROJECT_PATH/output/name/12_1.txt"
i2="$PROJECT_PATH/output/name/12_2.txt"
o="$PROJECT_PATH/output/name/13.txt"

function main () {
  printf "Solving Q13 ... "

  tab=`echo '\t'`
  paste -d "$tab" $i1 $i2 > $o

  echo "Done."
}

main
