from nltk.corpus import words
import bcrypt
import threading
import os

str1 = "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq"
str2 = "$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC"
str3 = "$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q"
crypts1 = [str1, str2, str3]

str4 = "$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm"
str5 = "$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im"
crypts2 = [str4, str5]

str6 = "$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom"
str7 = "$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be"
str8 = "$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK"
crypts3 = [str6, str7, str8]

str9 = "$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q"
str10 = "$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq"
str11 = "$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12"
crypts4 = [str9, str10, str11]

str12 = "$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O"
str13 = "$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK"
str14 = "$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O"
crypts5 = [str12, str13, str14]

str15 = "$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"
crypts6 = [str15]

salt1 = "$2b$08$J9FW66ZdPI2nrIMcOxFYI."
salt2 = "$2b$09$M9xNRFBDn0pUkPKIVCSBzu"
salt3 = "$2b$10$xGKjb94iwmlth954hEaw3O"
salt4 = "$2b$11$/8UByex2ktrWATZOBLZ0Du"
salt5 = "$2b$12$rMeWZtAVcGHLEiDNeKCz8O"
salt6 = "$2b$13$6ypcazOOkUT/a7EwMuIjH."

temp = words.words()
wordlist = []
for w in temp:
	if 6 < len(w) < 10:
		wordlist.append(w)

def find_hash(salt, crypts):
	count = 0
	for w in wordlist:
		password = w.encode()
		s = salt.encode()
		for c in crypts:
			if bcrypt.checkpw(password, c.encode()):
				print(c)
				print("password: ", password)
				print('\n')

if __name__ == "__main__":
	#print("salt1")
	#find_hash(salt1, crypts1)
	print("salt6 start")
	find_hash(salt6, crypts6)

	'''thread1 = threading.Thread(target = find_hash, args = (salt1, crypts1))
	thread2 = threading.Thread(target = find_hash, args = (salt2, crypts2))
	thread3 = threading.Thread(target = find_hash, args = (salt3, crypts3))
	thread4 = threading.Thread(target = find_hash, args = (salt4, crypts4))
	thread5 = threading.Thread(target = find_hash, args = (salt5, crypts5))
	thread6 = threading.Thread(target = find_hash, args = (salt6, crypts6))'''

	'''print("starting thread1")
	thread1.start()
	print("starting thread2")
	thread2.start()
	print("starting thread3")
	thread3.start()
	print("starting thread4")
	thread4.start()
	print("starting thread5")
	thread5.start()
	print("starting thread6")
	thread6.start()'''

	'''thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	thread5.join()
	thread6.join()'''

