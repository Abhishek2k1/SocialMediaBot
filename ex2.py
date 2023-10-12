import praw
import random
import time
reddit = praw.Reddit(
    client_id="J3POXaCcpRSCR7c6povU2Q",
    client_secret="m22iNjZn8Su9z3f-JXGS7EwvuDEq_w",
    user_agent="<1st_bot>",
    username='Embarrassed-Big389',
    password='Masti@321'
)

# get subreddit
subreddit = reddit.subreddit("anime")

sad_quotes = [
"Every one of us must do what is in our powers! If we are going to die anyway, then it is better to die fighting than to do nothing!- Sakura Haruno",
"A real ninja is one who endures no matter what gets thrown at him ... All you do need is the guts to never give up. Jiraiya",
"Never underestimate your opponent, no matter how small they may seem.- Shino Aburame"
"Hard work is worthless for those that do not believe in themselves.- Naruto Uzumaki"
"Power is not will, it is the phenomenon of physically making things happen.- Madara Uchiha"
""
]


# you can get whatever amount of the post you want
for submission in subreddit.hot(limit=10):
    # print(submission.title)

    # getting the comment of the post
    for comment in submission.comments:
        # here we are defining that if the comment had a body then only print the comment
        if hasattr(comment, "fight"):
            # converting the comment is lower case
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("-----------")
                print(comment.body)
                # choosing random quote in the list
                random_index = random.randint(0, len(sad_quotes) - 1)
                comment.reply(sad_quotes[random_index])
                # this allows your bot to sleep for 700 seconds
                time.sleep(700)