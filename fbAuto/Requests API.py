import requests
import time
import random
import pickle
import pyautogui
with open('matruycap', 'r') as filetext:
    token = filetext.readline()
req = "Steam?fields=posts.limit(5){message}"

def req_facebook(req):
    r = requests.get("https://graph.facebook.com/v2.11/" + req, {'access_token': token})
    return r

results = req_facebook(req).json()
data = []
results = results['posts']
i = 0
while True:
    try:
        time.sleep(random.randint(2, 5))
        data.append(results['data'])
        r = requests.get(results['paging']['next'])
        results = r.json()
        i += 1
    except:
        print('done')
        break
print(data)
# pickle.dump(data, open("steam_data.pkl", "wb"))
# loaded_data = pickle.load(file=open("steam_data.pkl "))