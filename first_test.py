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

#______________________________________________________________________________________________________________________________________
#C:\Users\prati\AppData\Local\Google\Chrome for Testing\User Data
# options.add_argument(r"C:\Users\prati\AppData\Local\Google\Chrome for Testing\User Data")  # Path to your Chrome data
# options.add_argument("--profile-directory=Default")
#_______________________________________________________________________________________________________________________________________



# Step 1: Set up WebDriver
driver = webdriver.Chrome(options=options)  # Replace with webdriver.Firefox() or webdriver.Edge() as needed

driver.maximize_window()
# Step 2: Open a website
driver.get(r"https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=en&ifkv=AcMMx-cQvlH_Y6UUiVgtXs1Z_iS0aTfpzHIsS0T_zO9fhMc1sf3uM0xazrjibwzaROhab-ho06n4&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1993052362%3A1733489554065220&ddm=1")

# driver.get(r"https://www.youtube.com/")

time.sleep(5)

email = "greatminds2k24@gmail.com"
password = "GreatMinds@224"

pyautogui.typewrite(email)
pyautogui.press('enter')

time.sleep(2)

pyautogui.typewrite(password)
pyautogui.press('enter') 

# Step 3: Interact with the page (e.g., search for something)
# search_box = driver.find_element(By.NAME, "q")  # Find the search box
# search_box.send_keys("Selenium Python")        # Type a query
# search_box.send_keys(Keys.RETURN)             # Simulate pressing Enter

# Step 4: Wait and close
time.sleep(500)  # Wait to see results

