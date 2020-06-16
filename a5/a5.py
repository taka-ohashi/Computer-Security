from Crypto.Cipher import AES
from Crypto.Random import random
from Crypto.Util.Padding import pad, unpad 
import json
from base64 import b64encode

def main():
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	#str1, header = getInput('mustang.bmp')
	#ecb(str1, header, alpha, 16)
	#cbc(str1, header, alpha, 16)
	key = randKey(alpha, 16).encode()
	cipher = AES.new(key, AES.MODE_CBC)
	string = ';admin=true;'
	ciphertext = submit(string, key, cipher)
	cipher2 = AES.new(key, AES.MODE_CBC, cipher.iv)
	print(ciphertext)
	print(verify(ciphertext, cipher2))

#takes in plaintext file
def getInput(fname):
	string = ""
	file = open(fname, "rb")
	data = file.readlines()
	for tup in data:
		string += str(tup)
	data = string.split("\\x")
	string = ""
	for i in data:
		string += i
	header = string[:105]
	string = string[105:]
	return string, header
	

#ecb
def ecb(input1, header, alpha, keyLen):
	key = randKey(alpha, keyLen).encode()
	cipher = AES.new(key, AES.MODE_ECB)
	input1 = pad(input1.encode(), 16)
	ciphertext = cipher.encrypt(input1)
	file1 = open("mustang_encrypt.bmp", "wb")
	file1.write(header.encode())
	file1.write(ciphertext)
	file1.close()

#cbc
def cbc(input1, header, alpha, keyLen):
	key = randKey(alpha, keyLen).encode()
	cipher = AES.new(key, AES.MODE_CBC)
	input1 = pad(input1.encode(), 16)
	ciphertext = cipher.encrypt(input1)
	file1 = open("mustang_encrypt.bmp", "wb")
	file1.write(header.encode())
	file1.write(ciphertext)
	file1.close()

def randKey(alpha, keyLen):
	key = ""
	count = 0
	while count < keyLen:
		key += random.choice(alpha)
		count += 1
	return key


# # # # # task 2 # # # # #
#generate random AES key and IV in the main
def submit(input, key, cipher):
	string = ''
	for i in input:
		#i = i.replace(';', '%3b').replace('=', '%3d')
		i = i.replace(';', '@').replace('=', '@')
		string += i
	string  = "userid=456;userdata=" + string + ";session-id=31337"
	string = pad(string.encode(), 16)
	ciphertext = cipher.encrypt(string)
	return ciphertext 

def verify(ciphertext, cipher):
	decrypted = cipher.decrypt(ciphertext)
	decryptedAndUnpadded = unpad(decrypted, 16)
	if ';admin=true;' in decryptedAndUnpadded.decode():
		return True
	return False

def alterText():
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	key = randKey(alpha, 16).encode()
	cipher = AES.new(key, AES.MODE_CBC)
	cipher_list = []
	msg = ";admin=true;"
	ciphertext = submit(msg, key, cipher)
	i = 0
	while i*16 <= len(ciphertext):
	    cipher_list.append(ciphertext[i*16: 16 + (i*16)])
	    i += 1
	attack_on_block = cipher_list[1]
	list1 = list(attack_on_block)
	list1[0] = chr(list1[0] ^ ord('@') ^ ord(";"))
	list1[6] = chr(list1[6] ^ ord('@') ^ ord("="))
	list1[11] = chr(list1[11] ^ ord('@') ^ ord(";"))
	print(list1)


	newList1 = []
	for i in list1:
		newList1.append(str(i))
	cipher_list[1] = ''.join(newList1)
	newCipherList = []
	for i in cipher_list:
		newCipherList.append(str(i))
	ciphertext = ''.join(newCipherList)
	cipher2 = AES.new(key, AES.MODE_CBC, cipher.iv)
	#ciphertext = pad(ciphertext.encode(), 16)
	print(ciphertext)
	ciphertext = ciphertext.encode()
	print(ciphertext)
	print(type(ciphertext))
	verify(ciphertext, cipher2)


if __name__ == "__main__":
	#main()
	alterText()
