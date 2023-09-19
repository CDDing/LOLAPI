import pandas as pd

tier = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND"]
division = ["I", "II", "III", "IV"]
path = 'C:/Users/Myeong Geun/PycharmProjects/lolapi/config/static/dragontail-12.1.1/12.1.1/data/ko_KR'
ChampionFile=pd.read_json(path+'/champion.json')
ChampionNameList=[i for i in ChampionFile['data'].index]
Champion={}
for i in range(len(ChampionNameList)):
    Tier={}
    for j in range(len(tier)):
        Division={}
        for k in range(len(division)):
            Division[division[k]]={'PickCount':0,'WinCount':0}
            Division['Tier']=tier[j]
        Tier[tier[j]]=Division
    Champion[ChampionNameList[i]]=Tier
GameCnt={}
for i in range(len(ChampionNameList)):
    Tier={}
    for j in range(len(tier)):
        Division={}
        for k in range(len(division)):
            Division[division[k]]={'GameCount':0}
        Tier[tier[j]]=Division
    GameCnt=Tier
Champion['GameCnt']=GameCnt
for a in range(len(tier)):
    for b in range(len(division)):
        GameCount=0
        championPick=0
        championWin=0
        path = 'C:/Users/Myeong Geun/PycharmProjects/lolapi/Tier/' + tier[a] + '/' + division[b]
        GameIDFile = pd.read_csv(path + '/게임목록.csv')
        for i in range(len(GameIDFile)):
            GameID = GameIDFile.loc[i, '0']
            #print(Champion['Aatrox']['IRON']['I']['PickCount'])
            try:
                GameJson=pd.read_json(path+'/'+GameID+'/'+GameID+'.json')
                GameCount+=1
                for j in (GameJson['info']['participants']):
                    Champion[j['championName']][tier[a]][division[b]]['PickCount']+=1
                    print(tier[a]+division[b]+GameID+j['championName']+str(Champion[j['championName']][tier[a]][division[b]]['PickCount']))
                    if(j['win']==True):
                        Champion[j['championName']][tier[a]][division[b]]['WinCount']+=1
            except:
                print(tier[a]+division[b]+GameID+"오류")
                pass
        Champion['GameCnt'][tier[a]][division[b]]['GameCount']=GameCount
pd.DataFrame(Champion).to_json('통계.json')
print(Champion)