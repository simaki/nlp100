#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/16_"

function main () {
  printf "Solving Q16 ... "

  split -l 1000 $i $o

  echo "Done."
}

main
