from TwitterAPI import TwitterAPI
api = TwitterAPI("4lwy77hY2gYaNjRejD7wN7BA6", 
                "TEv5phCk7F4FJbn9zj7aUnfDjRzCUcUYXXFs4r39TdlijdxxPm", 
                "1272061300282060801-bslZ4uGCUHZh3oWStI6oSEjcDgyvB2", 
                "USXN3I2ayHMBWQk2G5T2oByfj2ByRntk9l9juplRtY4rD",
                api_version='2')

r = api.request('users/:4939401/followers', {'max_results':1000, 'user.fields': ['location', 'name', 'username']})


