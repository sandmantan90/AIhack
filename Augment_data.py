'''
read each audio file and make 2 augmented copies of each.
augmentation includes random pitch shift, random time scaling, time shifting and random magnitude noise addition
'''

from cv2 import imwrite
import os
import librosa
import numpy as np
import random

dur=10#sec
augment_no=3
folders=['TAM','GUJ','MAR','HIN','TEL']
n=0#file number counter
address=r"/home/aih04/dataset"
os.chdir(address)

dst = r'/home/aih04/LID/Augmented_trainInput.txt'

def addNoise(data,noise=noise):
    noise_mag=np.random.uniform(0,.1)
    data+=noise[:10*fs]*noise_mag
    
    return data

def augment(data):
  dice = random.randint(0, 1)
  if bool(dice):
    
    data1=change_pitch(data,1.5)
    data1=stretch(data1, 1.23)
    data1= np.roll(data1, int(2*np.floor(len(data1)/3)))#make the content different
    
    data2=change_pitch(data,-1.5)
    data2=stretch(data2, .81)
    data2= np.roll(data2, int(np.floor(len(data2)/3)))
    
  else:
    
    data1=change_pitch(data,1.5)
    data1=stretch(data1, .81)
    data1= np.roll(data1, int(2*np.floor(len(data1)/3)))
    
    data2=change_pitch(data,-1.5)
    data2=stretch(data2, 1.23)
    data2= np.roll(data2, int(np.floor(len(data2)/3)))
    
  return(data1,data2)
    
    
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
                audio1,audio2=augment(audio)
                
                #add noise
                for aud in [audio,audio1,audio2]:
                  aud=addNoise(aud)
                                
                S = librosa.feature.melspectrogram(audio, sr=fs, n_mels=129, fmax=5000,n_fft=1600, hop_length=320)
                save_address='/home/aih04/dataset/Augmented_train/'+str(int(n))+'.png'
                imwrite(save_address,S)
                file= str(int(n))+' '+str((f))
                f1.write(file+'\n')
                n+=1
                
                S1 = librosa.feature.melspectrogram(audio1, sr=fs, n_mels=129, fmax=5000,n_fft=1600, hop_length=320)
                save_address='/home/aih04/dataset/Augmented_train/'+str(int(n))+'.png'
                imwrite(save_address,S1)
                file= str(int(n))+' '+str((f))
                f1.write(file+'\n')
                n+=1
                
                S2 = librosa.feature.melspectrogram(audio2, sr=fs, n_mels=129, fmax=5000,n_fft=1600, hop_length=320)
                save_address='/home/aih04/dataset/Augmented_train/'+str(int(n))+'.png'
                imwrite(save_address,S2)
                file= str(int(n))+' '+str((f))
                f1.write(file+'\n')
                n+=1
                
                
                print(f,fil)
                print(n,':',fil)
                
f1.close()


  
