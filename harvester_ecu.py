'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########CREDENCIALES API TWITTER  ############   
ckey = "7oS2MLGrkGwOjZqsLE9bAJFXU"
csecret = "uKNiOxWy6rFGcMKU2OI1eE044POKl91DkOyPQXs4Lf4GkOaQNi"
atoken = "1104101144-45oSJJYmIb5tQ0ie1moMp9mCRDnACyV9ExR7mJM"
asecret = "YJsiKXjc02ahZuB3d9YOYGg7yJp8da7Rx4N9fa1iNsG88"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
 
    def on_error(self, status):
        print status
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
 
 
if len(sys.argv)!=3:
    sys.stderr.write("Error: needs more arguments: <URL><DB name>\n")
    sys.exit()
 
URL = sys.argv[1]
db_name = sys.argv[2]
 
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
 
twitterStream.filter(locations=[-81.39, -5.02, -75.19, 1.88])  #ECUADOR
