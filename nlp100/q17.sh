#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/17.txt"

function main () {
  printf "Solving Q17 ... "

  tab=`echo '\t'`
  cut -f 1 -d "$tab" $i | sort | uniq > $o

  echo "Done."
}

main
