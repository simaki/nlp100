#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/15.txt"

function main () {
  printf "Solving Q15 ... "

  n=5
  # # Read from stdin:
  # printf "Enter number of lines: "
  # read n

  tail -n $n $i > $o

  echo "Done."
}

main
