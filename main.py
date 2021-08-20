import requests 
# 導入 BeautifulSoup 模組(module)：解析HTML 語法工具
import bs4
import datetime
import time
import json

#while(1):
    #now_time = datetime.datetime.now().strftime('%H:%M:%S')
    #time.sleep(1)
    #print(now_time)

def get_one_page(URL):
    your_key = 'CWB-C8ACFDB1-541F-435F-8351-998F26FF2B4D'
    r = requests.get(URL)
    json_str = r.text

    jsondata=json.loads(json_str)
    info = (jsondata['records']['earthquake'][0]['reportContent'])
    detail = (jsondata['records']['earthquake'][0]['earthquakeInfo'])
    print(info)
    print(detail)   

        

# 組成 正確 URL
link = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-C8ACFDB1-541F-435F-8351-998F26FF2B4D&format=JSON"
# 執行單頁面網頁爬蟲
get_one_page(link)
# 避免被太快被 PTT 封鎖請求
