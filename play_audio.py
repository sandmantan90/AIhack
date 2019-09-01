import librosa
import IPython.display as ipd

folders=['TAM','GUJ','MAR','HIN','TEL']
address=r"/home/aih04/dataset"

folder=input('TAM,GUJ,MAR,HIN,TEL')
file=input('eg:AI01_HIN_XXX.wav')
load_address=address+'/'+folder+'/'+fil
audio,fs=librosa.load(load_address,sr=16000)
ipd.Audio(audio,rate=fs)
