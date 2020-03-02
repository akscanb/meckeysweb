import praw
import os

reddit = praw.Reddit(
    client_id=print(os.environ['CLIENT_ID']), 
    client_secret=print(os.environ['CLIENT_SECRET']),
    user_agent=print(os.environ['USER_AGENT'])
)

print(reddit.read_only)

for submission in reddit.subreddit('mechmarket').hot(limit=10):
    print(submission.title)
