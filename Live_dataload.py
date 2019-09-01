#this image will be saved in the current working directory which is to be fed to our network

import librosa
from cv2 import imwrite

dur=10

def dataPreprocesses(inputWav)
  audio,fs=librosa.load(inputWav,sr=16000)
   while len(audio)<fs*dur:
     j+=1
     audio=np.concatenate((audio,audio),axis=0)

   audio=audio[0:fs*dur]
   S = librosa.feature.melspectrogram(audio, sr=fs, n_mels=129, fmax=5000,n_fft=1600, hop_length=320)
  
   imwrite('myImage.png',S)

