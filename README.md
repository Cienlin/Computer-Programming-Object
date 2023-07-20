# Computer-Programming-Object
此為程式設計2期末專題，由409170452林慈恩和409180419宋承碩共同作業，並無任何商業用途。

主要程式是利用爬蟲爬取imdb電影評論網站('https://www.imdb.com/?ref_=nv_home') 的Top 250 Movies，以及透過電影分類篩選出來的排名前50部電影。

目前只抓取電影名稱，上映年份，評分，片長，電影介紹，導演及主要卡司，和分類名稱。

次要是爬取the Numbers的market charts('https://www.the-numbers.com/market/genres') ，並以電影分類來抓取1995至2023的market shar(市佔率)資料。

再利用python Flask及SQLalchemy創建網頁及連接SQLServer資料庫，將抓取的資料存取或做成表格及圖表再呈現至網頁上，再利用css美化網頁。

注意!.html文件須放在templates資料夾中，.css,.js,圖片均須放至static資料夾中

首頁
![螢幕擷取畫面 (24)](https://github.com/Cienlin/Computer-Programming-object/assets/102715193/372fbad5-106a-4c9d-b7f9-b51f3a437ce6)

分類查詢結果
![螢幕擷取畫面 (25)](https://github.com/Cienlin/Computer-Programming-object/assets/102715193/c58f33e4-2ad6-4f3c-918f-9e10562628f4)

指定電影查詢結果
![螢幕擷取畫面 (26)](https://github.com/Cienlin/Computer-Programming-object/assets/102715193/c04c3675-e768-4d0e-8b23-e220fc6b2786)

Top 250結果，並以50筆資料顯示分頁
![螢幕擷取畫面 (29)](https://github.com/Cienlin/Computer-Programming-object/assets/102715193/4ec94dcc-c694-48e1-9a5a-73e4ee21bc61)
![螢幕擷取畫面 (30)](https://github.com/Cienlin/Computer-Programming-object/assets/102715193/05e49b8e-5bf5-45c4-b3a9-df0363a5474f)

the Numbers表格及繪圖
![螢幕擷取畫面 (27)](https://github.com/Cienlin/Computer-Programming-object/assets/102715193/cad7dfb2-6689-4925-9c65-2f4dc5b22b44)
![螢幕擷取畫面 (28)](https://github.com/Cienlin/Computer-Programming-object/assets/102715193/476901fc-bc12-4af0-b419-65795e605d66)
