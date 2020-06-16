from Crypto.Cipher import AES
from Crypto.Random import random
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad 
import math

#sends
#p = 37
#g = 5

p = "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371"
g = "A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5"

p = int(str(p), 16)
g = int(str(g), 16)

print(p)
print(g)

#x and y are between 1 and p-1
x = 2 #only Alice knows
y = 3 #only Bob knows

alice = pow(g, x,p)
bob = pow(g, y, p)

AliceComp = pow(bob, x, p)
BobComp = pow(alice, y, p)
print('AliceComp', AliceComp)
print('BobComp', BobComp)

keyA = SHA256.new()
keyA.update(str(AliceComp).encode())
keyB = SHA256.new()
keyB.update(str(BobComp).encode())

Akey = keyA.digest()[:16]
Bkey = keyB.digest()[:16]
print('keyA digest: ', Akey)
print('keyB digest: ', Bkey)

AliceMessage = pad('Hi Bobby'.encode(), 16)
BobMessage = pad('Hi Alice'.encode(), 16)

cipher = AES.new(Akey, AES.MODE_CBC)
ciph_A = cipher.encrypt(AliceMessage)

cipherB = AES.new(Bkey, AES.MODE_CBC)
ciph_B = cipher.encrypt(BobMessage)

print('ciph_A', ciph_A)
print('ciph_B', ciph_B)