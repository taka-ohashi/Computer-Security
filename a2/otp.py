from Crypto.Random import random
import struct

def main():
	#print(Random.choice(['dogs', 'cats', 'bears']))
	#str1 = "Darlin dont you go"
	#str2 = "and cut your hair!"
	#print(xor(str1, str2))
	#print(random.choice(['dogs', 'cats', 'bears']))
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	#msg = "Arlette"
	#print("msg:     " + msg)
	#print("encrypted: " + otp(alpha, msg))

	print("bmp encryption\n")
	encryptOTP("aRt.bmp", alpha)
	#printEncrypted("cp_encrypt.bmp")
	#encryptOTP("mustang.bmp", alpha)

	#twoPadTwo("cp-logo.bmp", "mustang.bmp", alpha)
	
def printEncrypted(fname):
	file = open(fname, "rb")
	lst = file.readlines()
	print(lst)
	'''str1 = ""
	for item in lst:
		str1 += str(item)
	print(str1)'''

def randKey(alpha, msg):
	msgLen = len(msg)
	key = ""
	count = 0
	while count < msgLen:
		key += random.choice(alpha)
		count += 1
	return key


def xor(string1, string2):
	print("string1_len: " + str(len(string1)))
	print("string2_len: " + str(len(string2)))

	if len(string1) != len(string2):
		return None
	output = ""
	lst = []
	idx = 0
	while idx < len(string1):
		hexval = hex(ord(string1[idx]) ^ ord(string2[idx]))[2:]
		if len(hexval) == 1:
			output += "0" + hexval
			lst.append("0" + hexval)
		else:
			output += hexval
			lst.append(hexval)
		idx += 1
	byte_obj = []
	for item in lst[0]:
		byte_obj.append(item.encode('ascii'))
	print(byte_obj)
	print(struct.pack('<s', byte_obj))
	#return struct.pack(llh01, lst[0])
	#return output


def otp(alpha, msg):
	rand_key = randKey(alpha, msg)
	output = xor(msg, rand_key)

	return output

def encryptOTP(fname, alpha):
	data = open(fname, "rb")
	list = data.readlines()
	data = str(list[0])
	print(len(data))
	header = data[:203]
	data = data.split("\\x")
	string = ""
	for tup in data[203:]:
		string += tup

	encrypted = otp(alpha, string)
	output = str(header) + encrypted
	file1 = open("cp_encrypt.bmp", "w")
	#print(output)
	file1.write(output)
	#file1.write(struct.pack('<p', output))
	file1.close()

def two_encryptOTP(fname1, fname2, alpha):
	data1 = open(fname1, "rb")
	list1 = data1.readlines()
	pic1 = ""
	for item in list1:
		pic1 += str(item)
	header1 = str(pic1[:54])
	data1 = pic1[54:]
	data1 = data1.split("\\x")
	string1 = str(data1[:54])
	for tup in data1[54:]:
		string1 += tup

	rand_key = randKey(alpha, string1)
	encrypted1 = xor(string1, rand_key)
	output1 = header1 + encrypted1
	data2 = open(fname2, "rb")
	list2 = data2.readlines()
	pic2 = ""
	for item in list2:
		pic2 += str(item[:])
	header2 = str(pic2[:54])
	data2 = pic2[54:]
	data2 = data2.split("\\x")
	string2 = str(data2[:54])
	for tup in data2[54:]:
		string2 += tup
	encrypted2 = xor(string2, rand_key)
	output1 = header2 + encrypted2
	file1 = open("cp_encrypt.bmp", "wb")
	file2 = open("mustang_encrypt.bmp", "wb")
	file1.write(encrypted1)
	file2.write(encrypted2)
	file1.close()
	file2.close()

def twoPadTwo(logo, mustang, alpha):
	data1 = open(logo, "rb")
	list1 = data1.readlines()
	pic1 = ""
	for item in list1:
		pic1 += str(item)
	header1 = str(pic1[:54])
	data1 = pic1[54:]
	data1 = data1.split("\\x")
	string1 = str(data1[:54])
	for tup in data1[54:]:
		string1 += tup
	rand_key = randKey(alpha, string1)
	encrypted1 = xor(string1, rand_key)
	output1 = header1 + encrypted1
	with open(mustang, "rb") as myFile:
		data2 = myFile.read()
	print(len(data2))

if __name__ == "__main__":
	main()

