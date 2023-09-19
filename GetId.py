import requests
import pandas as pd
import time
api=pd.read_csv('api.csv')
api_key=api.loc[0,'0']
print(api_key)


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
        queue = "https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/"+tier[a]+"/"+division[b]+""+'?api_key=' + api_key
        req=requests.get(queue)
        league_df=pd.DataFrame(req.json())
        account=[]
        for i in range(len(league_df)):
            try:
                sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[i] + '?api_key=' + api_key
                r = requests.get(sohwan)
                while r.status_code == 429:
                    time.sleep(5)
                    sohwan = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + league_df['summonerName'].iloc[i] + '?api_key=' + api_key
                    r = requests.get(sohwan)
                print(r.json())
                account_id = r.json()['puuid']
                account.append(r.json()['puuid'])
            except:
                pass
        accountddpd=pd.DataFrame(account)
        print(path)
        #accountddpd.to_csv(path+'/데이터.csv',index=False,encoding='cp949')
