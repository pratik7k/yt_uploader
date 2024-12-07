from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui


options = Options()
options.add_experimental_option("detach", True) 
options.add_argument("--no-sandbox")



driver = webdriver.Chrome(options=options)

driver.maximize_window()


driver.get(r"https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=en&ifkv=AcMMx-cQvlH_Y6UUiVgtXs1Z_iS0aTfpzHIsS0T_zO9fhMc1sf3uM0xazrjibwzaROhab-ho06n4&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1993052362%3A1733489554065220&ddm=1")


time.sleep(5)

email = "greatminds2k24@gmail.com"
password = "GreatMinds@224"

pyautogui.typewrite(email)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite(password)
pyautogui.press('enter') 


time.sleep(5)


#_______________________________________________________________________________________________________________________________________
create_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon/span/div"))  # Replace with your actual XPath
)

create_button.click()

driver.implicitly_wait(3)

upload_videos_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item"))
)

upload_videos_button.click()

#_______________________________________________________________________________________________________________________________________
# upload_videos button on the orignal website page
# /html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item
#_______________________________________________________________________________________________________________________________________
# create button on channel content page
# document.querySelector("#button > yt-icon > span > div")
# #button > yt-icon > span > div
# /html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon/span/div
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
# tab*2 for thumnail
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