import webbrowser 
import praw

reddit = praw.Reddit(
    client_id = "J3POXaCcpRSCR7c6povU2Q",
    client_secret = "m22iNjZn8Su9z3f-JXGS7EwvuDEq_w",
    password = "Masti@321",
    user_agent = "my user agent",
    username = "Embarrassed-Big389",
)

random_submission = reddit.subreddit('playboicarti').random()
print(random_submission.title)
webbrowser.open(random_submission.url)
