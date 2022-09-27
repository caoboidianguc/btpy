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
    return mavung



ma = diadiem('columbia')
    
print(tenTPho)
print(ma)
