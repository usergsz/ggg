from aip import AipSpeech
from playsound import playsound
import os

def shuohua(text):
    APP_ID = '27411377'
    API_KEY = 'CajZUk1cHLaIDpGbEHwyFzX6'
    SECRET_KEY = 'cs0IvRonZvtnliRGiGIePzjxuq6lcNun'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    #vol：音量；spd:语速；pit:音调；per:精品音库5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美 
    result  = client.synthesis(text,'zh',1,{'vol':9,'spd':5,'pit':5,'per':4})
    if not isinstance(result,dict):
        with open('audio.mp3','wb+') as f:
            f.write(result)
    playsound('audio.mp3')
    os.remove('audio.mp3')
