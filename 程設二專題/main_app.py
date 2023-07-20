from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request,redirect,url_for
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?'\
'driver=ODBC+Driver+17+for+SQL+Server&'\
'trusted_connection=yes&'\
'server=LAPTOP-3Q90POBO&'\
'database=testdb1'

from movies_data import MovieInfo,Top250Movie,db
db.init_app(app)

#首頁
@app.route('/')
def index():
    return render_template('index.html',**locals())


#電影分類前50
@app.route('/genre',methods = ['POST'])
def genre():
    genre_name = request.values['genre']
    genre_datas = MovieInfo.query.filter_by(genre = genre_name)
    return render_template('show_genre.html',**locals())

#不分類前250電影
@app.route('/top_250_list',defaults = {'num':1})
@app.route('/top_250_list/<int:num>')
def top_250_list(num):
    datas250 = Top250Movie.query.order_by(Top250Movie.id).paginate(per_page = 50,page = num)
    return render_template('250_TopMovie.html',**locals())



#查詢電影
@app.route('/specific_movie',methods = ['POST'])
def specific_movie():
    movie_name = request.values['movieName']
    movie_data = MovieInfo.query.filter_by(title = movie_name).first()
    return render_template('specific_movie.html',**locals())


from market_share import genres,all_data
@app.route('/market_share')
def market_share():
    genre_datas = genres
    all_datas = all_data
    return render_template('market_share.html',**locals())


#回到首頁功能
@app.route('/back_to_index',methods = ['GET'])
def back_to_index():
    return redirect(url_for('index'))


if __name__ == '__main__': 
    app.run()