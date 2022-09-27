from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



listCoin = ["Dogecoin", "Cardano", "Stellar", "Bitcoin Cash", "Litecoin", "Ethereum Classic"]


def xulyThongTin(tinTraVe, tenCoin):
      soLanYeuCau = tinTraVe['status']['elapsed']
      #print(f"Số lần yêu cầu: {soLanYeuCau}")
      
      dulieu = tinTraVe['data']
      #print(type(dulieu)) #-->list
      for thing in dulieu:
            if thing['name'] == tenCoin:
                  marketCap = thing['cmc_rank']
                  giaCoin = thing['quote']['USD']['price']
                  print(tenCoin)
                  print(f"Xếp hạng {marketCap} - tổng tiền vào coin.")
                  print(f"Giá : {giaCoin} USD")
                  print("-------+------------+------------")
                  print()
            
            

def yeuCauData() :
      url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
      headers = {}
      para = {}
      para['start'] = '1'
      para['limit'] = '30'
      para['convert'] = 'USD'
      para['sort'] = 'market_cap'

      headers['Accepts'] = 'application/json'
      headers['Accept-Encodeing'] = 'deflare, gzip'
      headers['X-CMC_PRO_API_KEY'] = '6b9982e2-c01f-48c6-b6c7-fe9c4c4af28d'
      session = Session()
      session.headers.update(headers)

      try:
        response = session.get(url, params=para)
        tinTraVe = response.json()

        #tinTraVe = json.loads(response.text)
        #injson = json.dumps(tinTraVe, indent=4)
        #print(injson)


      except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

      return xulyThongTin(tinTraVe, tenCoin)



for tenCoin in listCoin:
      yeuCauData()