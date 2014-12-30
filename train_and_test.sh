if [ $# -eq 1 ]; then
    bash ./train.sh $1 && bash ./test.sh $1
elif [ $# -eq 2 ]; then
    bash ./train.sh $1 $2 && bash ./test.sh $1 $2
elif [ $# -eq 3 ]; then
    bash ./train.sh $1 $2 $3 && bash ./test.sh $1 $2 $3
else
    bash ./train.sh && bash ./test.sh
fi
