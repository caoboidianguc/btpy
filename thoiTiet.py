import requests
import json


def diadiem(tpho):
    global tenTPho, bang
    url = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete"
    capYeuCau = {}
    capYeuCau['apikey'] = '4mAQ2hzQGsZtHM3mM4LPfErIUpxzBLXl'
    capYeuCau['q'] = tpho
    capYeuCau['details'] = False
    #API Key	4mAQ2hzQGsZtHM3mM4LPfErIUpxzBLXl
    response = requests.get(url, params=capYeuCau)
    #print(response.url)
    majson = response.json()
    mavung = majson[0]['Key']
    tenTPho = majson[0]['LocalizedName']
    bang = majson[0]['AdministrativeArea']['LocalizedName']
    #return mavung
    return dubao(mavung)
    



def noiDungDuBao(thogtin):
    try:
        mota = thogtin['Headline']['Text']
        ngaydubao = thogtin['DailyForecasts'][0]['Date']
        nhietdothap = thogtin['DailyForecasts'][0]['Temperature']['Minimum']['Value']
        donvi = thogtin['DailyForecasts'][0]['Temperature']['Minimum']['Unit']
        nhietdocao = thogtin['DailyForecasts'][0]['Temperature']['Maximum']['Value']
        hienThiNoiDung = '{}\n{}\n{} \nNgay {} \nNhiet Do Cao Nhat la({}): {}\nNhiet Do Thap Nhat la({}): {}'.format(tenTPho, bang, mota,ngaydubao,donvi,nhietdocao,donvi,nhietdothap)
    except:
        hienThiNoiDung = 'Loi ket noi mang!'
    return hienThiNoiDung



def dubao(mavung):
    #mavung = diadiem(tpho)
    url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/' + mavung
    capd = {}
    capd['apikey'] = '4mAQ2hzQGsZtHM3mM4LPfErIUpxzBLXl'
    capd['metric'] = False
    res = requests.get(url, params=capd)
    print(res.url)
    thogtin = res.json()
    bang = noiDungDuBao(thogtin)
    return bang


kiemtra = diadiem('columbia')
print(kiemtra)






