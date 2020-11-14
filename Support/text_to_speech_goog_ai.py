import pygame
import os
from google.cloud import texttospeech
#from text_to_speech_helper import text_send_to_server
from text_to_speech_helper import play_mp3_content
#from projetc_X import play_mp3_content
    
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YOUR JSON API KEY"


# Instantiates a client
def speech_result_return(create_text):

    
    client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
    #text_send_to_server2 = text_send_to_server()
    text_send_to_server2 = create_text
    #text_send_to_server2 = input("nyomjad: ")
    synthesis_input = texttospeech.SynthesisInput(text=text_send_to_server2)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
    language_code="en-GB", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
    response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config)

# The response's audio_content is binary.
    with open("text.mp3", "wb") as out:
        file = out.write(response.audio_content)
        print('Audio content written to file "text.mp3"')
        play_mp3_content()
        
