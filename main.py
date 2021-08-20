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
    earNo = jsondata['records']['earthquake'][0]['earthquakeNo']
    ori_time = (jsondata['records']['earthquake'][0]['earthquakeInfo']['originTime'])
    epic_lat_val = (jsondata['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['epiCenterLat']['value'])
    epic_lat_unit = (jsondata['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['epiCenterLat']['unit'])
    epic_lon_val = (jsondata['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['epiCenterLon']['value'])
    epic_lon_unit = (jsondata['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['epiCenterLon']['unit'])
    ear_depth_val = (jsondata['records']['earthquake'][0]['earthquakeInfo']['depth']['value'])
    ear_depth_unit = (jsondata['records']['earthquake'][0]['earthquakeInfo']['depth']['unit'])
    location = (jsondata['records']['earthquake'][0]['earthquakeInfo']['epiCenter']['location'])
    inf_area =  (len(jsondata['records']['earthquake'][0]['intensity']['shakingArea']))
    print(info)#大概資訊
    print('No.',earNo)#案件編號
    print('發生位置','北緯:',epic_lat_val,epic_lat_unit,'東經:',epic_lon_val,epic_lon_unit)
    print('地震深度:',ear_depth_val,ear_depth_unit)
    print('震央位置',location)
    for t in range(inf_area):
        print((jsondata['records']['earthquake'][0]['intensity']['shakingArea'][t]['areaDesc']))
        #print('\n')
        print((jsondata['records']['earthquake'][0]['intensity']['shakingArea'][t]['areaName']))
    #print(inf_area)
    #print(detail)
    

        

# 組成 正確 URL
link = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-C8ACFDB1-541F-435F-8351-998F26FF2B4D&format=JSON"
# 執行單頁面網頁爬蟲
get_one_page(link)
# 避免被太快被 PTT 封鎖請求
