# coding=utf-8
import requests

number = 15254300
find = 0
while number < 15260000:
	link ='https://dbditem.jd.com/'+`number`
	r = requests.get(link)
	want = 'SONY' in r.text
	if want == 1:
		print link
		find += 1
		result =r.url
		f = open("text2.txt",'wb')
		f.write(result+"\n")
		f.close()
			#	if `find`%10 ==0:
			#		print "目前搜索到 "+ `find` +" 个SONY产品"
		number += 1
	else:
		number += 1
print "搜索结束一共找到 " + `find` + "个SONY产品，记录将保存在desktop>text3.txt中"
