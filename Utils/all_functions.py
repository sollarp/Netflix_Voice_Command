import urllib.request
import urllib.parse
import vlc
import re
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from Support import Tkinter
import os
from text_to_speech_goog_ai import speech_result_return
import pygame
from sqlite_test import data_entry
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


def terminate_all_process(self):
    try:
        self.driver.close()
        return False
    except:
        self.player.stop()


def play_mp3(self, mp3_input):
    os.system('sudo amixer cset numid=1 100%')
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_input)
    pygame.mixer.music.play()
    # pygame.event.wait()
    print("end of scrip")
    os.system('sudo amixer cset numid=1 85%')


def calling_vlc(self, vlc_input):
    self.player = vlc.MediaPlayer(vlc_input)


def text_onscreen(self, screen_text):
    self.label = tkinter.Label(text=screen_text, font=('Times', '30'), fg='lime green', bg='white')
    self.label.master.overrideredirect(True)
    self.label.master.geometry("+850+50")
    self.label.master.wm_attributes("-topmost", True)
    self.label.pack()
    self.label.update()
    self.label.after(2000)
    self.label.master.destroy()


def website_request(self, text):
    query_string = urllib.parse.urlencode({"search_query": text})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    return search_results


def text_send_to_server(self, result_search_for):  ##text to speach google API
    create_text = (result_search_for)
    speech_result_return(create_text)


def text_lenght_result(self, last_word, text_q):
    print(text_q)
    s1 = text_q
    s2 = last_word
    print(s1[s1.index(s2) + len(s2):])
    result_search_for = (s1[s1.index(s2) + len(s2):])
    return result_search_for


def searching_in_searchBar(self, text_q, last_word):  ## Netflix search bar function
    # last_word = 'for'
    result_search = self.text_lenght_result(last_word, text_q)
    print(text_q)
    self.text_send_to_server(result_search_for='searching for ' + result_search)
    try:
        self.driver.find_element_by_class_name("searchTab").click()
    except:
        pass
    finally:
        print("search_i.. try except")
        self.search_bar_input = self.driver.find_element_by_name("searchInput")
        self.search_bar_input.clear()
        self.search_bar_input.send_keys(result_search)
        self.search_bar_input.send_keys(Keys.RETURN)
        time.sleep(3)


def find_elements_on_website(self, f_loop):  ##  find URL and Movie title on netflix website
    ii = None
    for ii in range(0, 5):
        ids = self.driver.find_elements_by_xpath("//a[@href]" and "//a[@aria-label]")[f_loop]

        movie_name = (ids.get_attribute("aria-label"))
        url_link = (ids.get_attribute("href"))
        data_entry(movie_name, url_link)
        print(ids.get_attribute("aria-label"))
        f_loop += 1


def create_driver_session(self, session_id, executor_url):  ## Selenium webdriver session to reuse opened webdriver

    # Save the original function, so we can revert our path
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute
    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id
    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute
    return new_driver


## function for finding show title and url when "add this to my playlist" in text_q.
def user_stored_for_local_database(self):
    time.sleep(3)
    app_mount = self.driver.find_element_by_id('appMountPoint')
    app_mount_str = (app_mount.text)
    self.movie_title = app_mount_str.partition('\n')[0]
    self.url_get = self.driver.current_url

