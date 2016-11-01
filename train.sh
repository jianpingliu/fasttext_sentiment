myshuf() {
  perl -MList::Util=shuffle -e 'print shuffle(<>);' "$@";
}

normalize_text() {
  tr '[:upper:]' '[:lower:]' | sed -e 's/^/__label__/g' | \
    sed -e "s/'/ ' /g" -e 's/"//g' -e 's/\./ \. /g' -e 's/<br \/>/ /g' \
        -e 's/,/ , /g' -e 's/(/ ( /g' -e 's/)/ ) /g' -e 's/\!/ \! /g' \
        -e 's/\?/ \? /g' -e 's/\;/ /g' -e 's/\:/ /g' | tr -s " " | myshuf
}

RESULTDIR=result
DATADIR=data
DATANAME=amazon
TRAINDATA=train.csv
TESTDATA=test.csv

mkdir -p "${RESULTDIR}"

cat "${DATADIR}/${DATANAME}/${TRAINDATA}" | normalize_text > "${DATADIR}/train.data"
cat "${DATADIR}/${DATANAME}/${TESTDATA}" | normalize_text > "${DATADIR}/test.data"

make
rm -rf *.o

./fasttext supervised -input "${DATADIR}/train.data" -output "${RESULTDIR}/${DATANAME}" \
-dim 20 -lr 0.25 -wordNgrams 2 -minCount 20 -bucket 1000000 -epoch 5 -thread 10 > /dev/null

./fasttext predict-prob "${RESULTDIR}/${DATANAME}.bin" "${DATADIR}/test.data" 3 \
 >  "${RESULTDIR}/predict"