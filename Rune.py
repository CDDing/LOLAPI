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

Rune=pd.read_json('C:/Users/Myeong Geun/PycharmProjects/lolapi/config/static/dragontail-12.1.1/12.1.1/data/ko_KR/runesReforged.json')

RuneImageDirectory={}
print(Rune['slots'])
print(Rune['slots'][0])
print(Rune['slots'][0][0])
print(Rune['slots'][0][0]['runes'])
print(Rune['slots'][2][2]['runes'][1])
print(str(len(Rune['slots']))+"마법 지배 영감")
print(str(len(Rune['slots'][0]))+"첫째줄")
print(len(Rune['slots'][0][0]))
print(str(len(Rune['slots'][2][0]['runes']))+"줄마다 갯수")
print(len(Rune['slots'][1][2]['runes'][1]))
RuneDirectory=pd.read_json('C:/Users/Myeong Geun/PycharmProjects/lolapi/config/static/RuneDirectory.json')
print(RuneDirectory[8100][0])