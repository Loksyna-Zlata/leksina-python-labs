from array import*
import random
spysok = []
for i in range(10, 21):
   spysok.append(i)
masyv = array('i', spysok)
random.shuffle(masyv)
print("Числа розташовані у випадковій послідовності: ", masyv)