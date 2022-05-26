"""enxode()方法为str对象的方法，用于将字符串转换为二进制数据（即bytes）
	decode()方法为bytes对象的方法，用于解码"""
verse = '耶稣无人舟自恒'
byte = verse.encode(encoding = 'GBK')
print('原来的字符串：', verse)
print('转码后的字符串：', byte)
print('解码后的字符串：', byte.decode(encoding = 'GBK'))