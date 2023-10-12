import praw

def redditConnect():
    reddit=praw.Reddit(client_id="J3POXaCcpRSCR7c6povU2Q",
                        client_secret= "m22iNjZn8Su9z3f-JXGS7EwvuDEq_w",
                        user_agent="my user agent",
                        username="",
                        password="Masti@321",
    )
    # for submission in reddit.subreddit("all").hot(limit=25):
    #     print(submission.title)
   
    print(reddit.read_only, "YEH PRINT HO RA")
    return reddit

def printPostFromSubreddit (redditCon, subreddit):
    for submission in redditCon.subreddit (subreddit).hot(limit=2):
        print(submission.title, "YEH HO RA")
        print(submission.score)
        print("**********************************************************")

selftext = '''
I am learning how to use the Reddit API with Python using the PRAW wrapper.
By following the tutorial on https://www.jcchouinard.com/post-on-reddit-api-with-python-praw/
This post was uploaded from my Python Script
'''
def postToReddit(redditCon, subreddit, title, selftext):
    redditCon.validate_on_submit = 1
    subreddit = redditCon.subreddit(subreddit)
    subreddit.submit(title, selftext)
    print("Post submitted")

if __name__ == '__main__':
    printPostFromSubreddit (redditConnect(), 'quotes')
    # postToReddit(redditConnect(), 'quotes', "MOTIVATION", selftext)