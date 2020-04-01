import json, requests

subreddit = 'copypasta'

r = requests.get(
    'http://www.reddit.com/r/{}.json'.format(subreddit),
    headers={'user-agent': 'Mozilla/5.0'})

post_list = []

for post in r.json()['data']['children']:
    export_post = {'title': "EMPTY", 'content': "EMPTY", 'link': "EMPTY"}
    export_post['title'] = post['data']['title']
    export_post['content'] = post['data']['selftext']
    export_post['link'] = post['data']['url']
    post_list.append(export_post)

with open("data.json", 'w') as outfile:
    json.dump(post_list, outfile)
