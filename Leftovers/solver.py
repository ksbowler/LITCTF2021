from sympy.ntheory.modular import crt
import random
from Crypto.Util.number import *
import sympy
import math

val = [16751036754, 7441743891, 13537409447, 12455208971, 16901669565, 15060041617, 15538665605, 192375025, 2176355740, 21877084789, 3184436468, 13214581420]

random.seed(1337)
mod = []
for i in range(len(val)):
	mod.append(sympy.prevprime(random.randint(1,4e10)))

print(val)
print(mod)
#print(crt(mod,val))
flag, MOD = crt(mod,val)
flag = int(flag)
while math.log10(flag) <= 128:
	FLAG = long_to_bytes(flag)
	flag += MOD
	if b"flag" in FLAG:
		print(FLAG)
		break
