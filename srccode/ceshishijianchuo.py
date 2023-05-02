from pydub import AudioSegment
import speech_recognition as sr
import os

def split_audio(audio_file, chunk_size_ms):
    chunks = []
    start = 0
    end = chunk_size_ms
    while end <= len(audio_file):
        chunks.append(audio_file[start:end])
        start = end
        end += chunk_size_ms
    return chunks

def transcribe_audio(audio_chunk):
    r = sr.Recognizer()
    with sr.AudioFile(audio_chunk) as source:
        audio = r.record(source)
        text = r.recognize_google(audio, language="zh-CN")
        return text

audio_file = AudioSegment.from_file("audio_65_raw.wav", format="wav")
chunk_size_ms = 10000
audio_chunks = split_audio(audio_file, chunk_size_ms)

subtitles = []
for i, chunk in enumerate(audio_chunks):
    chunk_file = "chunk{0}.wav".format(i)
    chunk.export(chunk_file, format="wav")
    text = transcribe_audio(chunk_file)
    subtitles.append(text)
    os.remove(chunk_file)

with open("subtitles.srt", "w", encoding="utf-8") as f:
    for i, subtitle in enumerate(subtitles):
        start_time = i * chunk_size_ms
        end_time = (i + 1) * chunk_size_ms
        f.write("{0}\n{1} --> {2}\n{3}\n\n".format(i+1, start_time, end_time, subtitle))
