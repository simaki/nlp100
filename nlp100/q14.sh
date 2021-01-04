#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/14.txt"

function main () {
  printf "Solving Q14 ... "

  n=5
  # # Read from stdin:
  # printf "Enter number of lines: "
  # read n

  head -n $n $i > $o

  echo "Done."
}

main
