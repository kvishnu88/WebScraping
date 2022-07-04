from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import aspose.words as aw

URL = "https://testbook.com/ssc-cgl-exam/previous-year-papers"
driver = webdriver.Chrome(executable_path='C:/chromeDriver/chromedriver.exe')
driver.get(URL)
d = driver.find_element(By.XPATH,
                        '//*[@id="target-pyp"]/div[2]/year-wise-papers/div/div[1]/div[1]/test-card[5]/div/div[2]/div[1]')
d.click()
driver.implicitly_wait(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')

for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href[:5] == 'https':
        if len(href.split('=')) == 3:
            split_link = href.split('=')[2]
            print(split_link)
            if ('.pdf' in split_link):
                response = requests.get(split_link)
                pdf = open("pdf" + split_link[-12:-5] + ".pdf", 'wb')
                pdf.write(response.content)
                pdf.close()
                print("File ", " downloaded")
