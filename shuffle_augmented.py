import random

train_percent=90


dst = r'/home/aih04/dataset/Input.txt'

f1 = open(dst,'r')
f=f1.readlines()


random.shuffle(f)

index=int(len(f)*train_percent/100)
ftrain=f[:index]
ftest=f[index:]

dst = r'/home/aih04/dataset/TrainInput.txt'

f1 = open(dst,'w+')
for i in ftrain:
   f1.write(i)
f1.close()

dst = r'/home/aih04/dataset/TestInput.txt'

f2 = open(dst,'w+')
for i in ftest:
   f2.write(i)
f2.close()

