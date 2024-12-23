from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui


options = Options()
options.add_experimental_option("detach", True) 
options.add_argument("--no-sandbox")

options.add_argument(r"--user-data-dir=C:\Users\prati\AppData\Local\Google\Chrome for Testing\User Data")  # Replace with your Chrome user data directory
options.add_argument("--profile-directory=Default")


driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get(r"https://studio.youtube.com/channel/UCf-L6gB9z9PDJNygwH0-M1g/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")


#_______________________________________________________________________________________________________________________________________
create_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/div/ytcp-button/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]"))  # Replace with your actual XPath
)

create_button.click()

driver.implicitly_wait(3)

upload_videos_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/div/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[1]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string"))
)

upload_videos_button.click()

driver.implicitly_wait(5)




#_______________________________________________________________________________________________________________________________________
# clicks the select files button / discarded method 

# actions = ActionChains(driver)

# # Perform Shift + Tab 5 times
# for _ in range(4):
#     actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
#     # time.sleep(1)

# # Press Enter
# actions.send_keys(Keys.ENTER).perform()
#_______________________________________________________________________________________________________________________________________
# alternate method for uploading files 
# this method works and is out best method till now 

file_input = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
)

# file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')


file_input.send_keys(r"C:\Users\prati\OneDrive\Desktop\projects\yT_uploader\vids\video.mp4")

# time.sleep(10)
#_______________________________________________________________________________________________________________________________________
# write title and description 
actions = ActionChains(driver)

title ="domestic deer"
description = "first video"

for i in range(2):

    actions.send_keys(Keys.TAB).perform()
    time.sleep(2)

actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

for char in title:
    actions.send_keys(char)
    # time.sleep(1)

actions.perform()  

actions.send_keys(Keys.TAB).send_keys(Keys.TAB).perform()

for char in description:
    actions.send_keys(char).perform()
    # time.sleep(1)

#_______________________________________________________________________________________________________________________________________
# to press not for children field
# actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform() // for pushing shift+tab


for _ in range(10):
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.2) 

# Press the Down Arrow key slowly
actions.send_keys(Keys.ARROW_DOWN).perform()


time.sleep(5)    
#_______________________________________________________________________________________________________________________________________

# pressing next button 
next_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]'))
)
next_button.click()
time.sleep(0.2)
next_button.click()
time.sleep(0.2)
next_button.click()

#_______________________________________________________________________________________________________________________________________
# for publishing the video 
for _ in range(9):
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.2)

time.sleep(3)

actions.send_keys(Keys.ARROW_DOWN).perform()

actions.send_keys(Keys.ARROW_DOWN).perform()

#_______________________________________________________________________________________________________________________________________
# clicking the publish button 
# /html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]
publish_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]'))
)

publish_button.click()

#_______________________________________________________________________________________________________________________________________

# select_files_button = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#select-files-button > ytcp-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill"))
# )

# select_files_button.click()

#_______________________________________________________________________________________________________________________________________
# upload_videos button on the orignal website page
# /html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item
#_______________________________________________________________________________________________________________________________________
# create button on channel content page
# document.querySelector("#button > yt-icon > span > div")
# #button > yt-icon > span > div
# /html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon/span/div

#_______________________________________________________________________________________________________________________________________
# select files button
# /html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]
# #select-files-button > ytcp-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill
# //*[@id="select-files-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]

#_______________________________________________________________________________________________________________________________________
# upload videos button on channel content page
# #text-item-0 > ytcp-ve > tp-yt-paper-item-body > div > div > div > yt-formatted-string
# //*[@id="text-item-0"]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string
# /html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/div/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[1]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string

#_______________________________________________________________________________________________________________________________________
# visibility button
# #step-badge-3
# document.querySelector("#step-badge-3")
# //*[@id="step-badge-3"]
# /html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/ytcp-animatable/ytcp-stepper/div/div[4]/ytcp-ve/button

#______________________________________________________________________________________________________________________________________

# next button
# #next-button > ytcp-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill
# //*[@id="next-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]
# /html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]

#_______________________________________________________________________________________________________________________________________

# publish button 
# #done-button > ytcp-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill
# //*[@id="done-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]
# /html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]

#_______________________________________________________________________________________________________________________________________
# public visibility button 
# #offRadio
# //*[@id="offRadio"]
# /html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[2]

# use full xpath
#_______________________________________________________________________________________________________________________________________

# tab*9 for title (it is there by default)
# tab*2 for description
# tab*2 for thumbnail
# tab*8 for chossing for children or not
# down*1 for no
# tab*10 for next
# do next thrice == enter*3
# shift+tab*2
# down*3 for public
# tab*14 for publish
# enter for publish

#_______________________________________________________________________________________________________________________________________

# shift+tab*19 for create button
# tab and then enter for upload videos 
# tab*3 and then enter for choosing files

#_______________________________________________________________________________________________________________________________________