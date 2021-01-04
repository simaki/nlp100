#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o1="$PROJECT_PATH/output/name/12_1.txt"
o2="$PROJECT_PATH/output/name/12_2.txt"

function main () {
  printf "Solving Q12 ... "

  tab=`echo '\t'`
  cut -f 1 -d "$tab" $i > $o1
  cut -f 2 -d "$tab" $i > $o2

  echo "Done."
}

main
