def xml(tag,content,**param):
     string = ""
     string = "<" + tag + " "
     for i,j in param.items():
         string = string + i + "=" + "\\" + "\"" + j + "\\" + "\""
     string=string + ">" + content + "</" + tag + ">"
     return string

 
 
print(xml("a", "Hello there", href = " http://python.org ", _class = " my-link ", id = " someid "))
