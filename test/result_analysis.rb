results_file=File.new('test/ground_truth.txt')
answers_file=File.new('test/result.txt')
results_index=0
answers_index=0
index=1
results=[]
answers=[]
results_file.each do |result_line|
  results.push(result_line)
end
answers_file.each do |answer_line|
  answers.push(answer_line)
end
exact_same=0
fuzzy_same=0
while results_index<results.length
  result_element=results[results_index].split(' ')
  while answers_index<answers.length
    answer_element=answers[answers_index].split(' ')
    answers_index=answers_index+1
    if result_element[0]==answer_element[0]
      if result_element[1]==answer_element[1]
        if result_element[2]==answer_element[2]
          exact_same=exact_same+1
          fuzzy_same=fuzzy_same+1
          break
        else
          if result_element[2].include?answer_element[2] or answer_element[2].include?result_element[2]
            fuzzy_same=fuzzy_same+1
            break
          end
          next
        end
      else
        next
      end
    else
      next
    end
  end
  results_index=results_index+1
  answers_index=0
end
#puts exact_same
exact_precision=exact_same*1.0/answers.length
exact_recall=exact_same*1.0/results.length
exact_f1=2*exact_precision*exact_recall/(exact_precision+exact_recall)
puts 'exact_precision='+exact_precision.to_s
puts 'exact_recall='+exact_recall.to_s
puts 'exact_f1='+exact_f1.to_s
puts ''

#puts fuzzy_same
fuzzy_precision=fuzzy_same*1.0/answers.length
fuzzy_recall=fuzzy_same*1.0/results.length
fuzzy_f1=2*fuzzy_precision*fuzzy_recall/(fuzzy_precision+fuzzy_recall)
puts 'fuzzy_precision='+fuzzy_precision.to_s
puts 'fuzzy_recall='+fuzzy_recall.to_s
puts 'fuzzy_f1='+fuzzy_f1.to_s
