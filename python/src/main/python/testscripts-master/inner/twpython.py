import tweepy
 
consumer_key = 'XetEQUsm8LAh3Du0dvUI0Q'
consumer_secret = 'RCkscaiVdcPDHRiQDAmLqa2Fb5j6twbhrpPCB9MHF0'
access_token = '41016643-7oA7bNZE3c69oyib8Wk5AMPNTqhq9dZv6BODkd8aA'
access_token_secret = 'w5CgpCeG4y95GgLgzmt36fvKjduZGZ7FMIFMLtHjj1M'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def print_image_tweet(hashtag, no_of_tweets):
    count = 0    
    for tweet in tweepy.Cursor(api.search,q=hashtag,include_entities=True).items():
        for image in  tweet.entities.get('media', []):
            print image, image['media_url']
            count = count + 1 
        if count == no_of_tweets:
            break

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print "Error:  Insufficient Argument---python twpython.py hashtag_name num_of_tweets"
        print "Example python twpython.py omg 5"
    else:
	print_image_tweet(sys.argv[1], int(sys.argv[2]))
