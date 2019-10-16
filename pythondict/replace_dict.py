#encoding=utf-8
import re
strr="aass\n"
target="<font color=red size=+2><b>a\n</b></font> <br><br><font color=black>a [ə]\n" #在用的时候再加r

print(strr)

strbej="ssa"

test="a	<font color=red size=+2><b>a\n</b></font> <br><br><font color=black>a [ə]\n   ein\n</font><br>"
test2="woolen	 #fenggefu#   Wollstoff\n\nwoolenUS [wulənəm]\n   aus Wo/ll(AAA)e; wollig; Wollware}; Wollwaren #fenggefu#"

pat_ende = re.compile(r'<font ([\s\S]*)]\n|\n</font><br>')
pat_ende2= re.compile(r'\[([\s\S]*?)]|\n|\S+\}')
pat_ende3=re.compile(r'/|\(|\)')

pat_judge=re.compile(r'([\s\S]*?);([\s\S]*?)')

str2=re.sub(pat_ende,r" #fenggefu#",test)
str3=re.sub(pat_ende3,r" ",test2)

#flag=pat_judge.match(strbej).group()
list=(strbej.split(";"))

print(list)