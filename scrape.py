import snscrape.modules.twitter as twitterScrapper
import json

scraper = twitterScrapper.TwitterSearchScraper("#BNB", False)

tweets = []

for i, tweet in enumerate(scraper.get_items()):
    if i > 50:
        break

    tweets.append({"id" : tweet.id, "content" : tweet.content, "likes" : tweet.likeCount})

f = open("tweets.json", "w")
j = json.dumps(tweets)
f.write(j)
f.close()