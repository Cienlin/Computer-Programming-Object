# Computer-Programming-Object
此為程式設計2期末專題，由409170452林慈恩和409180419宋承碩共同作業，並無任何商業用途。

主要程式是利用爬蟲爬取imdb電影評論網站('https://www.imdb.com/?ref_=nv_home') 的Top 250 Movies，以及透過電影分類篩選出來的排名前50部電影。

目前只抓取電影名稱，上映年份，評分，片長，電影介紹，導演及主要卡司，和分類名稱。

次要是爬取the Numbers的market charts('https://www.the-numbers.com/market/genres') ，並以電影分類來抓取1995至2023的market shar(市佔率)資料。

再利用python Flask及SQLalchemy創建網頁及連接SQLServer資料庫，將抓取的資料存取或做成表格及圖表再呈現至網頁上，再利用css美化網頁。

注意!.html文件須放在templates資料夾中，.css,.js,圖片均須放至static資料夾中

首頁
![螢幕擷取畫面 (24)](https://github.com/Cienlin/Computer-Programming-Object/assets/102715193/b953b12e-50bf-413a-bd55-b0aa80076414)

分類查詢結果
![螢幕擷取畫面 (25)](https://github.com/Cienlin/Computer-Programming-Object/assets/102715193/6da0f003-18dc-4258-9823-03069278653a)

指定電影查詢結果
![螢幕擷取畫面 (26)](https://github.com/Cienlin/Computer-Programming-Object/assets/102715193/fd0a5be3-fd15-463c-8327-8c772c56ef1e)

Top 250結果，並以50筆資料顯示分頁
![螢幕擷取畫面 (29)](https://github.com/Cienlin/Computer-Programming-Object/assets/102715193/3304fdbf-9054-432e-8d56-a5717c964b6a)
![螢幕擷取畫面 (30)](https://github.com/Cienlin/Computer-Programming-Object/assets/102715193/79144d65-19dd-4796-aa60-1ee8391d173f)

the Numbers表格及繪圖
![螢幕擷取畫面 (27)](https://github.com/Cienlin/Computer-Programming-Object/assets/102715193/8464685c-6c06-46f6-ab35-f15e6c40cab4)
![螢幕擷取畫面 (28)](https://github.com/Cienlin/Computer-Programming-Object/assets/102715193/cb8519d0-a4af-4c10-bf54-586cc9062441)


