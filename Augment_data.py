'''
read each audio file and make 2 augmented copies of each.
augmentation includes random pitch shift, random time scaling, time shifting and random magnitude noise addition.
'''

from cv2 import imwrite
import os
import librosa
import numpy as np
import random

dur=6#sec
folders=['TAM','GUJ','MAR','HIN','TEL']
n=0#file number counter
address=r"/home/aih04/dataset"
os.chdir(address)

dst = r'/home/aih04/LID/Augmented_trainInput.txt'
noise,fs=librosa.load(r"/content/drive/My Drive/noise7.wav",sr=16000)#CHANGE THIS ADDRESS


def augment(data,noise=noise):
    
    p = np.random.uniform(-1.5, 1.5)
    s=np.random.uniform(.83, 1.23)
    roll=np.random.uniform(0, len(data))
    noise_mag=np.random.uniform(0,.1)
    
    data=change_pitch(data,p)
    data=stretch(data, s)
    data= np.roll(data, int(roll))#make the content different
    data+=noise[:dur*fs]*noise_mag
    
    return(data)

    
def change_pitch(data, semitone=1):
    input_length =len(data)
    data = librosa.effects.pitch_shift(data, 16000, semitone, bins_per_octave=12)
    if len(data)>input_length:
        data = data[:input_length]
    else:
        while len(data)<input_length:
            data=np.concatenate((data,data),axis=0)
            
        data=data[0:input_length]
    return data
  
def stretch(data, rate=2):
    input_length =len(data)
    data = librosa.effects.time_stretch(data, rate )
    if len(data)>input_length:
        data = data[:input_length]
    else:
        while len(data)<fs*dur:
            data=np.concatenate((data,data),axis=0)

        data=data[0:input_length]
    return data

f1 = open(dst,'w')
for f,folder in enumerate(folders):
    os.chdir(address+'/'+folder)
    for root, subdirs, files in os.walk('.'):
        print(root, 'lol',subdirs,'::',files)
        for fil in files:
            load_address=address+'/'+folder+'/'+fil
            if (os.path.splitext(fil)[1]=='.wav'):
                audio,fs=librosa.load(load_address,sr=16000)

                while len(audio)<fs*dur:
                    audio=np.concatenate((audio,audio),axis=0)

                audio=audio[0:fs*dur]
                audio=augment(audio)             
                              
                                
                S = librosa.feature.melspectrogram(audio, sr=fs, n_mels=129, fmax=5000,n_fft=1600, hop_length=192)
                S=librosa.power_to_db(S,ref=np.max)
                
                save_address='/home/aih04/dataset/Augmented_train/'+str(int(n))+'.png'#CHANGE THIS ADDRESS
                imwrite(save_address,S)
                file= str(int(n))+' '+str((f))
                f1.write(file+'\n')
                n+=1
                                                
                print(f,':',n,':',fil)
                
f1.close()


  
