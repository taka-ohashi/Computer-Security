def main():
   #lst = openfile("caesar_easy_encrypted.txt")
   englishFreq = [0, 8.12, 1.49, 2.71, 4.32, 12.02, 2.30, 2.03, 5.92, 7.31, 0.10, 0.69, 3.98, 2.61, 6.95, 7.68, 1.82, 0.11, 6.02, 6.28, 9.1, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07]
   doubles = {'th':2.71, 'he': 2.33, 'in': 2.03, 'er':1.78, 'an':1.61, 're':1.41, 'es':1.32, 'on':1.32, 'st': 1.25, 'nt':1.17, 'en':1.13, 'at':1.12, 'ed': 1.08, 'nd':1.07, 'to': 1.07, 'or': 1.6, 'ea':1.00, 'ti':0.99, 'ar':0.98, 'te':0.98, 'ng':0.89, 'al':0.88, 'it':0.88, 'as': 0.87, 'is':0.86, 'ha':0.83, 'et':0.76, 'se':0.73, 'ou':0.72, 'of':0.71}
   triples = {'the': 1.81, 'and':0.73,'ing':0.72,'ent':0.42, 'ion': 0.42, 'her':0.36, 'for':0.34, 'tha':0.33, 'nth': 0.33, 'int':0.32, 'ere':0.31,'tio':0.31, 'ter':0.30, 'est':0.28, 'ers':0.28, 'ati':0.26, 'hat':0.26,'ate':0.25, 'all':0.25, 'all':0.25, 'eth': 0.24, 'hes':0.24, 'ver':0.24, 'his': 0.24, 'oft':0.22, 'ith':0.21, 'fth': 0.21, 'sth':0.21, 'oth':0.21, 'res':0.21, 'ont':0.20}
   monodict = {'z':'a', 'a': 'w', 'r':'d', 'b':'e', 'u':'f', 'n':'g', 'x':'h', 'l':'i', 't':'m', 'd':'l', 'k':'m', 'i':'n', 'q':'p', 's':'o', 'g':'r', 'f':'s', 'k':'t', 'w':'u', 'c':'v', 'd':'y', 'e':'z', 'h':'x', 'j':'l', 'm':'k', 'o':'c', 'p':'j', 'v':'Q', 'y':'b'}
   key2 = {'a':'t', 'b':'f', 'c':'o', 'd':'r', 'e':'d', 'f':'m', 'g':'l', 'h':'h', 'i':'b', 'j':'n', 'k':'X', 'l':'p', 'm':'c', 'n':'v', 'o':'w', 'p':'g', 'q':'X', 's':'i', 't':'j', 'r':'u','u':'y', 'v':'a', 'w':'k', 'x':'e', 'y':'s', 'z':'x'}


   #caesar_salad("caesar_easy_encrypted.txt", englishFreq)
   #caesar_salad("caesar_easy_2_encrypted.txt", englishFreq)
   #caesar_salad("caesar_hard_encrypt.txt", englishFreq)
   #caesar_salad("caesar_hard_2_encrypt.txt", englishFreq)
   #monocipher( "mono_easy_encrypt.txt",englishFreq, doubles, triples, monodict)
   #monocipher( "mono_medium_encrypt.txt",englishFreq, doubles, triples, key2)

   #lst = openfile("qwert.txt")
   #print(separate_parts(lst[0], 5))
   vegan_cipher('vigerene_easy_encrypted.txt', englishFreq, 5)


def caesar_salad(fname, english):
   first = 1
   min_chi = 100000000
   min_shift = 0
   total = 0
   count = 0 
   loop = 1 
   chi_squared = 0
   #open file and read 
   list = openfile(fname)
   total = countTotal(list)
   str1 = list[0]
   while loop < 27:
      freqTable = [0]*27
      freqTable = countFreq(str1)
      chi_squared = calc_chi_squared(freqTable, english, total)
   
      if chi_squared < min_chi:
          min_chi = chi_squared
          min_shift = count
      count += 1 
      newstr = ""
      for letter in str1:
         if ord(letter) >= 65 and ord(letter) <= 122 and letter.isalpha():
            newstr = newstr + rotate(letter)
         else:
            newstr = newstr + letter
      str1 = newstr
      loop += 1 
	#rotate all letters by count
   str1 = list[0]
   print("Key: ", min_shift)
   output = rotate_string(str1, min_shift)
   print(output)

def monocipher(fname, singles, doubles, triples, monodict):
   total = 0 
   letterFreq = [0]*27
   tupleFreq = {}
   tripFreq = {} 
   cipherKey = {}
   ciphered = ""
   #open file and read
   list = openfile(fname)
   for thing in list:
      ciphered += thing
   #Count occurances in text 
   total = countTotal(ciphered)
   letterFreq = countFreq(ciphered)
   tupleFreq = countTuples(ciphered, doubles)
   #tripFreq = countTriples(ciphered, triples)
   #print ("{:<8} {:<15}".format('Tuple', 'Frequency') )
   #for k, v in tupleFreq.items():
    #  frequency = v
     # print ("{:<8} {:<15}".format(k, frequency) )
   cipherKey = createKey(singles, letterFreq)
   keylist = cipherKey.keys()
   #substitute based on stats
   #print(decodeMono(ciphered, cipherKey, keylist))
   keylist = monodict.keys()
   print(decodeMono(ciphered, monodict, keylist))

def vegan_cipher(fname, english, key_length):
   lst1 = openfile(fname)
   ciphered = ""
   for thingy in lst1:
      ciphered += thingy
   parts = separate_parts(ciphered, key_length)
   i = 0
   output = ""
   while i < len(parts):
      min_shift = caesar2(parts[i], english)
      print(min_shift)
      #output += rotate_string(parts[i], min_shift)
      i += 1

def caesar2(string, english):
   min_chi = 100000000
   min_shift = 0
   total = 0
   count = 0 
   loop = 1 
   chi_squared = 0
   total = countTotal(string)
   while loop < 27:
      freqTable = [0]*27
      freqTable = countFreq(string)
      #print(freqTable)
      chi_squared = calc_chi_squared(freqTable, english, total)
      if chi_squared < min_chi:
          min_chi = chi_squared
          min_shift = count
      count += 1 
      newstr = ""
      for letter in string:
         if ord(letter) >= 65 and ord(letter) <= 122 and letter.isalpha():
            newstr = newstr + rotate(letter)
         else:
            newstr = newstr + letter
      string = newstr
      loop += 1
   return min_shift


def separate_parts(ciphered, key_length):
   filtered = filter_non_alpha(ciphered)
   parts = []
   text_length = len(filtered)
   part_length = text_length / key_length
   #remaining = text_length % key_length
   for i in range(key_length):
      current_part = ""
      mod = i % key_length
      for letter in filtered:
         location = filtered.index(letter)
         if location % key_length == mod:
            current_part += letter
      parts.append(current_part)
   return parts

def decodeMono(text, cipherKey, key):
   new = []
   for letter in text:
      letter = letter.lower()
      if ord(letter) >= 65 and ord(letter) <= 122 and letter.isalpha():
        new.append(cipherKey.get(letter))
      else:
        new.append(letter)
   return "".join(new) 

def createKey(singles, textFreq):
   cipherKey = {}
   i = 1
   j = 0 
   #arrays of visited letters
   visitedSingle = []
   visitedText = []
   #max value found in array 
   maxSingle = 0
   maxText = 0 
   #index to be stored in visited
   indexSingle = 0
   indexText = 0
   #letter corresponding to max value 
   singlesLetter = ""
   textLetter = "" 

   #take the biggest value from each list 
   #find corresponding letters in each list
   while j < 26:
      i = 0
      maxSingle = 0
      maxText = 0
      while i < 27:
         if (i not in visitedSingle) and (singles[i] > maxSingle):
            indexSingle = i
            maxSingle = singles[i]
            singlesLetter = chr(i + 96)
         if (i not in visitedText) and (textFreq[i] > maxText):
            indexText = i
            maxText = textFreq[i]
            textLetter = chr(i + 96)
         i +=1

      #map both letters to dictionary 
      cipherKey[textLetter] = singlesLetter

      #take out current index by storing in visited array   
      visitedSingle.append(indexSingle)
      visitedText.append(indexText)
      

      j += 1

   return cipherKey


def sub_tuple(text, old_tuple, new_tuple):
   idx = 0
   output = ""
   while idx < len(text) - 1:
      newtxt = ""
      curr_tuple = ""
      curr_tuple += text[idx] + text[idx + 1]
      if curr_tuple == old_tuple:
         newtxt = output + new_tuple
         idx += 2
      else:
         newtxt = output + text[idx]
         idx += 1
      output = newtxt
   return output + text[len(text)-1]

def sub_triple(text, triple):
   return text

def rotate_string(str1, min_shift):
   loop = 0 
   while loop < min_shift:
      newstr = ""
      for letter in str1:
         if ord(letter) >= 65 and ord(letter) <= 122 and letter.isalpha():
            newstr = newstr + rotate(letter)
         else:
            newstr = newstr + letter
      str1 = newstr
      loop += 1
   return str1

def calc_chi_squared(freqTable, english, total):
   chi_squared = 0
   idx = 1
   while idx < 27:
      expected = 0
      observed = 0 
      expected = total * (english[idx] / 100)
      observed = freqTable[idx]
      chi_squared = chi_squared + ((observed - expected)**2) / expected
      idx += 1 
   return chi_squared

def openfile(fname):
   fd = open(fname, "r")
   list = fd.readlines()
   return list

def countTotal(list):
   count = 0
   for letter in list[0]:
      if ord(letter) >= 65 and ord(letter) <= 122 and letter.isalpha():
         count+=1
   return count

def countFreq(list):
   freqTable = [0] * 27
   for letter in list:
      if ord(letter) >= 65 and ord(letter) <= 122 and letter.isalpha():
         letter = letter.lower()
         index = ord(letter) - 96
         freqTable[index]+=1
   return freqTable

def countTuples(text, doubles):
   text = filter_non_alpha(text)
   tuples = {} 
   length = len(text)
   i = 0
   while i < (length - 1):
      currDub = ""
      currDub += text[i] + text[i+1]
      # searche {doubles} for currentdouble
      if currDub in tuples:
         tuples[currDub] += 1 
      else:
         tuples[currDub] = 1 
      i += 1 
   return tuples
   
def countTriples(text, triples):
   text = filter_non_alpha(text)
   triples = {} 
   length = len(text)
   i = 0
   while i < (length - 2):
      currTriples = ""
      currTriples += text[i] + text[i+1] + text[i+2]
      # searche {doubles} for currentdouble
      if currTriples in triples:
         triples[currTriples] += 1 
      else:
         triples[currTriples] = 1 
      i += 1 
   return triples

def filter_non_alpha(str_text):
   temp_text = ""
   for i in str_text:
      if ord(i) >= 65 and ord(i) <= 122 and i.isalpha():
         temp_text += i
   str_text = temp_text
   return str_text

def rotate(letter):
	output = ''
	if ord(letter) == 65:
		output = 'Z'
	elif ord(letter) == 97:
		output = 'z'
	else:
		output = chr(ord(letter) - 1)
	return output

if __name__ == "__main__":
	main()
