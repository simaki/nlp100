#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/18.txt"

function main () {
  printf "Solving Q18 ... "

  sort -n -r -k 3 $i > $o

  echo "Done."
}

main
