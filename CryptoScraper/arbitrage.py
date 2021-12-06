import requests
import time
import pandas

#Web Scraper for arbitrage trading Cryptocurrencies

"""   ---------    Defining important Functions     -----------"""

### pulling data from canadian exchange
def Quad(rate, fee):
    
    output = [["Trade Pair", "Ask", "Bid"]]
    
    quad_url = 'https://api.quadrigacx.com/v2/ticker?book='
    
    pair = ['btc_cad','btc_usd', 'eth_cad', 'ltc_cad','bch_cad']
    
    for p in pair:
        k = requests.get(url = quad_url+p , data = {}, headers = {})
        quad = k.json()
        ask = float( quad['ask'])
        bid = float( quad['bid'])
                      
        var = [ p, ask - fee*ask , bid - fee*bid ]
        output.append(var)
        time.sleep(1)
        
    output[2][1] =  output[2][1]* rate 
    output[2][2] =  output[2][2]* rate 
    
    
    return output


## pulling data from Kraken exchange
def Krak(rate, fee):
       # Getting data from Kraken
    output = [["Trade Pair", "Ask", "Bid"]]
    
    pairs1 = 'BCHUSD,XETHZUSD,XETHZCAD,XLTCZUSD,XXBTZUSD,XXBTZCAD'
    pairs2 = ['Bch_Usd',"eth_cad", 'Eth_Usd', 'Ltc_Usd',"btc_cad",'Btc_Usd']
    
    k_url_ticker = 'https://api.kraken.com/0/public/Ticker'
    k = requests.post(url = k_url_ticker + "?pair="+ pairs1, data = {}, headers = {})
    k_tick = k.json()
    
    
    i = 0
    for key, var in k_tick["result"].items():
        
        ask = float(var['a'][0])
        bid= float(var['b'][0])
        
        ask = ask + ask*fee
        bid = bid + bid*fee
        
        temp = [pairs2[i], ask*rate, bid*rate]
        output.append(temp)
        i = i+1
    output[2][1] =  output[2][1]/ rate 
    output[2][2] =  output[2][2]/ rate 
    output[5][1] =  output[5][1]/ rate 
    output[5][2] =  output[5][2]/ rate 
    time.sleep(1)
   
    return output
    
    
   
"""   ---------    Start of Script    -----------"""
CAD_USD = 1.29  # the cad to usd exchange rate
fee_quad = 0.005
fee_krak = 0.002
transfer = 0.001

fee_krak = fee_krak + transfer
korders = 'https://api.kraken.com/0/public/Depth'
qorders = 'https://api.quadrigacx.com/v2/order_book'
log = time.time()
while True :
    
    datk = Krak(rate = CAD_USD, fee = fee_krak)
    datq = Quad(rate = CAD_USD, fee = fee_quad)
    
    hello = []
    
    USD_BCH_CAD =  100.0*(datq[5][2]- datk[1][1] )/ datk[1][1] 
    USD_ETH_CAD =  100.0*(datq[3][2]- datk[3][1] )/ datk[3][1]
    USD_LTC_CAD =  100.0*(datq[4][2]- datk[4][1] )/ datk[4][1]
    USD_BTC_CAD =  100.0*(datq[1][2]- datk[6][1] )/ datk[6][1]
    USD_BTC_USD =  100.0*(datq[2][2]- datk[6][1] )/ datk[6][1]
    
    CAD_ETH_CAD =  100.0*(datq[3][2]- datk[2][1] )/ datk[2][1]
    CAD_BTC_USD =  100.0*(datq[2][2]- datk[5][1] )/ datk[5][1]
    CAD_BTC_CAD =  100.0*(datq[1][2]- datk[5][1] )/ datk[5][1]
    
    
    rhello = []
    
    rUSD_BCH_CAD =  100.0*(datk[1][2]- datq[5][1] )/ datk[1][1]
    rUSD_ETH_CAD =  100.0*(datk[3][2]- datq[3][1] )/ datk[3][1]
    rUSD_LTC_CAD =  100.0*(datk[4][2]- datq[4][1] )/ datk[4][1]
    rUSD_BTC_CAD =  100.0*(datk[6][2]- datq[1][1] )/ datk[6][1]
    rUSD_BTC_USD =  100.0*(datk[6][2]- datq[2][1] )/ datk[6][1]
    
    rCAD_ETH_CAD =  100.0*(datk[2][2]- datq[3][1] )/ datk[2][1]
    rCAD_BTC_USD =  100.0*(datk[5][2]- datq[2][1] )/ datk[5][1]
    rCAD_BTC_CAD =  100.0*(datk[5][2]- datq[1][1] )/ datk[5][1]
    
    
    hello.append([  'USD_ETH_CAD', USD_ETH_CAD  ])
    hello.append([ 'USD_LTC_CAD' , USD_LTC_CAD  ])
    hello.append([  'USD_BTC_CAD',  USD_BTC_CAD ])
    hello.append(['USD_BTC_USD'  ,  USD_BTC_USD  ])
    
    rhello.append([  'CAD_ETH_USD', rUSD_ETH_CAD  ])
    rhello.append([ 'CAD_LTC_USD' , rUSD_LTC_CAD  ])
    rhello.append([  'CAD_BTC_USD',  rUSD_BTC_CAD ])
    rhello.append(['USD_BTC_USD'  ,  rUSD_BTC_USD  ])
    
    

    ti = time.clock()
    print('time =' + str(ti))
    print()
    colum = ["Coins", "% Profit"]
    df = pandas.DataFrame(data = hello, columns = colum)
    
    print (df)
    print()
    print("REVERSED")
    
    df = pandas.DataFrame(data = rhello, columns = colum)
    
    print (df)
    print()
    
    
    time.sleep(3)