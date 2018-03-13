import os
import time
import tweepy
consumer_key = 'xQ9YvqCAb46kiVNBMsgnCoJjK'
consumer_secret = 'whpMlUA3YZuslYrMaVB15o0DO8y4WXtrfOAvGk51NI68YyGToz'
access_token = '3273763111-r1CBfJqmmOdeMEXWNTR1roz2F1rKfEdzVnDmdoN'
access_token_secret = 'JmTiDOtCicLnAEmz22mxCWojLN2M19YJCQVyU3hBNFCEE'

# these are the key and access secret codes for sending the tweet
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
b=1
a=0
while a<=2 :
    img="/home/cs2017a102/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 800*600 "+img
    os.system(cmd)
    print ("pic taken")
    #read image from location
    api.update_with_media(img, status="Nice one")
    print("wait for 5 seconds for selfiee!!")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
