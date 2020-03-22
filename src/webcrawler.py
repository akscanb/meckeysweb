import praw
import os
import time

reddit = praw.Reddit(
    client_id=os.environ['CLIENT_ID'], 
    client_secret=os.environ['CLIENT_SECRET'],
    user_agent=os.environ['USER_AGENT']
)

print(reddit.read_only)
current_timestamp = time.time()
two_months_timestamp = current_timestamp - (60*60*24*60)
for submission in reddit.subreddit('mechmarket').stream.submissions():
    print(submission.title)
    print(submission.link_flair_text)
