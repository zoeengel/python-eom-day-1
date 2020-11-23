from random import sample
from random import shuffle

x = sample(range(1,50),6)
x.sort()
print(x)

lotto = list (range(1,50))
mynum = []

for i in range (6):
    shuffle(lotto)
    x = lotto.pop()
    mynum.append(x)

mynum.sort()
print("your lotto numbers are: ", mynum)
