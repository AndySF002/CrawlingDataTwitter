import tweepy
import datetime
import pandas as pd
from tweepy.auth import OAuthHandler

#Api Key & Api key secret
auth = OAuthHandler('')

#Access Token & Secret
auth.set_access_token('')

api = tweepy.API(auth, wait_on_rate_limit = True)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1) #mencari data sesuai tanggal 

str(today)
str(yesterday)

tweets = tweepy.Cursor(api.search_tweets, 
                       q = 'topik yang akan di cari', #isi '' dengan topik yang dicari
                      #q = 'Gempa Bumi since'+str(yesterday)+'until:'+str(today),
                      tweet_mode = 'extended',
                      lang = 'id',
                      count=100).items(5000) #jumlah data yang ingin di cari

output = []



for tweet in tweets:
    
    #text = tweet._json['full_text']
    data = {
        #"created_at" : tweet._json['created_at'],
        "full_text" : tweet._json['full_text']
    }
    output.append(data)
    
    #output
df= pd.DataFrame(output) #tampilkan data
df

df.to_csv('datamandalika.csv', index=False) #simpan data ke file csv
