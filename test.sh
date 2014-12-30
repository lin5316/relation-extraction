echo 'generating test feature and record...'
if [ $# -eq 1 ]; then
    python test/generate_feature_record.py $1
else
    python test/generate_feature_record.py
fi

echo 'predicting result...'
python test/predict_result.py

echo 'generating ground truth...'
python test/generate_ground_truth.py

echo $2
ruby test/result_analysis.rb >> eval_neg_rate
