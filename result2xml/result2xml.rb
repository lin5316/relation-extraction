require 'rexml/document'
corpus_file=File.new('mid')
result_file=File.new('result')
xml_result_file=File.new('xml_result.xml','w+')
doc = REXML::Document.new
corpus=[]
results=[]
corpus_file.each do|line|
  corpus.push(line)
end
result_file.each do |line|
  results.push(line)
end
root=doc.add_element('weibos')
i=1
corpus.each do |sentence|
  if sentence=="\n"
    next
  end

  weibo=root.add_element('weibo',{'id'=>"#{i}"})
  weibo.add_text(sentence)
  results.each do |result|
    if result.split(' ')[0].to_i==i
      weibo.add_element('employee',{'from'=>result.split(' ')[2],'name'=>result.split(' ')[1]})
    end
  end
  i=i+1
end
xml_result_file.puts(doc.write)

