from urllib import request
from bs4 import BeautifulSoup
import time


while True:
    try:
        target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159")
        soup = BeautifulSoup(target, 'xml') #data 불러옴

        #print(soup)


        for location in soup.select("location"):

            if location.select_one("city").string == '부산':
                """
                print("city:", location.select("city"))
                print("weather:", location.select("wf"))
                print("low:", location.select("tmn"))
                print("high:", location.select("tmx"))
                """
                weather = list(location.select("wf"))
                low = list(location.select("tmn"))
                high = list(location.select("tmx"))

                weather_list = [item1.strip('<wf>').strip('</wf>') for item1 in weather]
                low_list = [int(''.join(filter(str.isdigit, item2))) for item2 in low]
                high_list = [int(''.join(filter(str.isdigit, item3))) for item3 in high]

                print(weather_list)
                print(low_list)
                print(high_list)


    except:
        print("finish!!")
        exit(1)

    time.sleep(10)




