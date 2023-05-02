import urllib.request
import speech_recognition as sr

# 下载中文语音模型
lm_url = "https://github.com/bamtercelboo/chinese_models/raw/master/zh_broadcastnews-032020-cedict/zh_broadcastnews-032020-cedict.lm.bin"
lm_file = "data/model/zh_broadcastnews-032020-cedict.lm.bin"
urllib.request.urlretrieve(lm_url, lm_file)

dic_url = "https://github.com/bamtercelboo/chinese_models/raw/master/zh_broadcastnews-032020-cedict/zh_broadcastnews-032020-cedict.dic"
dic_file = "data/dict/zh_broadcastnews-032020-cedict.dic"
urllib.request.urlretrieve(dic_url, dic_file)

# 创建Recognizer对象
recognizer = sr.Recognizer()

# 读取音频文件
audio_file = "audio_IMG_0153.wav"
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)

# 将音频转换为文本
try:
    text = recognizer.recognize_sphinx(audio, language='zh-CN')
    print("转换结果：", text)
except Exception as e:
    print("出现错误：", str(e))
