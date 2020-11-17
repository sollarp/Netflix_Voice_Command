from porcupine import Porcupine
import struct
import pyaudio
from Netflix_control import GoogleSearch
import pygame
import os

porcupine = Porcupine(
    library_path='/home/pi/libpv_porcupine.so',
    model_file_path='/home/pi/porcupine_params.pv',
    keyword_file_paths=['/home/pi/bumblebee_raspberry-pi.ppn'],
    sensitivities=[0.5])

# awake = False
start_time = None
wake_time = 3000  # m

# setup audio
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length)

print("I stand ready!")



class wake_up:

    def wake_active(self):
        s_driver_bool = None
        google_search = GoogleSearch()
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            result = porcupine.process(pcm)
            if result:
                # wake-word detected
                print('you sad bumblebee')
                pygame.mixer.init()
                ## Respond with sound
                pygame.mixer.music.load("bee_sound.wav")
                pygame.mixer.music.play()
                ## Turns TV volume 83%
                os.system('sudo amixer cset numid=1 83%')
                change = google_search.secondary_voice(s_driver_bool)
                if change == True:
                    s_driver_bool = True
                else:
                    s_driver_bool = False


start = wake_up()
start.wake_active()