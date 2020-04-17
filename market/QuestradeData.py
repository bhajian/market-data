import requests
import json
import numpy as np

loginUrl = 'https://login.questrade.com/oauth2/'


def login(token):
    url = loginUrl + 'token?grant_type=refresh_token&refresh_token={}'.format(token)
    resp = requests.get(url)
    if resp.ok:
        jData = json.loads(resp.content)
        return np.array(jData)


def getCandles(baseUrl, symbolId, startTime, endTime, interval, token):
    url = baseUrl + 'v1/markets/candles/{}?startTime={}&endTime={}&interval={}'\
        .format(symbolId, startTime, endTime, interval)
    headers = {'Authorization': 'Bearer {}'.format(token)}
    resp = requests.get(url, headers=headers)
    if resp.ok:
        jData = json.loads(resp.content)
        return np.array(jData)


def searchSymbol(baseUrl, symbol, token):
    url = baseUrl + 'v1/symbols/search?prefix={}'.format(symbol)
    headers = {'Authorization': 'Bearer {}'.format(token)}
    resp = requests.get(url, headers=headers)
    if resp.ok:
        jData = json.loads(resp.content)
        return np.array(jData["symbols"][0])