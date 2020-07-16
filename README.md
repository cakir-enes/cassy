# Datasets

- https://archive.org/details/twitter_cikm_2010 -> Training 115k users, 3.8M tweet. Test 5K user 5M tweet. Study for geolocated tweeting.
- training_set_users.txt -> UserId\tUserLoc ; training_set_tweets.txt UserId\tTweetId\tTweet\tCreatedAt

- http://academictorrents.com/details/2399616d26eeb4ae9ac3d05c7fdd98958299efa9 Followers 11M



## Cassandra Tables:

CREATE TABLE posts_by_user (
userid text, 
postid text, 
post text, 
posted timestamp, 
PRIMARY KEY ((userid), posted)
) WITH CLUSTERING ORDER BY (posted DESC);


3s group by
4ms user posts ordered by time (2m records, 334 post)
