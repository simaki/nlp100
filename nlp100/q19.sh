#!/bin/sh

PROJECT_PATH="`dirname ${0}`/.."
i="$PROJECT_PATH/data/name/popular-names.txt"
o="$PROJECT_PATH/output/name/19.txt"

function main () {
  printf "Solving Q19 ... "

  tab=`echo '\t'`
  cut -f 1 -d "$tab" $i | sort | uniq -c > $o
  sed "s/^[ \t]*//" $o > tmp.txt
  sort -n -r -k 1 tmp.txt | cut -f 2 -d " " > $o
  rm tmp.txt

  echo "Done."
}

main
