import pandas as pd
import requests
import time
import json
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
        puuid=pd.read_csv(path+'/데이터.csv')
        try:
            GameArray=pd.read_csv(path+'/게임목록.csv')
        except:
            GameArray=pd.DataFrame(index=range(0,0),columns=['0'])
        for i in range(len(puuid)):
            try:
                CallGameId='https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid.loc[i,'0']+'/ids?queue=420&start=0&count=20'
                r=requests.get(CallGameId,headers=request_header)
                while r.status_code == 429:
                    time.sleep(5)
                    CallGameId = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid.loc[i, '0'] + '/ids?queue=420&start=0&count=20'
                    r=requests.get(CallGameId,headers=request_header)
                print(r.json())
                for j in r.json():
                    print(j)
                    if not (GameArray['0']==j).any():
                        GameArray.loc[len(GameArray)] = [j]
            except:
                pass
        print(path+'\n'+GameArray)
        pd.DataFrame(GameArray).to_csv(path+'/게임목록.csv',index=False,encoding='cp949')