# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:49:54 2019

@author: KETAN
"""

import random

train_percent=90


dst = r'/home/aih04/LID/trainInput.txt'

f1 = open(dst,'r')
f=f1.readlines()


random.shuffle(f)

index=int(len(f)*train_percent/100)
ftrain=f[0:index]
ftest=f[index:-1]

dst = r'/home/aih04/LID/traintInput.txt'

f1 = open(dst,'w')
for i in ftrain:
   f1.write(i)
f1.close()

dst = r'/home/aih04/LID/testInput.txt'

f2 = open(dst,'w')
for i in ftest:
   f2.write(i)
f2.close()














