from moviepy.editor import VideoFileClip

video_path = "IMG_0153.MOV"
audio_path = "audio_IMG_0153.wav"

video = VideoFileClip(video_path)
audio = video.audio
audio.write_audiofile(audio_path)
