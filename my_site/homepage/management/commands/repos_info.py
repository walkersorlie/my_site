import requests
import json as json_py
import os
from django.core.management.base import BaseCommand, CommandError
from homepage.models import Repository
import sys


class Command(BaseCommand):
    help = 'Checks github repos for into'

    def handle(self, *args, **options):
        url = 'https://api.github.com/graphql'
        query = {
            "query": "{viewer {repositories(first: 20) {totalCount edges {node {name description pushedAt url} cursor} pageInfo {endCursor hasNextPage}}}}"
        }
        api_token = os.environ['MY_SITE_GITHUB_ACCESS_TOKEN']
        headers = {'User-Agent': 'Mozilla/5.0', 'Authorization': 'token %s' % api_token}

        r = requests.post(url=url, json=query, headers=headers)
        # print (r.text)
        # print (json_py.dumps(r.text, sort_keys=True, indent=4))
        # print (json_py.loads(r.text))
        # print (r.json())
        # self.stderr.write(r.text)
        self.stderr.write(str(r.json()))

        result = json_py.loads(r.text)
        # print ()
        # print (result['data']['viewer']['repositories']['edges'][0])
        # print (result['data']['viewer']['repositories']['edges'][1])
        # print ()
        # print (result['data']['viewer']['repositories']['totalCount'])
        # print (result['data']['viewer']['repositories']['edges'][0])

        # self.stdout.write('')

        # print (result['data']['viewer']['repositories']['pageInfo']['endCursor'])
        # print (result['data']['viewer']['repositories']['pageInfo']['hasNextPage'])

        total_count = result['data']['viewer']['repositories']['totalCount']

        for repo_num in range(total_count):
            self.stdout.write(str(repo_num))
            # check if each repo is in the database or not
            # if not, create new entry
            # if it is, check pushed_at. If database time is older, then update fields. Check for differences first????
            current = result['data']['viewer']['repositories']['edges'][repo_num]
            self.stdout.write(str(current))
            self.stdout.write(current['node']['name'])
            name = current['node']['name']
            if Repository.objects.filter(repo_name=name):
                self.stdout.write('check')
            else:
                self.stdout.write('add')


        # if has_next_page:
        #     query = {
        #         "query": "{viewer {repositories(first: 3 after: \"" + end_cursor + "\") {totalCount edges {node {name description pushedAt url} cursor} pageInfo {endCursor hasNextPage}}}}"
        #     }
        #     r = requests.post(url=url, json=query, headers=headers)
        #
        #     result = json_py.loads(r.text)
        #     has_next_page = result['data']['viewer']['repositories']['pageInfo']['hasNextPage']
        #     print (result['data']['viewer']['repositories']['pageInfo'])
        #     end_cursor = result['data']['viewer']['repositories']['pageInfo']['endCursor']
        #     print (r.json())
        #     print ()
        # else:
        #     break
