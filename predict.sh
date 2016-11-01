normalize_text() {
  tr '[:upper:]' '[:lower:]' | sed -e 's/^/__label__/g' | \
    sed -e "s/'/ ' /g" -e 's/"//g' -e 's/\./ \. /g' -e 's/<br \/>/ /g' \
        -e 's/,/ , /g' -e 's/(/ ( /g' -e 's/)/ ) /g' -e 's/\!/ \! /g' \
        -e 's/\?/ \? /g' -e 's/\;/ /g' -e 's/\:/ /g' | tr -s " "
}

RESULTDIR=result
DATADIR=data
DATANAME=amazon

cat "${DATADIR}/text" | normalize_text > "${DATADIR}/text.data"

./fasttext predict-prob "${RESULTDIR}/${DATANAME}.bin" "${DATADIR}/text.data" 5 \
 >  "${RESULTDIR}/predict"
