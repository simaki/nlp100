#!/bin/sh

DATADIR="./data"

mkdir $DATADIR

mkdir "$DATADIR/name"
name="popular-names.txt"
echo --- Fetch $name start ---
curl https://nlp100.github.io/data/popular-names.txt -o $DATADIR/name/$name
echo --- Fetch $name end ---

mkdir "$DATADIR/wiki"
name="jawiki-country.json.gz"
echo --- Fetch $name start ---
curl https://nlp100.github.io/data/jawiki-country.json.gz -o $DATADIR/wiki/$name
gzip -df $DATADIR/wiki/$name
echo --- Fetch $name end ---

mkdir "$DATADIR/neko"
name="neko.txt"
echo --- Fetch $name start ---
curl https://nlp100.github.io/data/neko.txt -o $DATADIR/neko/$name
echo --- Fetch $name end ---

mkdir "$DATADIR/news"
name_zip="NewsAggregatorDataset.zip"
name="NewsAggregatorDataset"
echo --- Fetch $name start ---
curl https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip -o $DATADIR/news/$name_zip
unzip -o $DATADIR/news/$name_zip -d $DATADIR/news/$name
rm $DATADIR/news/$name_zip
echo --- Fetch $name end ---

mkdir "$DATADIR/w2v"
name_gz="GoogleNews-vectors-negative300.bin.gz"
name="GoogleNews-vectors-negative300.bin"
echo --- Fetch $name start ---
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM" -o $DATADIR/w2v/$name_gz
gzip -df $DATADIR/w2v/$name_gz
echo --- Fetch $name end ---

name="questions-words.txt"
echo --- Fetch $name start ---
curl http://download.tensorflow.org/data/questions-words.txt -o $DATADIR/w2v/$name
echo --- Fetch $name end ---

name_zip="wordsim353.zip"
name="wordsim353"
echo --- Fetch $name start ---
curl http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip -o $DATADIR/w2v/$name_zip
unzip $DATADIR/w2v/$name_zip -d $DATADIR/w2v/$name
rm $DATADIR/w2v/$name_zip
echo --- Fetch $name end ---
