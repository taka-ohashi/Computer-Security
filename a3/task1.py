from Crypto.Hash import SHA256
from Crypto.Random import random
import time

def main():
	bits = 8 
	while bits != 52:
		hash2same(10, bits)
		bits += 2

def hash2same(length, digest_size):
	start = time.time()
	str1  = create_random_string(length)
	count = 0
	while(1):
		count += 1
		str2 = create_random_string(length)
		h1 = hash256(str1)
		h2 = hash256(str2)
		out1 = output_w_size_limit(h1, digest_size) 
		out2 = output_w_size_limit(h2, digest_size)
		if(compare_hashes(out1, out2)):
			end = time.time()
			print("time: ", str(end - start))
			print("string1: ", str1)
			print("string2: ", str2)
			print("out1: ", out1)
			print("out2: ", out2)
			print("input count: ", count)
			with open("file1.txt", "a") as myfile:
				myfile.write(str(digest_size) + "\n")
				myfile.write("time: " + str(end - start) + "\n")
				myfile.write("str1: " + str1 + "\n")
				myfile.write("str2: " +str2 + "\n")
				myfile.write("out1: " +out1 + "\n")
				myfile.write("out2: " +out2 + "\n")
				myfile.write("count: " + str(count) + "\n\n")
			myfile.close()
			break
	print("collision found")


def create_random_string(length):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	word = ""
	count = 0
	while count < length:
		word += random.choice(alpha)
		count += 1 
	return word

def hash256(stuff):
	h = SHA256.new()
	h.update(stuff.encode())
	return h.hexdigest()

def output_w_size_limit(string, size):
	result = ''.join(format(ord(i), 'b') for i in string)
	return result[:size]

def compare_hashes(str1, str2):
	tup1 = tuple(str1)
	tup2 = tuple(str2)
	for x,y in zip(tup1, tup2):
		if x != y:
			return 0
	return 1

if __name__ == "__main__":
	main()


