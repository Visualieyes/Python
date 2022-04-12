from logging import exception
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def countSolana(text):
    return text.lower().count('solana')

def countSolidity(text):
    return text.lower().count('solidity')

def countEth(text):
    return text.lower().count('ethereum')

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("--incognito")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = "https://indeed.com"
what_query = "Blockchain Developer"
where_query = "Canada"

# wait = WebDriverWait(driver, 5)

# url = "{}/jobs?q={}&l={}".format(base_url, what_query, where_query)
driver.implicitly_wait(10)
driver.get(base_url)
driver.implicitly_wait(10)

search_what = driver.find_element_by_css_selector("#text-input-what")
search_where = driver.find_element_by_css_selector("#text-input-where")
search_button = driver.find_element_by_css_selector(".yosegi-InlineWhatWhere-primaryButton")

search_what.send_keys(what_query)
search_where.clear()
# search_where.send_keys(where_query)

search_button.click() 

driver.implicitly_wait(10)

titles = []
companies = []
descriptions = []
while True:
    results_container = driver.find_element(By.ID, "mosaic-provider-jobcards")

    results = results_container.find_elements(By.CSS_SELECTOR, '.result')
    for result in results:
        try:
            result.click()
            frame = driver.find_element(By.ID, 'vjs-container-iframe')
            driver.switch_to.frame(frame)
            job_title = 'title'
            job_company = 'company'
            # job_title = driver.find_element(By.CLASS_NAME, "icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title is-embedded")
            # job_company = driver.find_element(By.CSS_SELECTOR, ".icl-u-lg-mr--sm.icl-u-xs-mr--xs")
            job_description = driver.find_element(By.ID, "jobDescriptionText")
            print(job_description.text)
            titles.append(job_title)
            companies.append(job_company)
            descriptions.append(job_description.text)
            driver.switch_to.default_content()
        except:
            print("error")
            titles.append(job_title)
            companies.append(job_company)
            descriptions.append("None")
    try:
        next_button = driver.find_element(By.XPATH, '//*[@id="resultsCol"]/nav/div/ul/li[6]/a')
        next_button.click()
        try:
            popup = driver.find_element(By.ID, 'popover-x')
            close_popup = popup.find_element(By.TAG_NAME, 'button')
            close_popup.click()
        except:
            print('no popup')
    except:
        print("error finding next button")
        break
    


data = {
    'titles': titles,
    'companies': companies,
    'descriptions': descriptions
    }

df = pd.DataFrame(data)

df['solana'] = df['descriptions'].apply(countSolana)
df['solidity'] = df['descriptions'].apply(countSolidity)
df['ethereum'] = df['descriptions'].apply(countEth)

totalSol = df['solana'].sum()
totalSoli = df['solidity'].sum()
totalEth = df['ethereum'].sum()

print("Total count:")
print("Solana: {}".format(totalSol))
print("Ethereum: {}".format(totalEth))
print("Solidity: {}".format(totalSoli))

# for result in results:
#     print(result) 



# soup = BeautifulSoup(driver.page_source, 'html.parser')



driver.quit()