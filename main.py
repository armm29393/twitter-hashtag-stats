import pytz
from datetime import datetime, timedelta
from thai_strftime import thai_strftime
from config import *

endDate = datetime.utcnow().replace(tzinfo=pytz.UTC)
startDate = endDate - timedelta(hours=16)
localDate = endDate.astimezone(pytz.timezone("Asia/Bangkok"))

print('startDate>>', startDate)
print('endDate>>', endDate)

for s in config['data']:
    print(f'Getting {s["title"]} stats...')
    data_all, data_tweet, data_retweet = search(s['q'], startDate, endDate - timedelta(seconds=10))
    status = f'{config["header"]}\n\n'
    status += f'วันที่ {thai_strftime(localDate, fmt="%-d %b %Y %H:%M", buddhist_era=False)}\n'
    status += f'{s["type"].capitalize()}: {s["title"]}\n\n'
    status += f'Tweet: {data_tweet}\n'
    status += f'Retweet: {data_retweet}\n'
    status += f'Total: {data_all}\n\n'
    status += f'{config["footer"]}'
    print(status)
    print('-'*30)
    postTweet(status)
