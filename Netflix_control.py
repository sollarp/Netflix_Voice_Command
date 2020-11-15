import urllib.request
import urllib.parse
from Support import vlc
from Support.Google_SpeechToText import main
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import os
from Support.sqlite_test import data_entry
from Support.helper_for_sqlite import readSingleRow
from Support.unoffical_netfix_database import netflix_api
from Utils.all_functions import FunctionSupport


class GoogleSearch:
    driver = None
    search_bar_input = None
    player = None
    chrome_options = None
    label = None
    keyboard = Controller()

    ## function for finding show title and url when "add this to my playlist" in text_q.
    def init_chrome_options(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (X11; CrOS armv7l 11895.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.125 Safari/537.36"
        )
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument("--user-data-dir=chrome-data")

    ## Selenium webdriver Chrome version you have to download.
    def init_driver(self):
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',
                                       options=self.chrome_options)
        pyautogui.press('f11')

    def secondary_voice(self, s_driver_bool):  ### Starting point
        functionsupport = FunctionSupport()
        self.init_chrome_options()
        x = s_driver_bool

        while True:
            text_q = main().lower()
            if text_q:
                functionsupport.text_onscreen(text_q)

            if 'netflix' in text_q:
                try:
                    self.player.stop()  # stops vlc player
                except:
                    pass
                finally:
                    url_link = 'https://www.netflix.com/SwitchProfile?tkn=J3LTSQQC2NDQHLYPD6UGZ76T'
                    if x:
                        self.driver.get(url_link)
                        functionsupport.find_elements_on_website(f_loop=5)
                        return True
                    else:
                        self.init_driver()
                        self.driver.get(url_link)
                        self.s_driver = functionsupport.create_driver_session(session_id=self.driver.session_id,
                                                                              executor_url=self.driver.command_executor._url)
                        functionsupport.find_elements_on_website(f_loop=5)
                        return True


            elif 'add this to my playlist' in text_q:
                movie_name = functionsupport.movie_title
                url_link = functionsupport.url_get
                data_entry(movie_name, url_link)
                return True

            elif 'want to watch' in text_q:
                try:
                    self.player.stop()  # close vlc player
                except:
                    pass
                finally:
                    last_word = 'watch'
                    result_search = functionsupport.text_lenght_result(last_word,
                                                                       text_q)  # getting string after 'watch' word
                    print("local database: " + result_search)
                    result_search = result_search.strip()  ### delete space after 'watch' word
                    local_database = readSingleRow(result_search)  # searching in sqlite database (local database)
                    print("sqlite database value= " + local_database)
                    if local_database == 'not_in_database':
                        return_sql_url = netflix_api(result_search)  # searching in Unogs Netflix API

                        print("vegso: " + return_sql_url)
                        if return_sql_url == '0':

                            url_link = 'https://www.netflix.com/SwitchProfile?tkn=J3LTSQQC2NDQHLYPD6UGZN76TI'
                            if x:
                                self.driver.get(url_link)
                                time.sleep(1)
                                functionsupport.searching_in_searchBar(text_q,
                                                                       last_word)  # searching in netflix website search bar
                                print("netflix searchbar")
                                return True
                            else:
                                self.init_driver()
                                self.driver.get(url_link)
                                ## store session in memory to reuse webdriver
                                self.s_driver = functionsupport.create_driver_session(session_id=self.driver.session_id,
                                                                                      executor_url=self.driver.command_executor._url)
                                time.sleep(1)
                                functionsupport.searching_in_searchBar(text_q, last_word)
                                print("netflix searchbar")
                                return True

                        else:
                            if x:
                                self.driver.get('https://www.netflix.com/watch/' + return_sql_url)
                                functionsupport.user_stored_for_local_database()  ## find show name and url to add to playlist
                                return True
                            else:
                                self.init_driver()
                                self.driver.get('https://www.netflix.com/watch/' + return_sql_url)
                                ## store session in memory to reuse webdriver
                                self.s_driver = functionsupport.create_driver_session(session_id=self.driver.session_id,
                                                                                      executor_url=self.driver.command_executor._url)
                                functionsupport.user_stored_for_local_database()  ## find show name and url to add to playlist
                                print("API database")
                                return True

                    else:
                        if x:
                            self.driver.get(local_database)
                            return True
                        else:
                            self.init_driver()
                            self.driver.get(local_database)
                            self.s_driver = functionsupport.create_driver_session(session_id=self.driver.session_id,
                                                                                  executor_url=self.driver.command_executor._url)
                            return True
            ## Search on  netflix search bar  with webbrowser
            elif 'search for' in text_q:
                url_link = 'https://www.netflix.com/SwitchProfile?tkn=J3LTSQQC2NDQHLYPD6UGZN76TI'
                if x:
                    self.driver.get(url_link)
                    time.sleep(1)
                    functionsupport.searching_in_searchBar(text_q, last_word='for')
                    print("netflix searchbar")
                    return True
                else:
                    self.init_driver()
                    self.driver.get(url_link)
                    self.s_driver = functionsupport.create_driver_session(session_id=self.driver.session_id,
                                                                          executor_url=self.driver.command_executor._url)
                    time.sleep(1)
                    functionsupport.searching_in_searchBar(text_q, last_word='for')
                    print("netflix searchbar")
                    return True

            elif 'go to sleep' in text_q:
                try:
                    functionsupport.terminate_all_process()
                    os.system('echo "standby 0" | cec-client -s -d 1')
                except:
                    os.system('echo "standby 0" | cec-client -s -d 1')
                finally:
                    break

            elif 'shut down' in text_q:
                try:
                    functionsupport.terminate_all_process()
                except:
                    pass
                break
            ### This is a configuration to my Toshiba TV to control
            elif 'quiet' in text_q or 'volume down' in text_q:
                os.system('sudo amixer cset numid=1 90%')
                break

            elif 'volume up' in text_q or 'louder' in text_q:
                os.system('sudo amixer cset numid=1 100%')
                break

            elif 'wake up' in text_q:
                os.system('echo "as 0" | cec-client -s -d 1')

                break

            elif 'tv off' in text_q:
                os.system('echo "standby 0" | cec-client -s -d 1')
                break
            ## page goes down, up, back
            elif 'go down' in text_q or 'scroll down' in text_q:
                try:
                    self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
                except:
                    pass
                return True

            elif 'go up' in text_q or 'scroll up' in text_q:
                try:
                    scroll_up = self.driver.find_element_by_tag_name('body')
                    scroll_up.send_keys(Keys.PAGE_UP)
                except:
                    pass
                return True

            elif 'go back' in text_q:
                try:
                    self.driver.back()
                except:
                    pass
                return True
            ## Close every VLC or Webdriver activity
            elif 'shut down' in text_q:
                try:
                    functionsupport.terminate_all_process()
                except:
                    pass
                break
                # go_back = self.driver.find_element_by_tag_name('body')
                # go_back.send_keys(Keys.TAB)
                # go_back.send_keys(Keys.ENTER)

            ## This works intermittenly as mouse pointer random
            elif 'pause' in text_q:
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                break


            ## select first show from search result on Netflix websearch.
            elif 'play first' in text_q:
                body = self.driver.find_element_by_tag_name('body')
                body.send_keys(Keys.ESCAPE)
                select_movie = '0'
                stored_path = '//*[@id="title-card-0-%s"]/div[1]/a' % select_movie
                time.sleep(1)
                test_select = self.driver.find_element_by_xpath(stored_path)
                test_select.click()
                time.sleep(1)
                # star_playing = self.driver.find_element_by_class_name('jaw-play-hitzone') --- changed website class
                star_playing = self.driver.find_element_by_class_name('previewModal--player-titleTreatmentWrapper')

                # star_playing = self.driver.find_element_by_class_name('button-primary large iconOnly ltr-ublg01')
                star_playing.click()
                # jaw-play-hitzone
                os.system('sudo amixer cset numid=1 100%')
                functionsupport.user_stored_for_local_database()
                return True

            elif 'play ii' in text_q:
                body = self.driver.find_element_by_tag_name('body')
                body.send_keys(Keys.ESCAPE)
                select_movie = '1'
                stored_path = '//*[@id="title-card-0-%s"]/div[1]/a' % select_movie
                time.sleep(1)
                test_select = self.driver.find_element_by_xpath(stored_path)
                test_select.click()
                time.sleep(1)
                star_playing = self.driver.find_element_by_class_name('previewModal--player-titleTreatmentWrapper')
                star_playing.click()
                os.system('sudo amixer cset numid=1 100%')
                functionsupport.user_stored_for_local_database()
                return True

            elif 'play third' in text_q:
                body = self.driver.find_element_by_tag_name('body')
                body.send_keys(Keys.ESCAPE)
                select_movie = '2'
                stored_path = '//*[@id="title-card-0-%s"]/div[1]/a' % select_movie
                time.sleep(1)
                test_select = self.driver.find_element_by_xpath(stored_path)
                test_select.click()
                time.sleep(1)
                star_playing = self.driver.find_element_by_class_name('previewModal--player-titleTreatmentWrapper')
                star_playing.click()
                functionsupport.user_stored_for_local_database()
                return True

            elif 'play 4' in text_q:
                body = self.driver.find_element_by_tag_name('body')
                body.send_keys(Keys.ESCAPE)
                select_movie = '1'
                stored_path = '//*[@id="title-card-0-%s"]/div[1]/a' % select_movie
                time.sleep(1)
                test_select = self.driver.find_element_by_xpath(stored_path)
                test_select.click()
                time.sleep(1)
                star_playing = self.driver.find_element_by_class_name('previewModal--player-titleTreatmentWrapper')
                star_playing.click()
                functionsupport.user_stored_for_local_database()
                return True

            elif 'grinch' in text_q:
                try:
                    functionsupport.terminate_all_process()
                    time.sleep(1)
                    functionsupport.calling_vlc()
                except:
                    functionsupport.calling_vlc('/home/pi/Videos/Grinch.mkv')
                    self.player.set_fullscreen(True)
                    self.player.play()
                    time.sleep(2)
                break

            ## This is no longer working as Youtube Dll not available
            elif 'youtube' in text_q:

                try:
                    functionsupport.terminate_all_process()

                except Exception:
                    pass

                finally:

                    query2 = main()
                    wr = functionsupport.website_request(query2)
                    print(wr)
                    url = ("http://www.youtube.com/watch?v=" + wr[0])
                    video = pafy.new(url)
                    best = video.getbest()
                    playurl = best.url
                    ins = vlc.Instance()
                    self.player = ins.media_player_new()
                    code = urllib.request.urlopen(url).getcode()
                    self.player.set_fullscreen(True)
                    print("search for: ")

                    media = ins.media_new(playurl)
                    media.get_mrl()
                    self.player.set_media(media)
                    self.player.play()

                break

            elif 'volume five' in text_q:
                self.player.audio_set_volume(50)
                break
            elif 'volume ten' in text_q:
                self.player.audio_set_volume(100)
                break
            else:
                if text_q is False or '' in text_q:
                    self.s_driver = functionsupport.create_driver_session(session_id=self.driver.session_id,
                                                                          executor_url=self.driver.command_executor._url)
                if self.s_driver:
                    return x == True
                else:
                    return x == False
