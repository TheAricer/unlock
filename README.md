Usage:
	[*]-h 	是查看都有哪些命令，以及使用方法
	[*]------------编码---------------[*]
	[*]-urlen 	对后面的参数进行URl编码
	[*]-urlde 	对后面的参数进行URL解码
	[*]-b64en 	对后面的参数进行base64编码
	[*]-b64de 	对后面的参数进行base64解码
	[*]-china_six 	对后面的参数进行汉字转十六进制
	[*]-six_china 	对后面的参数进行十六进制转汉字
	[*]-char_six	对后面的参数进行字符串转十六进制
	[*]-six_char	对后面的参数进行十六进制转字符串
	[*]-un_china 	对后面的参数进行Unicode转汉字
	[*]-china_un 	对后面的参数进行汉字转Unicode
	[*]-html_de 	对后面的参数进行html实体解码
	[*]-html_en 	对后面的参数进行html实体编码
	[*]-----------------加解密----------------[*]
	[*]-caser_en 	对后面的参数进行凯撒加密
	[*]-caser_de 	对后面的参数进行凯撒解密
	[*]-md5 	对后面的参数进行md5加密
	[*]-fence 	对后面的参数进行栅栏密码解密
	[*]-mose 	对后面的参数进行摩斯电码解密(可采用，！@＃进行分割)
	[*]-atbash 	对后面的参数进行埃特巴什码转换
	[*]-vigener 	对后面的参数进行维尔吉尼亚密码解密
	[*]-vigener_en 	对后面的参数进行维尔吉尼亚密码加密
	[*]-bacon_en 	对后面的参数进行培根密码加密
	[*]-bacon_de 	对后面的参数进行培根密码解密
	[*]-adfgx_en 	对后面的参数进行ADFGX密码加密
	[*]-adfgx_de 	对后面的参数进行ADFGX密码解密
	[*]-adfgvx_en 	对后面的参数进行ADFGVX密码加密
	[*]-adfgvx_de 	对后面的参数进行ADFGVX密码解密
	[*]----------------Example---------------[*]
	[*]字符串转十六进制：python unlock.py -char_six '<?php phpinfo();?>'
	[*]凯撒密码：python coding.py -caser_en abcd(明文) 3(偏移量)
	[*]维吉尼亚：python coding.py -vigener abcd(密文) aaaa(密钥)
	[*]维吉尼亚：python coding.py -vigener_en abcd(明文) aaaa(密钥)
	[*]培根密码解密：python coding.py -bacon_de aaaaaaaaabaaaba(不用带空格)
	[*]ADFGX加解密：python coding.py -adfgx_de 'aaa(明文或密文)' 'aaa(密钥)'
