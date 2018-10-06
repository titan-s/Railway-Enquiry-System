import requests
url="https://api.railwayapi.com/v2/live/train/"
train_no=input("Input train no. : ")
url=url+train_no+"/date/"
#date=datetime.date.today()
date=input("date <dd-mm-yyyy> : ")
url=url+date+"<ENTER YOUR API KEY>"
json_data=requests.get(url).json()
print(json_data)
print(type(json_data))
print()
print(json_data['train'])
print(type(json_data['train']))
print(type(json_data['train']['days']))
for day in json_data['train']['days']:
    print(day['code']," ",day['runs'])

print()
print(type(json_data['route']))
for r in json_data['route']:
    print(r['station']['name'],": ",r['status'],": ",r['scharr'],": ",r['schdep'])
