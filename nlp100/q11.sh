#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/11.txt"

function main () {
  printf "Solving Q11 ... "

  tab=`echo '\t'`
  sed "s/$tab/\ /g" $i > $o

  echo "Done."
}

main
