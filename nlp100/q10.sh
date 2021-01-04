#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/10.txt"

function main () {
  printf "Solving Q10 ... "

  cat $i | wc -l | sed 's/\ //g' > $o

  echo "Done."
}

main
