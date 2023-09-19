import requests
import pandas as pd
import time
api=pd.read_csv('api.csv')
api_key=api.loc[0,'0']
request_header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}
#summoner_name="hide on bush"

#sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +summoner_name+'?api_key=' + api_key
#r = requests.get(sohwan)
#r.json()['id'] #소환사의 고유 id
#print(r.json()['name'])

tier=["IRON","BRONZE","SILVER","GOLD","PLATINUM","DIAMOND"]
division=["I","II","III","IV"]
for a in range(len(tier)):
    for b in range(len(division)):
        path='C:/Users/Myeong Geun/PycharmProjects/lolapi/Tier/'+tier[a]+'/'+division[b]
        queue = "https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/"+tier[a]+"/"+division[b]+"?page=2"
        req=requests.get(queue,headers=request_header)
        league_df=pd.DataFrame(req.json())
        accountList=pd.read_csv(path+'/데이터.csv')
        print(tier[a]+division[b]+"인원 수 :"+str(len(accountList)),end='')
        for i in range(len(league_df)):
            try:
                sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[i] + '?api_key=' + api_key
                r = requests.get(sohwan)
                while r.status_code == 429:
                    time.sleep(120)
                    sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[i] + '?api_key=' + api_key
                    r = requests.get(sohwan)

                account_id = r.json()['puuid']
                if not (accountList['0']==account_id).any():
                    accountList.loc[len(accountList)]=account_id
            except:
                pass
        print("->"+str(len(accountList)))
        accountList.to_csv(path+'/데이터.csv',index=False,encoding='cp949')
'''
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
        pd.DataFrame(GameArray).to_csv(path+'/게임목록.csv',index=False,encoding='cp949')'''