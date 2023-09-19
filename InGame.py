import pandas as pd
import requests
import time
import os
api=pd.read_csv('api.csv')
api_key=api.loc[0,'0']
request_header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}
tier=["IRON","BRONZE","SILVER","GOLD","PLATINUM","DIAMOND"]
division=["I","II","III","IV"]
for a in range(len(tier)):
    for b in range(len(division)):
        path='C:/Users/Myeong Geun/PycharmProjects/lolapi/Tier/'+tier[a]+'/'+division[b]
        GameIDFile=pd.read_csv(path+'/게임목록.csv')
        for i in range(len(GameIDFile)):
            GameID=GameIDFile.loc[i,'0']
            if not os.path.isdir(path+'/'+GameID):
                os.mkdir(path+'/'+GameID)
                request_url='https://asia.api.riotgames.com/lol/match/v5/matches/'+GameID
                r=requests.get(request_url,headers=request_header)
                while r.status_code==429:
                    time.sleep(120)
                    GameID=GameIDFile.loc[i,'0']
                    request_url='https://asia.api.riotgames.com/lol/match/v5/matches/'+GameID
                    r=requests.get(request_url,headers=request_header)
                print(path+'/'+GameID+'/'+GameID+'.json')
                pd.DataFrame(r.json()).to_json(path+'/'+GameID+'/'+GameID+'.json',force_ascii=False)
                pd.DataFrame(r.json()).to_json('C:/Users/Myeong Geun/PycharmProjects/lolapi/Game/'+GameID+'.json',force_ascii=False)
                #pd.DataFrame(r.json()).to_csv(path+'/'+GameID+'.csv',index=False,encoding='cp949')
