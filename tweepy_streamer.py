from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials # import credentials file


# create a class to filter tweets to make streaming more concise
class TwitterStreamer():
    """
    Class for streaming and processing live tweets
    """

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list): # look in itself, a file to save the tweets in, and filter by hashtag

        # this handles Twitter authentication and the connection to the twitter streaming api
        listener = StdOutListener() # create listener object
        auth = OAuthHandler(twitter_credentials.CONSUMER_API_KEY, twitter_credentials.CONSUMER_API_SECRET) #authenticate code
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET) #set access token using keys

        stream = Stream(auth, listener) 

        # filter tweets
        stream.filter(track=hash_tag_list)

# create a class to inherit from StreamListener class
class  StdOutListener(StreamListener):
    """
    This is a basic listener class that just prints received tweets to stdout
    """

    # a constructor that associates listener with the file it will write to
    def __init__(self): # here is different from the video: fetched_tweets_filename was taken out and defined after
        self.fetched_tweets_filename = fetched_tweets_filename  

    # the following two are overridden methods
    def on_data(self, data): # take in data streamed in from streamListener
        # what the hell is going on here i need to do some python reading
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf: # 'a' means append
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status): # if an error occurs
        print(status) # print status message from error to screen

# if in main part of program
if __name__ == "__main__":
       
       hash_tag_list = ["kim wonshik", "ravi", "vixx", "VIXX"]
       fetched_tweets_filename = "tweets.json" # could be tweets.txt
       
       # define a TwitterStreamer object
       myTwitterStreamer = TwitterStreamer()
       myTwitterStreamer.stream_tweets(fetched_tweets_filename, hash_tag_list)



