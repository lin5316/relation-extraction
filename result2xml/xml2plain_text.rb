require 'rexml/document'
file=File.new('input')
doc=REXML::Document.new(file)
output=File.new('mid','w')
root=doc.root
root.elements.each do |ele|
  output.puts(ele.text.to_s)
end
