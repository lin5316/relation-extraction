echo 'generating train feature...'
if [ $# -eq 1 ]; then
    python train/generate_feature.py $1
elif [ $# -eq 2 ]; then
    python train/generate_feature.py $1 $2
else
    python train/generate_feature.py
fi

echo 'training model...'
python train/train_model.py
