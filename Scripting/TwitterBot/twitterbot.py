import tweepy
import yaml

with open("config.yaml") as f:
    try:
        config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(e)


def about_me(client: tweepy.Client) -> None:
    """Print information about the client's user."""
    # The `public_metrics` addition will give me my followers count, among other things
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")


api = tweepy.Client(
    bearer_token=config["BEARER_TOKEN"],
    consumer_key=config["CONSUMER_KEY"],
    consumer_secret=config["CONSUMER_SECRET"],
    access_token=config["ACCESS_TOKEN"],
    access_token_secret=config["ACCESS_TOKEN_SECRET"],
    wait_on_rate_limit=True,
)

# user = api.get_me()
# ID = user.data.id

search_string = "Raja Haseeb"
number_of_tweets = 5  # we want two items

# Follower bot
# for follower in api.get_users_followers(id=ID).data:
#     print(follower.username)
#     if follower.username == "Hassanrajapk":
#         id_follower = follower.id
#         print(id_follower)
#         api.follow_user(id_follower)
#         break


# Liking a tweet
for tweet in api.search_recent_tweets(search_string).data[:number_of_tweets]:
    print(tweet)
    try:
        api.like(tweet.id, user_auth=True)
        print("I liked that tweet!")
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break

# response = api.get_users_followers(id=ID)
# print(response.data)


# user = api.get_me()
# print(user.data.name)

# about_me(api)

# public_tweets = api.get_home_timeline()
# for tweet in public_tweets.data:
#     print(tweet.text)
