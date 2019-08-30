# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:49:54 2019

@author: KETAN
"""

import os
import librosa
import numpy as np
import random

test_percent=10


dst = r'/home/aih04/LID/trainInput.txt'

f1 = open(dst,'r')
f=f1.readlines()


f=random.shuffle(f)
index=int(len(f)*test+percent/100)
ftrain=f[0:index]
ftest=f[index:-1]

dst = r'/home/aih04/LID/traintInput.txt'

f1 = open(dst,'w')
f1.write(ftrain)
f1.close()
dst = r'/home/aih04/LID/testInput.txt'
f2 = open(dst,'w')
f2.write(ftest)
f2.close()















'''





for f,folder in enumerate(folders):
    os.chdir(address+'/'+folder)
    for root, subdirs, files in os.walk('.'):
        print(root, 'lol',subdirs,'::',files)
        for fil in files:
            load_address=address+'/'+folder+'/'+fil
            if (os.path.splitext(fil)[1]=='.wav'):
                audio,fs=librosa.load(load_address,sr=16000)

                while len(audio)<fs*dur:
                    j+=1
                    audio=np.concatenate((audio,audio),axis=0)


                audio=audio[0:fs*dur]
                S = librosa.feature.melspectrogram(audio, sr=fs, n_mels=129, fmax=5000,n_fft=1600, hop_length=320)
                save_address='/home/aih04/dataset/Train/'+str(int(n))+'.png'
                imwrite(save_address,S)
                file= str(int(n))+' '+str((f))
                f1.write(file+'\n')
                print(f,fil)
                print(n,':',fil)
                n+=1
               #file number counter
f1.close()
''' 