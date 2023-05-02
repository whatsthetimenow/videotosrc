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
text = r.recognize_google(audio_data, language='zh-CN')

print(text)

# 打开文件，如果文件不存在则创建新文件
with open(f"{textfilename}", "w") as file:
    # 写入文本
    file.write(text)

# 关闭文件
file.close()
