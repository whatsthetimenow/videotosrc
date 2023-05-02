import sys
import speech_recognition as sr

# 获取文件名
audiofilename = sys.argv[1]
textfilename = sys.argv[2]

# 创建一个识别器实例
r = sr.Recognizer()

# 打开音频文件
with sr.AudioFile(audiofilename) as source:
    audio_data = r.record(source)  # 从文件中读取音频数据

# 将音频数据传递给语音识别器进行转换
text = r.recognize_sphinx(audio_data, language='zh-CN')

# 将识别结果写入文件
with open(textfilename, 'w', encoding='utf-8') as f:
    f.write(text)

# 关闭文件
f.close()