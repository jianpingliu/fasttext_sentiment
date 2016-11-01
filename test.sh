RESULTDIR=result
DATADIR=data
DATANAME=amazon

./fasttext test "${RESULTDIR}/${DATANAME}.bin" "${DATADIR}/test.data" 1

./fasttext predict-prob "${RESULTDIR}/${DATANAME}.bin" "${DATADIR}/test.data" 3 \
 >  "${RESULTDIR}/predict"