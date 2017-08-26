#coding:utf-8
#Author By Arice
#Referer:部分代码思维来源于互联网
import sys
import urllib
import hashlib
import base64
import HTMLParser
import cgi
import re
import binascii
from pycipher import ADFGX
from pycipher import ADFGVX
from termcolor import cprint

def urlcode(Val):
	cprint(Val+'====>url编码结果为：'+urllib.quote(Val,safe=''),'yellow')

def urldecode(Val):
	cprint(Val+'====>url解码结果为：'+urllib.unquote(Val),'yellow')
	#print urllib.unquote(Val)

def china_six(Val):
	Value1 = binascii.b2a_hex(Val.decode('utf-8').encode("utf8"))
	Value2 = binascii.b2a_hex(Val.decode('utf-8').encode("gbk"))
	cprint('原始汉字为：'+Val,'yellow')
	cprint('十六进制转汉字（UTF-8）版本：'+Value1,'yellow')
	cprint('十六进制转汉字（gbk）版本：'+Value2,'yellow')

def six_china(Val):
	Value1 = binascii.a2b_hex(Val).decode("utf8")
	Value2 = binascii.a2b_hex(Val).decode("gbk")
	cprint(u'汉字转十六进制（UTF-8）版本：'+Value1,'yellow')
	cprint(u'汉字转十六进制（gbk）版本：'+Value2,'yellow')

def char_six(Val):
	Value = binascii.b2a_hex(Val)
	cprint('原始字符串为：'+Val,'yellow')
	cprint('字符串转十六进制：'+Value,'yellow')

def six_char(Val):
	Value = binascii.a2b_hex(Val)
	cprint('原始十六进制为：'+Val,'yellow')
	cprint('十六进制转字符串：'+Value,'yellow')


def cmd5(Val):
	m = hashlib.md5()
	m.update(Val)
	cprint('原始数据为：'+Val,'yellow')
	cprint('加密后32位长度为：'+m.hexdigest(),'yellow')
	cprint('加密后16位长度为：'+m.hexdigest()[8:-8],'yellow')
	

def b64encode(Val):
	cprint(Val+'====>base64编码结果为：'+base64.b64encode(Val),'yellow')
	#print base64.b64encode(Val)

def b64decode(Val):
	try:
		cprint(Val+'====>base64解码结果为：'+base64.b64decode(Val),'yellow')
	except:
		cprint('解码失败，可能是由于解码数据有误!请重新输入有效数据','red')
	#print base64.b64decode(Val)

def unicode_china(Val):
	try:
		Value = Val.decode('unicode_escape')
		cprint(Val+u'====>Unicode转中文结果为'+Value,'yellow')
		#print Val.decode('unicode_escape')
	except:
		cprint('转换失败，可能是由于转换数据有误!请重新输入有效数据','red')

def china_unicode(Val):
	try:
		Value = Val.decode('utf-8').encode('unicode_escape')
		cprint(Val+'====>中文转Unicode结果为：'+Value,'yellow')
		#print Val.decode('utf-8').encode('unicode_escape')
	except:
		cprint('转换失败，可能是由于转换数据有误!请重新输入有效数据','red')

def caser_en(Val,num):
	Val = str(Val)
	num = int(num)
	l = []
	for i in range(len(Val)):
		#print Val[i]
		Vi = ord(Val[i])
		if Vi >= 97 and Vi <= 122:
			Vi = 97 + ((Vi - 97) + num) %26
			Vi = chr(Vi)
			l.append(Vi)
		elif Vi >=65 and Vi <= 90:
			Vi = 65 + ((Vi - 65) + num) %26
			Vi = chr(Vi)
			l.append(Vi)
		else:
			Vi = chr(Vi)
			l.append(Vi)
	cprint('凯撒加密前为：'+Val,'yellow')
	cprint('凯撒加密后为：'+''.join(l),'yellow')
	#print ''.join(l)

def caser_de(Val,num):
	Val = str(Val)
	num = int(num)
	l = []
	for i in range(len(Val)):
		#print Val[i]
		Vi = ord(Val[i])
		if Vi >= 97 and Vi <= 122:
			Vi = 97 + ((Vi - 97) - num) %26
			Vi = chr(Vi)
			l.append(Vi)
		elif Vi >=65 and Vi <= 90:
			Vi = 65 + ((Vi - 65) - num) %26
			Vi = chr(Vi)
			l.append(Vi)
		else:
			Vi = chr(Vi)
			l.append(Vi)
	cprint('凯撒解密前为：'+Val,'yellow')
	cprint('凯撒解密后为：'+''.join(l),'yellow')
	cprint('偏移量为：'+num,'yellow')
	#print ''.join(l)

def html_de(Val):
	html_de = HTMLParser.HTMLParser()
	Value = html_de.unescape(Val)
	cprint(Val+u'====>html实体解码后为：'+Value,'yellow')

def html_en(Val):
	html_en = cgi.escape(Val)
	cprint(Val+'====>html实体编码后为：'+html_en,'yellow')

#栅栏密码
def fence(Val):
	array = []
	cprint('原始数据为：'+Val,'yellow')
	for i in range(2,len(Val)):
		if len(Val) %i == 0:
			array.append(i)
	for j in array:
		n = len(Val) / j
		result = {q:'' for q in range(n)}
		for i in range(len(Val)):
			num = i % n
			result.update({num:result[num] + Val[i]})
		Value = ''
		for i in range(n):
			Value = Value + result[i]
		cprint('当组分成'+str(j)+'时，结果为：'+Value,'yellow')

#摩斯电码
def mose_de(Val):
	cprint('原始的摩斯电码为：'+Val,'yellow')
	Value = ''
	mose_code = {'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--',     'N': '-.',     'O': '---','P': '.--.',   'Q': '--.-',   'R': '.-.','S': '...',    'T': '-',      'U': '..-','V': '...-',   'W': '.--',    'X': '-..-','Y': '-.--',   'Z': '--..','0': '-----',  '1': '.----',  '2': '..---','3': '...--',  '4': '....-',  '5': '.....','6': '-....',  '7': '--...',  '8': '---..','9': '----.'}
	Val = re.split(",| |!|@|#|",Val)
	for V in Val:
		#print V
		for i in mose_code.keys():
			if mose_code[i] == V:
				Value+= i
	cprint('转换后的摩斯电码为：'+Value,'yellow')

#埃特巴什码
def atbash_de(Val):
	Value = ''
	atbash_code ={'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A',' ':' ','!':'!','@':'@','{':'{','}':'}',',':',','?':'?','a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}
	for V in Val:
		for i in atbash_code.keys():
			if atbash_code[i] == V:
				Value+= i
	cprint('原始的埃特巴什码为(大小写正常)：'+Val,'yellow')
	cprint('转换后的埃特巴什码为(大小写正常)：'+Value,'yellow')
	cprint('转换后的埃特巴什码为(纯大写)：'+str.upper(Value),'yellow')
	cprint('转换后的埃特巴什码为(纯小写)：'+str.lower(Value),'yellow')

#维吉尼亚密码解密
def vigener_de(Val,key):
	list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	array = []
	Value = ''
	num = 0
	if str(key.isalpha()) =="True":
		for i in key:
			array.append(ord(i.upper())-65)
		for y in Val:
			if num%len(array) == 0:
				num = 0
			if y.isupper():
				Value+=list[(ord(y)-65-array[num]) %26]
				num+=1
			else:
				Value+=list[(ord(y)-97-array[num]) %26].lower()
				num+=1
		cprint('维吉尼亚的密文为：'+Val,'yellow')
		cprint('维尼吉亚的密钥为：'+key,'yellow')
		cprint('经过维尼吉亚解密后的结果为：'+Value,'yellow')
	else:
		cprint('[*]警告！！！密钥只能是纯字母！请重新查看并输入有效密钥','red')
		sys.exit()

#维吉尼亚密码加密
def vigener_en(Val,key):
	list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	array = []
	Value = ''
	num = 0
	if str(key.isalpha()) =="True":
		for i in key:
			array.append(ord(i.upper())-65)
		for y in Val:
			if num%len(array) == 0:
				num = 0
			if y.isupper():
				Value+=list[(ord(y)-65+array[num]) %26]
				num+=1
			else:
				Value+=list[(ord(y)-97+array[num]) %26].lower()
				num+=1
		cprint('维吉尼亚的明文为：'+Val,'yellow')
		cprint('维尼吉亚的密钥为：'+key,'yellow')
		cprint('经过维尼吉亚加密后的结果为：'+Value,'yellow')
	else:
		cprint('[*]警告！！！密钥只能是纯字母！请重新查看并输入有效密钥','red')
		sys.exit()

#培根密码加密
def bacon_en(Val):
	No = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	first = ['aaaaa','aaaab','aaaba','aaabb','aabaa','aabab','aabba','aabbb','abaaa','abaab','ababa','ababb','abbaa','abbab','abbba','abbbb','baaaa','baaab','baaba','baabb','babaa','babab','babba','babbb','bbaaa','bbaab']
	second = ['aaaaa','aaaab','aaaba','aaabb','aabaa','aabab','aabba','aabbb','abaaa','abaaa','abaab','ababa','ababb','abbaa','abbab','abbba','abbbb','baaaa','baaab','baaba','baabb','baabb','babaa','babab','babba','babbb']
	Value1 = ''
	Value2 = ''
	cprint('培根密码加密前为：'+Val,'yellow')
	for V in Val:
		V = V.lower()
		for i in range(0,26):
			if V == No[i]:
				Value1+= first[i].join("  ")
				Value2+= second[i].join("  ")

	cprint('培根密码加密后第一种结果为（空格为方便分辨）：'+Value1,'yellow')
	cprint('培根密码加密后第二种结果为（空格为方便分辨）：'+Value2,'yellow')

#培根密码解密
def bacon_de(Val):
	No = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	first = ['aaaaa','aaaab','aaaba','aaabb','aabaa','aabab','aabba','aabbb','abaaa','abaab','ababa','ababb','abbaa','abbab','abbba','abbbb','baaaa','baaab','baaba','baabb','babaa','babab','babba','babbb','bbaaa','bbaab']
	second = ['aaaaa','aaaab','aaaba','aaabb','aabaa','aabab','aabba','aabbb','abaaa','abaaa','abaab','ababa','ababb','abbaa','abbab','abbba','abbbb','baaaa','baaab','baaba','baabb','baabb','babaa','babab','babba','babbb']
	Value1 = ''
	Value2 = ''
	for V in re.findall(".{5}",Val):
		for i in range(0,26):
			if V == first[i]:
				Value1+= No[i].join("  ")
			if V == second[i]:
				Value2+= No[i].join("  ")
	cprint('培根密码解密后第一种结果为（空格为方便分辨）：'+Value1,'yellow')
	cprint('培根密码解密后第二种结果为（空格为方便分辨）：'+Value2,'yellow')

#ADFGX加密
def adfgx_en(Val,key):
	flag = ADFGX('phqgmeaynofdxkrcvszwbutil',key).encipher(Val)
	cprint('ADFGX明文结果为：'+Val,'yellow')
	cprint('ADFGX密钥为：'+key,'yellow')
	cprint('ADFGX加密后结果为：'+flag,'yellow')

#ADFGX解密
def adfgx_de(Val,key):
	flag = ADFGX('phqgmeaynofdxkrcvszwbutil',key).decipher(Val)
	cprint('ADFGX密文结果为：'+Val,'yellow')
	cprint('ADFGX密钥为：'+key,'yellow')
	cprint('ADFGX解密后结果为：'+flag,'yellow')

#ADFGVX加密
def adfgvx_en(Val,key):
	flag = ADFGVX('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8',key).encipher(Val)
	cprint('ADFGVX明文结果为：'+Val,'yellow')
	cprint('ADFGVX密钥为：'+key,'yellow')
	cprint('ADFGVX加密后结果为：'+flag,'yellow')

#ADFGX解密
def adfgvx_de(Val,key):
	flag = ADFGVX('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8',key).decipher(Val)
	cprint('ADFGVX密文结果为：'+Val,'yellow')
	cprint('ADFGVX密钥为：'+key,'yellow')
	cprint('ADFGVX解密后结果为：'+flag,'yellow')
	

if __name__ == '__main__':
	title ='''
	             _            _
	 _   _ _ __ | | ___   ___| | __
	| | | | '_ \| |/ _ \ / __| |/ /
	| |_| | | | | | (_) | (__|   <
	 \__,_|_| |_|_|\___/ \___|_|\_\

			Author By Arice
'''                                                                
	if str.lower(sys.argv[1]) == '-h':
		cprint('\t'+title,'magenta')
		cprint('\tUsage:','magenta')
		cprint('\t[*]-h 	是查看都有哪些命令，以及使用方法','magenta')
		cprint('\t[*]------------编码---------------[*]','magenta')
		cprint('\t[*]-urlen 	对后面的参数进行URl编码','magenta')
		cprint('\t[*]-urlde 	对后面的参数进行URL解码','magenta')
		cprint('\t[*]-b64en 	对后面的参数进行base64编码','magenta')
		cprint('\t[*]-b64de 	对后面的参数进行base64解码','magenta')
		cprint('\t[*]-china_six 	对后面的参数进行汉字转十六进制','magenta')
		cprint('\t[*]-six_china 	对后面的参数进行十六进制转汉字','magenta')
		cprint('\t[*]-char_six	对后面的参数进行字符串转十六进制','magenta')
		cprint('\t[*]-six_char	对后面的参数进行十六进制转字符串','magenta')
		cprint('\t[*]-un_china 	对后面的参数进行Unicode转汉字','magenta')
		cprint('\t[*]-china_un 	对后面的参数进行汉字转Unicode','magenta')
		cprint('\t[*]-html_de 	对后面的参数进行html实体解码','magenta')
		cprint('\t[*]-html_en 	对后面的参数进行html实体编码','magenta')
		cprint('\t[*]-----------------加解密----------------[*]','magenta')
		cprint('\t[*]-caser_en 	对后面的参数进行凯撒加密','magenta')
		cprint('\t[*]-caser_de 	对后面的参数进行凯撒解密','magenta')
		cprint('\t[*]-md5 	对后面的参数进行md5加密','magenta')
		cprint('\t[*]-fence 	对后面的参数进行栅栏密码解密','magenta')
		cprint('\t[*]-mose 	对后面的参数进行摩斯电码解密(可采用，！@＃进行分割)','magenta')
		cprint('\t[*]-atbash 	对后面的参数进行埃特巴什码转换','magenta')
		cprint('\t[*]-vigener 	对后面的参数进行维尔吉尼亚密码解密','magenta')
		cprint('\t[*]-vigener_en 	对后面的参数进行维尔吉尼亚密码加密','magenta')
		cprint('\t[*]-bacon_en 	对后面的参数进行培根密码加密','magenta')
		cprint('\t[*]-bacon_de 	对后面的参数进行培根密码解密','magenta')
		cprint('\t[*]-adfgx_en 	对后面的参数进行ADFGX密码加密','magenta')
		cprint('\t[*]-adfgx_de 	对后面的参数进行ADFGX密码解密','magenta')
		cprint('\t[*]-adfgvx_en 	对后面的参数进行ADFGVX密码加密','magenta')
		cprint('\t[*]-adfgvx_de 	对后面的参数进行ADFGVX密码解密','magenta')
		cprint('\t[*]----------------Example---------------[*]','magenta')
		cprint('\t[*]字符串转十六进制：python unlock.py -char_six \'<?php phpinfo();?>\'','magenta')
		cprint('\t[*]凯撒密码：python coding.py -caser_en abcd(明文) 3(偏移量)','magenta')
		cprint('\t[*]维吉尼亚：python coding.py -vigener abcd(密文) aaaa(密钥)','magenta')
		cprint('\t[*]维吉尼亚：python coding.py -vigener_en abcd(明文) aaaa(密钥)','magenta')
		cprint('\t[*]培根密码解密：python coding.py -bacon_de aaaaaaaaabaaaba(不用带空格)','magenta')
		cprint('\t[*]ADFGX加解密：python coding.py -adfgx_de \'aaa(明文或密文)\' \'aaa(密钥)\'','magenta')

	elif str.lower(sys.argv[1]) == '-urlen':
		urlcode(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-urlde':
		urldecode(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-md5':
		cmd5(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-b64en':
		b64encode(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-b64de':
		b64decode(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-six_china':
		six_china(sys.argv[2])
	elif str.lower(sys.argv[1]) == '-china_six':
		china_six(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-char_six':
		char_six(sys.argv[2])
	elif str.lower(sys.argv[1]) == '-six_char':
		six_char(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-html_de':
		html_de(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-html_en':
		html_en(sys.argv[2])

	elif str.lower(sys.argv[1]) == '-un_china':
		unicode_china(sys.argv[2])
	elif str.lower(sys.argv[1]) == '-china_un':
		china_unicode(sys.argv[2])
	elif str.lower(sys.argv[1]) == '-caser_en':
		if len(sys.argv) < 4:
			print '没有偏移量'
		else:
			caser_en(sys.argv[2],sys.argv[3])
	elif str.lower(sys.argv[1]) == '-caser_de':
		if len(sys.argv) < 4:
			print '没有偏移量'
		else:
			caser_de(sys.argv[2],sys.argv[3])
	#栅栏密码
	elif str.lower(sys.argv[1]) == '-fence':
		fence(sys.argv[2])

	#摩斯电码
	elif str.lower(sys.argv[1]) == '-mose':
		mose_de(sys.argv[2])

	#埃特巴什码
	elif str.lower(sys.argv[1]) == '-atbash':
		atbash_de(sys.argv[2])

	#维吉尼亚密码解密
	elif str.lower(sys.argv[1]) == '-vigener':
		if len(sys.argv) < 4:
			print '没有输入有效的值，查看是否输入密钥和密文'
		else:
			vigener_de(sys.argv[2],sys.argv[3])

	#维吉尼亚密码加密
	elif str.lower(sys.argv[1]) == '-vigener_en':
		if len(sys.argv) < 4:
			print '没有输入有效的值，查看是否输入密钥和明文'
		else:
			vigener_en(sys.argv[2],sys.argv[3])

	#培根密码加密
	elif str.lower(sys.argv[1]) == '-bacon_en':
		bacon_en(sys.argv[2])
	#培根密码解密
	elif str.lower(sys.argv[1]) == '-bacon_de':
		bacon_de(sys.argv[2])

	#ADFGX密码
	elif str.lower(sys.argv[1]) == '-adfgx_en':
		if len(sys.argv) < 4:
			print '没有输入有效的值，查看是否输入密钥和明文'
		else:
			adfgx_en(sys.argv[2],sys.argv[3])

	#ADFGX解密
	elif str.lower(sys.argv[1]) == '-adfgx_de':
		if len(sys.argv) < 4:
			print '没有输入有效的值，查看是否输入密钥和密文'
		else:
			adfgx_de(sys.argv[2],sys.argv[3])

	#ADFGVX密码
	elif str.lower(sys.argv[1]) == '-adfgvx_en':
		if len(sys.argv) < 4:
			print '没有输入有效的值，查看是否输入密钥和明文'
		else:
			adfgvx_en(sys.argv[2],sys.argv[3])
	#ADFGVX解密
	elif str.lower(sys.argv[1]) == '-adfgvx_de':
		if len(sys.argv) < 4:
			print '没有输入有效的值，查看是否输入密钥和密文'
		else:
			adfgvx_de(sys.argv[2],sys.argv[3])























