from selenium import webdriver
from inputs import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import re


wordcloud_mode = 'wordcloud'
questions_mode = 'questions'

# wordcloud elements
wc_input_text_box_xpath = '//*[contains(@id, "mui-")]'
wc_send_button_xpath = '//*[@id="poll-submit-button"]'



def get_slido_event_id(url):
    match = re.search(r"app.sli.do/event/(.*?)/", url)
    if match:
        event_id = match.group(1)
        return event_id


slido_event_id = None
driver = None

def validate_inputs():
    global slido_event_id, driver
    
    if 'app.sli.do/event/' not in slido_base_url:
        print('Invalid slido base url')
        return False

    if mode not in [wordcloud_mode, questions_mode]:
        print('Invalid slido base url')
        return False
    try:
        slido_event_id = get_slido_event_id(slido_base_url)
    except Exception as e:
        print(f'Error geting event id from slido url. Check slido url. Error {e}')
        return False
    print(f'Slido event id: {slido_event_id}, mode: {mode}')
    try:
        driver = webdriver.Chrome(chrome_driver_path)
    except Exception as e:
        print(f'Error loading chrome driver. Check driver path. Error {e}')
        return False
    return True

def vote_questions():
    driver.get(f"https://app.sli.do/event/{slido_event_id}/live/questions")
    vote_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, vote_button_xpath)))
    vote_button = driver.find_element_by_xpath(vote_button_xpath)
    vote_button.click()
    driver.delete_all_cookies()
    print('Voted')


def vote_wordcloud():
    driver.get(f"https://app.sli.do/event/{slido_event_id}/live/polls")
    # time.sleep(5)

    input_text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, wc_input_text_box_xpath)))

    input_text_box = driver.find_element_by_xpath(wc_input_text_box_xpath)
    input_text_box.clear()
    input_text_box.send_keys(input_text)

    send_button = driver.find_element_by_xpath(wc_send_button_xpath)

    send_button.click()
    driver.delete_all_cookies()
    print('Word cloud submited')
 

def main():
    try:
        if not validate_inputs():
            print('Invalid inputs. Exiting...')
            return
        print('Validated Inputs')
        for __ in range(repeats):
            if mode == questions_mode:
                vote_questions()
            elif mode == wordcloud_mode:
                vote_wordcloud()
    except Exception as e:
        print(f'Error runing bot. {e}')
    finally:
        if driver:
            driver.close()
    
if __name__ == "__main__":
    main()