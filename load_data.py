from cv2 import imwrite
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from librosa import display

dur=10
folders=[]

n=np.zeros((1))
address=r"C:\Users\KETAN\OneDrive\Electrical\CDAC-AI Hackthon\dataset"
os.chdir(address)
f=0
i=0
dst = r'C:\Users\KETAN\OneDrive\Electrical\CDAC-AI Hackthon\dataset\trainInput.txt'

f1 = open(dst,'w')
for root, subdirs, files in os.walk('.'):
    print(root, 'lol',subdirs,'::')
    if subdirs==[]:
        f+=1
        print(f)
    for file in files:
        address=root+'\\'+file
        if (os.path.splitext(file)[1]=='.wav')&(file[0]!='.'):
            
            audio,fs=librosa.load(address,sr=16000)
            j=0
            while len(audio)<fs*dur:
                j+=1
                audio=np.concatenate((audio,audio),axis=0)
                
            
            audio=audio[0:fs*dur]
            S = librosa.feature.melspectrogram(audio, sr=fs, n_mels=129, fmax=5000,n_fft=1600, hop_length=320)
            save_address='/home/aih04/dataset/train/'+str(n)
            imwrite(save_address,S)
    
            
            file= str(int(n))+' '+str((f-1))
            f1.write(file+'\n')
              
            

            
            print(S.shape)
            print(f-1)
            i+=1             
           
            
            print(n,':',file)
            n+=1
f1.close()        
        
