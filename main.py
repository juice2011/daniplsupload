import praw
import time

day = 0

reddit = praw.Reddit(
    client_id="mA7R9ISAYzkt7GVPl7o3Cg",
    client_secret="f6aU3zQjLG_ukyBFn_4NdTLTvD4Mug",
    password="Pootie2011",
    user_agent="DANI PLS UPLOAD",
    username="Juice20115932",
)


while (day != 10):
    time.sleep(4)
    day += 1

    subreddit = reddit.subreddit("TESTINGAPILOLOL")

    subreddit.submit(title="Day" + " " + str(day) + " " + "Of Asking Dani To Upload", flair_text="TEST",
                     selftext="Please For My Sanity Upload")

    print(subreddit.display_name + " " + subreddit.fullname)

