from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.the-numbers.com/market/genres')
driver.maximize_window()
time.sleep(1)

genres = []
all_data = {}

for i in range(2, 9):
    genre_link = driver.find_element(By.XPATH, '//*[@id="page_filling_chart"]/center/table/tbody/tr[' + str(i) + ']/td[2]/b/a')
    genre_name = genre_link.text
    genres.append(genre_name)
    genre_link.click()

    # Year by Year Market Share
    year_datas = []
    market_share_datas = []
    for j in range(2, 31):
        year = driver.find_element(By.XPATH, '//*[@id="page_filling_chart"]/table[2]/tbody/tr[' + str(j) + ']/td[1]/a')
        market_share = driver.find_element(By.XPATH, '//*[@id="page_filling_chart"]/table[2]/tbody/tr[' + str(j) + ']/td[3]/a/b')
        year_datas.append(year.text)
        market_share_datas.append(market_share.text)
    all_data[genre_name] = dict(zip(year_datas, market_share_datas))

    driver.back()
    time.sleep(1)


import matplotlib.pyplot as plt
import numpy as np
#數據
years = sorted(list(all_data['Adventure'].keys()))
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'gray']

fig, ax = plt.subplots()

# 設定跳過年份間隔
year_interval = 5

x_ticks = np.arange(len(years))[::year_interval]
x_labels = [years[i] for i in x_ticks]

for genre, color in zip(all_data.keys(), colors):
    data = [float(all_data[genre][year].replace('%', '')) for year in years]
    ax.plot(years, data, label=genre, color=color)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax.set_xlabel('Year')
ax.set_ylabel('Market Share (%)')
ax.set_title('Genres Market Share')

ax.grid(True, linestyle='--', alpha=0.5)

plt.xticks(x_ticks, x_labels, rotation=45)
plt.tight_layout()
plt.savefig('C:\\Users\\User\Desktop\\程設二專題\\static\\photo\\market_share_img.png',dpi = 100,format = 'png')


time.sleep(2)
driver.close()