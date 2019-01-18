import requests
import json as json_py
import os

url = 'https://api.github.com/graphql'
query = {
    "query": "{viewer {repositories(first: 3) {totalCount edges {node {name description pushedAt url} cursor} pageInfo {endCursor hasNextPage}}}}"
}
api_token = os.environ['MY_SITE_GITHUB_ACCESS_TOKEN']
headers = {'User-Agent': 'Mozilla/5.0', 'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=query, headers=headers)
# print (r.text)
# print (json_py.dumps(r.text, sort_keys=True, indent=4))
# print (json_py.loads(r.text))

print (r.json())

result = json_py.loads(r.text)
# print ()
# print (result['data']['viewer']['repositories']['edges'][0])
# print (result['data']['viewer']['repositories']['edges'][1])
print ()
# print (result['data']['viewer']['repositories']['pageInfo'])
# print (result['data']['viewer']['repositories']['pageInfo']['endCursor'])
# print (result['data']['viewer']['repositories']['pageInfo']['hasNextPage'])

has_next_page = result['data']['viewer']['repositories']['pageInfo']['hasNextPage']
end_cursor = result['data']['viewer']['repositories']['pageInfo']['endCursor']

while has_next_page:
    query = {
        "query": "{viewer {repositories(first: 3 after: \"" + end_cursor + "\") {totalCount edges {node {name description pushedAt url} cursor} pageInfo {endCursor hasNextPage}}}}"
    }
    r = requests.post(url=url, json=query, headers=headers)

    result = json_py.loads(r.text)
    has_next_page = result['data']['viewer']['repositories']['pageInfo']['hasNextPage']
    end_cursor = result['data']['viewer']['repositories']['pageInfo']['endCursor']
    print (r.json())
    print ()
