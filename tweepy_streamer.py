from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials # import credentials file

#create a class to inherit from StreamListener class
class  StdOutListener(StreamListener):

#the following two are overridden methods
    def on_data(self, data): # take in data streamed in from streamListener
        print(data)
        return True

    def on_error(self, status): # if an error occurs
        print(status) # print status message from error to screen

# if in main part of program
if __name__ == "__main__":
    
    listener = StdOutListener() # create listener object
    auth = OAuthHandler(twitter_credentials.CONSUMER_API_KEY, twitter_credentials.CONSUMER_API_SECRET) #authenticate code
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET) #set access token using keys

    stream = Stream(auth, listener) 

    # filter tweets
    stream.filter(track = ['vixx', 'bts', 'super junior', 'VIXX'])
