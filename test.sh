echo 'generating test feature and record...'
if [ $# -ge 1 ]; then
    python test/generate_feature_record.py $1
else
    python test/generate_feature_record.py
fi

echo 'predicting result...'
python test/predict_result.py

echo 'generating ground truth...'
python test/generate_ground_truth.py

echo $3 >> eval_c
ruby test/result_analysis.rb >> eval_c
cp relation_extraction.model relation_extraction.model.c.$3
