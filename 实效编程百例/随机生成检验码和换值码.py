import random

num = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 59)]
random.shuffle(num)  # 打乱num的顺序
sec = ''.join(num)
random.shuffle(num)
dec = ''.join(num)
print(num)
print(sec)
print(dec)
