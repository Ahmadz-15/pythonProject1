from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import dicts


def search_for_substring(substrings_list, text):
    for i in substrings_list:
        if i in text:
            print('the substring {} found'.format(i))
        else:
            print('the substring {} not found'.format(i))


wallashops_url = 'https://www.wallashops.co.il/'
driver = webdriver.Chrome('./chromedriver')
driver.get(wallashops_url)

xp = dicts.Xpaths

# tap on cancel button on popup
driver.find_element(By.XPATH, xp['cancel_button']).click()

# tap on search
driver.find_element(By.XPATH, xp['search_banner']).send_keys('camera\n')

# find the search results
res = driver.find_element(By.XPATH, xp['search_res'])
search_list = ['camera', 'מצלמה']
search_for_substring(search_list, res.text)

# add product to basket
driver.find_element(By.XPATH, xp['add_to_basket']).click()
time.sleep(2)
# click on continue shopping
driver.find_element(By.XPATH, xp['continue_shopping']).click()

# back to main page
driver.find_element(By.XPATH, xp['main_page']).click()

# click on shopping basket
driver.find_element(By.XPATH, xp['shopping_basket']).click()

# check that basket is not empty and print total price
total_price = driver.find_element(By.XPATH, xp['total_price'])
print('Total Price={}'.format(total_price.text))

driver.quit()
