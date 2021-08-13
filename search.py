from TwitterAPI import TwitterAPI
import json
import pymongo
import datetime
import time
api = TwitterAPI("4lwy77hY2gYaNjRejD7wN7BA6", 
                "TEv5phCk7F4FJbn9zj7aUnfDjRzCUcUYXXFs4r39TdlijdxxPm", 
                "1272061300282060801-bslZ4uGCUHZh3oWStI6oSEjcDgyvB2", 
                "USXN3I2ayHMBWQk2G5T2oByfj2ByRntk9l9juplRtY4rD")

client = pymongo.MongoClient("mongodb+srv://zheverson:8326022@cluster0.m8gap.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


cursor = -1
num = 0
while cursor!=0:
    r = api.request('followers/list', {'user_id':4939401, 'count': 200, 'cursor': cursor})
    response = json.loads(r.text)
    cursor = response['next_cursor']
    users_info = [{'screen_name': j['screen_name'], 'location': j['location']} for j in response['users']]
    db.inventory.insert_many(users_info)
    num = num + 1
    db.time.insert_one({'num': num, 'time': str(datetime.datetime.now())})
    time.sleep(58)


