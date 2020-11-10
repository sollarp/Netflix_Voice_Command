import pygame
import text_to_speech_goog_ai ## good
import os


def text_send_to_server():
    
    
    create_text = input("requested text: ")
    return create_text

def play_mp3_content():
    os.system('sudo amixer cset numid=1 100%')
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('text.mp3')
    pygame.mixer.music.play()
    #pygame.event.wait()
    print("end of scrip")
    os.system('sudo amixer cset numid=1 85%')
#text_send_to_server()
