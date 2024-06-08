from transformers import pipeline
import torch
from pydub import AudioSegment
import numpy as np
device = "cuda:0" if torch.cuda.is_available() else "cpu"
pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-tiny",
  chunk_length_s=30,
  device=device,
)
def load_audio(path, format):
  audio = AudioSegment.from_file(path, format=format)

  if audio.frame_rate != 16000: # 16 kHz
    audio = audio.set_frame_rate(16000)

  if audio.sample_width != 2:   # int16
      audio = audio.set_sample_width(2)

  if audio.channels != 1: # mono
      audio = audio.set_channels(1)

  arr = np.array(audio.get_array_of_samples())
  arr = arr.astype(np.float32)/32768.0

  return arr
path = '/content/drive/MyDrive/sample3.flac'
format = 'flac'
data = {
    'path': path,
    'array': load_audio(path, format),
    'sampling_rate': 16000
    }
prediction = pipe(data.copy(), batch_size=8)["text"]
print(prediction)