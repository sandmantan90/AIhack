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
    
    die=np.random.randint(0,2)
    
    if die==1
               
        noise_mag=np.random.uniform(0,.1)
        data1=change_pitch(data,1.5)
        data1=stretch(data1, 1.23)
        data1= np.roll(data1, int(len(data)/3))#make the content different
        data1+=noise[:len(data1)]*noise_mag
        
        noise_mag=np.random.uniform(0,.1)
        data2=change_pitch(data,-1.5)
        data2=stretch(data2, .83)
        data2= np.roll(data2, int(2*len(data)/3))#make the content different
        data2+=noise[:len(data2)]*noise_mag
        
    else:
        noise_mag=np.random.uniform(0,.1)
        data1=change_pitch(data,1.5)
        data1=stretch(data1, .83)
        data1= np.roll(data1, int(len(data)/3))#make the content different
        data1+=noise[:len(data1)]*noise_mag
        
        noise_mag=np.random.uniform(0,.1)
        data2=change_pitch(data,-1.5)
        data2=stretch(data2, 1.23)
        data2= np.roll(data2, int(2*len(data)/3))#make the content different
        data2+=noise[:len(data2)]*noise_mag
    
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
                
                samples=fs*dur                
                
                noFrames = 0
                if len(audio)<samples:
                    while len(audio)<samples:
                        audio = np.concatenate((audio,audio), axis=0)
                    audio = audio[:samples]
                    noFrames = 1

                elif (len(audio) % samples > samples*0.5):
                    noFrames = int(np.ceil(len(audio) / samples))
                    audio = np.concatenate((audio,audio), axis=0)
                    audio = audio[:noFrames*samples]

                elif (len(audio) % samples < samples*0.5):
                    noFrames = int(np.floor(len(audio) / samples))
                    audio = audio[:noFrames*samples]

             
                for j in range(int(noFrames)):
                    clip = audio[j*samples:(j+1)*samples]   
                    
                    clip1,clip2 = augment(clip)
                    
                    #for clip
                    melspec = librosa.feature.melspectrogram(clip, sr = samples,
                                                             n_mels = 129, fmax = 5000,
                                                             n_fft = 1600, hop_length = 192)                    
                    melspec=librosa.power_to_db(melspec,ref=np.max)

                    save_address='/home/aih04/dataset/Augmented_train/'+str(int(n))+'.png'#CHANGE THIS ADDRESS
                    imwrite(save_address,melspec)
                    file= str(int(n))+' '+str((f))
                    f1.write(file+'\n')
                    n+=1
                    
                    #for clip1
                    melspec = librosa.feature.melspectrogram(clip1, sr = samples,
                                                             n_mels = 129, fmax = 5000,
                                                             n_fft = 1600, hop_length = 192)                    
                    melspec=librosa.power_to_db(melspec,ref=np.max)

                    save_address='/home/aih04/dataset/Augmented_train/'+str(int(n))+'.png'#CHANGE THIS ADDRESS
                    imwrite(save_address,melspec)
                    file= str(int(n))+' '+str((f))
                    f1.write(file+'\n')
                    n+=1
                    
                    #for clip2
                    melspec = librosa.feature.melspectrogram(clip2, sr = samples,
                                                             n_mels = 129, fmax = 5000,
                                                             n_fft = 1600, hop_length = 192)                    
                    melspec=librosa.power_to_db(melspec,ref=np.max)

                    save_address='/home/aih04/dataset/Augmented_train/'+str(int(n))+'.png'#CHANGE THIS ADDRESS
                    imwrite(save_address,melspec)
                    file= str(int(n))+' '+str((f))
                    f1.write(file+'\n')
                    n+=1        
                                                                   
                print(f,':',n,':',fil)
                
f1.close()
