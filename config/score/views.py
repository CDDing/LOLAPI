from django.shortcuts import render
import requests
import os
import pandas as pd
from datetime import datetime
# Create your views here.

'''api=pd.read_csv('api.csv')
api_key=api.loc[0,'0']
request_header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}'''

def score_view(request):
    tier=["IRON","BRONZE","SILVER","GOLD","PLATINUM","DIAMOND"]
    division=["I","II","III","IV"]
    GameFile = {}
    for a in range(len(tier)):
        GameTierFile={}
        for b in range(len(division)):
            path = 'C:/Users/Myeong Geun/PycharmProjects/lolapi/Tier/' + tier[a] + '/' + division[b]
            GameIDFile = pd.read_csv(path + '/게임목록.csv')
            GameTierFile[division[b]]=GameIDFile['0']
        GameFile[tier[a]]=GameTierFile

    return render(request, 'score/score_view.html',{'GameFile':GameFile})

def search_result(request):
    if(request.method=="GET"):
        GameID = request.GET.get('search_text')
        os.chdir("C:/Users/Myeong Geun/PycharmProjects/lolapi")
        Game=pd.read_json('C:/Users/Myeong Geun/PycharmProjects/lolapi/Game/'+GameID+".json")
        Rune=pd.read_json('C:/Users/Myeong Geun/PycharmProjects/lolapi/config/static/dragontail-12.1.1/12.1.1/data/ko_KR/runesReforged.json')
        RuneDirectory=pd.read_json('C:/Users/Myeong Geun/PycharmProjects/lolapi/config/static/RuneDirectory.json')
        GameDate=datetime.fromtimestamp(Game['info']['gameStartTimestamp']/1000)

    return render(request, 'score/score_result.html',{'GameID':GameID,'Game':Game,'Rune':Rune,'RuneDirectory':RuneDirectory,'GameDate':GameDate})

def summoner_search(request):
    if(request.method=="GET"):
        summonerName=request.GET.get('search_text')
        summoner_exist=False
        get_summonerURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str(summonerName)    #소환사 정보 검색
        r = requests.get(get_summonerURL, headers=request_header)
        if(r.status_code==requests.codes.ok):
            summoner_exist=True
            summoner=r.json()


    return render(request, 'score/summoner_search.html',{'summoner_exist':summoner_exist})

def summoner_result(request):
    return render(request, 'score/summoner_result.html')

def stat_choose(request):
    path='C:/Users/Myeong Geun/PycharmProjects/lolapi/config/static/dragontail-12.1.1/12.1.1/data/ko_KR'
    ChampionFile=pd.read_json(path+'/champion.json')
    ChampionNameList=[i for i in ChampionFile['data'].index]
    return render(request, 'score/stat_choose.html',{'ChampionNameList':ChampionNameList,'ChampionFile':ChampionFile})

def stat_result(request):
    path = 'C:/Users/Myeong Geun/PycharmProjects/lolapi/'
    ChampionStat=pd.read_json(path+'통계.json')
    if(request.method=="GET"):
        championName=request.GET.get('champion_name')
    return render(request, 'score/stat_result.html',{'championName':championName,'ChampionStat':ChampionStat[championName],'GameCount':ChampionStat['GameCnt']})