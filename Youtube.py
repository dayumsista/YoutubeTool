from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

Title = 'Aalto Talk with Linus Torvalds'

# Initialize the webdriver
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com/")

# Wait for the search box to load
search_box = driver.find_element(By.CSS_SELECTOR, "input#search")
time.sleep(random.uniform(6.969, 7.147))

# Input the search term
for char in Title:
    search_box.send_keys(char)
    time.sleep(0.1) 
time.sleep(random.uniform(2.236, 3.514))

# Click the search button
search_button = driver.find_element(By.CSS_SELECTOR, "button#search-icon-legacy")
search_button.click()

# Wait for the search results to load
time.sleep(random.uniform(5.141, 6.987))

# Scroll the page
driver.execute_script("window.scrollTo(0, 3214)")

# Find and click on the specific video
element = driver.find_element(By.CSS_SELECTOR, "[title='Aalto Talk with Linus Torvalds [Full-length]']")
driver.execute_script("arguments[0].click();", element)

# Wait for the video to load and potentially skip ads
time.sleep(random.uniform(33.45, 61.74))
try:
    skip_button = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
    if skip_button:
        skip_button.click()
except:
    pass

time.sleep(random.uniform(91.25, 101.21))

# Like the video
like_button = driver.find_element(By.CSS_SELECTOR, "#top-row #top-level-buttons-computed like-button-view-model")
like_button.click()

# Scroll a little
driver.execute_script("window.scrollTo(0, 312)")

# Wait for the comment box to load
time.sleep(30)

# Comment on the video
comment_box = driver.find_element(By.CSS_SELECTOR, "[role='textbox']")
comment_box.send_keys("Nice GG!")
time.sleep(random.uniform(1.545, 2.541))

# Submit the comment
submit_button = driver.find_element(By.CSS_SELECTOR, "#buttons #submit-button")
submit_button.click()

# Wait for a bit
time.sleep(random.uniform(3.458, 5.478))

# Close the browser
driver.quit()
