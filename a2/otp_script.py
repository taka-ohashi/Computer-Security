from Crypto.Random import random

s = open("cp-logo.bmp", "rb").read()

rnd = random.get_random_bytes(len(s))

x = []

def randKey(alpha, msg):
	msgLen = len(msg)
	key = ""
	count = 0
	while count < msgLen:
		key += random.choice(alpha)
		count += 1
	return key

for x1,x2 in zip(s,rnd):

	print("{:02x}".format(ord(str(x1)^ord(str(x2)))))
	x.append(temp.decode("hex"))

