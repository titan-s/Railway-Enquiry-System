import requests
url="https://api.railwayapi.com/v2/live/train/"
train_no=input("Input train no. : ")
url=url+train_no+"/date/"
#date=datetime.date.today()
date=input("date <dd-mm-yyyy> : ")
url=url+date+"/apikey/y3clwapnm8/"
json_data=requests.get(url).json()
position=json_data['position']

print('Current Status: ',position)


print(json_data)
