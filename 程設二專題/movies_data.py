from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?'\
'driver=ODBC+Driver+17+for+SQL+Server&'\
'trusted_connection=yes&'\
'server=LAPTOP-3Q90POBO&'\
'database=testdb1'
db = SQLAlchemy(app)


class MovieInfo(db.Model):
    __tablename__ = 'MovieInfo'
    id = db.Column(db.Integer,nullable = False,primary_key=True)
    genre = db.Column(db.String(50),nullable = False)
    title = db.Column(db.String(50),nullable = False)
    years = db.Column(db.String(50),nullable = False)
    runtime = db.Column(db.String(50),nullable = False)
    rate = db.Column(db.Float,nullable = False)
    intro = db.Column(db.String(500),nullable = False)
    stars = db.Column(db.String(500),nullable = False)
    #photo = db.Column(db.String(20),nullable = False,server_default = 'def.jpg')


    def __init__(self, genre, title, years, runtime, rate, intro, stars):
       self.genre = genre
       self.title = title
       self.years = years
       self.runtime = runtime
       self.rate = rate
       self.intro = intro
       self.stars = stars

class Top250Movie(db.Model):
    __tablename__ = 'Top250Movie'
    id = db.Column(db.Integer,nullable = False,primary_key=True)
    movie = db.Column(db.String(50),nullable = False)
    year = db.Column(db.String(50),nullable = False)
    runtime = db.Column(db.String(50),nullable = False)
    rate = db.Column(db.Float,nullable = False)
    intro = db.Column(db.String(500),nullable = False)
    director = db.Column(db.String(500),nullable = False)
    stars = db.Column(db.String(500),nullable = False)

    def __init__(self,movie,year,runtime,rate,intro,director,stars):
        self.movie = movie
        self.year = year
        self.runtime = runtime
        self.rate = rate
        self.intro = intro
        self.director = director
        self.stars = stars

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pandas as pd


#開始抓資料
start_time = time.time()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.imdb.com/')
driver.maximize_window()
time.sleep(1)


#點選top250選單
menu = driver.find_element(By.ID, 'imdbHeader-navDrawerOpen').click()
time.sleep(0.5)
top_movies = driver.find_element(By.XPATH,'//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[2]').click()
time.sleep(0.5)


#列出資料庫內評級最高的250部電影，入選規範必須是曾公開上映的非紀錄片，片長至少45分鐘，評分達兩萬五千人次以上，並且只有定期投票習慣的使用者才會採用計票
def imdb_top250_movies():
    data250 = pd.DataFrame([],columns=['Movie','Year','Runtime', 'Rate', 'Intro' ,'Director', 'Stars'])
    for i in range(175, 181):
        movie = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[1]/a')
        driver.execute_script("arguments[0].scrollIntoView();", movie)
        movie.click()
        title = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span')
        year = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[1]/a')
        try:
            runtime = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[3]')
        except NoSuchElementException:
            runtime = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[2]')
        rate = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]')
        intro = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/p')
        director = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[1]/div/ul/li/a')
        stars = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[3]/div')
        new_data = pd.DataFrame([[title.text, year.text.replace('(','').replace(')',''), runtime.text, rate.text, intro.text, director.text, stars.text]],
                                columns=['Movie','Year', 'Runtime' , 'Rate', 'Intro','Director', 'Stars'])
        data250 = pd.concat([data250,new_data])
        time.sleep(0.5)
        driver.back()
    return data250 

#Top Rated Movies by Genre
genres = {}
def get_genre_link():
    for i in range(1,24):
        genre = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/section/div[6]/div[2]/div[2]/a['+str(i)+']')
        genre_name = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/section/div[6]/div[2]/div[2]/a['+str(i)+']/span')
        genre_link = genre.get_attribute('href')
        genres[genre_name.text] = genre_link 
    return genres 


#在每個分類類別裡抓top50電影資訊
def get_top50_movieInfo(genres):
    movie_db = pd.DataFrame([],columns=['genre','title','years','runtime','rate','intro','stars'])

    for genre in genres:
        html = requests.get(genres.get(genre,0))
        soup = BeautifulSoup(html.text,'lxml')
        movies = soup.find_all('div',class_ = 'lister-item mode-advanced')
        
        for movie in movies:
            info = movie.find('div',class_ = 'lister-item-content')
            title = info.h3.a
            years = info.h3.find('span',class_ = 'lister-item-year text-muted unbold')
            runtime = info.find('p',class_ = 'text-muted').find('span',class_ = 'runtime')
            rate = info.find('div',class_ = 'ratings-bar').find('div',class_ = 'inline-block ratings-imdb-rating').strong
            intro = info.find('div',class_ = 'ratings-bar').find_next_sibling('p')
            stars = intro.find_next_sibling('p').find_all('a')

            star_list = ', '.join(star.text for star in stars)
            new_movie_db = pd.DataFrame([[genre, title.text, years.text.replace('(','').replace(')',''), runtime.text, rate.text, intro.text, star_list]],
                                        columns=['genre','title','years','runtime','rate','intro','stars'])  
            movie_db = pd.concat([movie_db,new_movie_db])
            
    return movie_db
'''
            抓圖片
            #save each photo into a file
            folder_path = "C:\\Users\\User\\Desktop\\程設二專題\\電影圖片\\"+genre
            photo_url = movie.find('div',class_ = 'lister-item-image float-left').a.img.get('src')

            img_response = requests.get(photo_url)
            #如果檢查沒資料夾，就建立一個
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            if img_response.status_code == 200:
            # 设置保存图片的路径和文件名
                save_path = folder_path+'\\'+title.text.replace('/',' ')+'.png'

                # 保存图片到本地文件
                with open(save_path, 'wb') as file:
                    file.write(img_response.content)
                print(title.text+" 保存成功！")
            else:
                print("無法獲取圖片。")
'''    
data250 = imdb_top250_movies()
get_genre_link()
movie_db = get_top50_movieInfo(genres)

datas250 = []
for index,row in data250.iterrows():
    movie = row['Movie']
    year = row['Year']
    runtime = row['Runtime']
    rate = row['Rate']
    intro = row['Intro']
    director = row['Director']
    stars = row['Stars']

    data = Top250Movie(
        movie=movie,
        year=year,
        runtime=runtime,
        rate=rate,
        intro=intro,
        director=director,
        stars=stars)
    datas250.append(data)


datas = []
for index, row in movie_db.iterrows():
    genre = row['genre']
    title = row['title']
    years = row['years']
    runtime = row['runtime']
    rate = row['rate']
    intro = row['intro']
    stars = row['stars']
    
    data = MovieInfo(
        genre=genre,
        title=title,
        years=years,
        runtime=runtime,
        rate=rate,
        intro=intro,
        stars=stars)

    datas.append(data)
    
with app.app_context():
    db.drop_all()   #如果資料表已存在就刪除
    db.create_all()
    db.session.add_all(datas)
    db.session.add_all(datas250)
    db.session.commit()


time.sleep(1)
end_time = time.time()
print('資料抓取成功!')
execution_time = end_time - start_time
print(f"程式執行時間：{execution_time} 秒")
driver.close()