from flask import Flask, render_template, request
import requests
import random
from bs4 import BeautifulSoup
import csv
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')
    
@app.route("/welcome")
def welcome():
    return "my pleasure"
    
@app.route("/html_tag")
def html_tag():
    return "<h1>HEY BUDDY, I'VE BEEN WAITING YOU FOR A LONG TIME </h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1> multiple line</h1>
    <u1><li>1번</li>
    <li>2번</li></ul>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("file.html")
    
@app.route("/hello_name/<string:name>")
def hello_name(name):
    return render_template("hello.html", people_name = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    result = num**3
    return render_template("cube.html", num=num, cube_num=result)
    
@app.route("/lunch")
def lunch():
    list =['20층', '김카', '진가와']
    dict = {'20층':'http://newsplus.chosun.com/site/data/img_dir/2010/04/12/2010041201333_0.jpg',
    '김카': 'https://igx.4sqi.net/img/general/600x600/25224626_w2nCYA2f3tJthJ0Sbcz9fpke3yLetCy6kr-O9-AXkco.jpg',
    '진가와' : 'https://t1.daumcdn.net/cfile/tistory/990AC73D5B5DD50E06'}
    
    chosen =random.choice(list)
    pick = dict[chosen]
    return render_template("lunch.html", chosen=pick)
    
@app.route('/lotto')
def lotto():
    lottonumber = random.sample(range(46),6)
    return render_template('lotto.html', lottonumber = lottonumber)
    
@app.route('/naver')
def naver():
    return render_template('naver.html')
    
    
@app.route('/google')
def google():
    return render_template('google.html')
    
@app.route('/hello')
def halo():
    return render_template('halo.html')
    
@app.route("/hi")
def hi():
    user_name = request.args.get('name')
    return render_template('hi.html', user_name=user_name)
    
@app.route('/hair_match')
def hair():
    return render_template('hair.html')
    
@app.route('/star')
def star():
    starname = request.args.get('starname')
    return render_template('star.html',starname=starname)
  
@app.route('/summoner')
def summoner():
    return render_template('summoner.html')
    
@app.route('/opgg')
def opgg():
    summon=request.args.get('summoner')
    url='http://www.op.gg/summoner/userName='+summon
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    win = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    lose = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    
    if len(win) == 0:
        win_i = "0승"
    else :
        win_i = win[0].text
    
    if len(lose)==0:
        lose_i='0패'
    else:
        lose_i = lose[0].text
        
        
    # f = open("list.txt",'a+')
    # data = '소환사의 이름은 {} {} {} 입니다.'.format(summon, win_i, lose_i)
    # f.write(data)
    # f.close()
    
    f = open('list.csv','a+', encoding='utf-8', newline='')
    csvfile = csv.writer(f)
    data=[summon, win_i, lose_i, datetime.datetime.now()]
    csvfile.writerow(data)
    f.close()
    
    return render_template('opgg.html', win=win_i, lose=lose_i,summon=summon)
    
@app.route('/log')
def log():
    f = open('list.csv','r', encoding='utf-8')
    logs = csv.reader(f)
    
    return render_template('log.html', logs=logs)
    