import praw

def redditConnect():
    reddit=praw.Reddit(client_id="J3POXaCcpRSCR7c6povU2Q",
                        client_secret= "m22iNjZn8Su9z3f-JXGS7EwvuDEq_w",
                        user_agent="my user agent",
                        username="",
                        password="",
    )
    print(reddit.read_only)
    return reddit

def printPostFromSubreddit (redditCon, subreddit):
    for submission in redditCon.subreddit (subreddit).hot(limit=2):
        print(submission.title)
        print("**********************************************************")

def postToReddit(redditCon, subreddit, title, url):
    redditCon.validate_on_submit = 1
    subreddit = redditCon.subreddit(subreddit)
    subreddit.submit(title, url=url)
    print("Post submitted")

if __name__ == '__main__':
    printPostFromSubreddit (redditConnect(), 'quotes')