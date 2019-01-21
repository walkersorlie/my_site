import requests
import json as json_py
import os
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured
from datetime import datetime
from homepage.models import Repository
import sys


class Command(BaseCommand):
    help = 'Checks github repos for into'


    def handle(self, *args, **options):
        url = 'https://api.github.com/graphql'
        query = {
            "query": "{viewer {repositories(first: 20) {totalCount edges {node {name description pushedAt url} cursor} pageInfo {endCursor hasNextPage}}}}"
        }

        try:
            api_token = os.environ['MY_SITE_GITHUB_ACCESS_TOKEN']

        except KeyError:
          raise ImproperlyConfigured('Environment variable "%s" not found.' % name)

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

        repo_list = []
        total_count = result['data']['viewer']['repositories']['totalCount']

        for repo_num in range(total_count):
            self.stdout.write(str(repo_num))

            current_repo = result['data']['viewer']['repositories']['edges'][repo_num]

            self.stdout.write(str(current_repo))
            self.stdout.write(current_repo['node']['name'])

            name = current_repo['node']['name']

            description = current_repo['node']['description']
            if description is None:
                description = ''

            dt = current_repo['node']['pushedAt']
            pushed_at = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%SZ')
            self.stdout.write(str(pushed_at))

            url = current_repo['node']['url']

            repo_list.append(name)

            if Repository.objects.filter(repo_name=name):
                self.stdout.write('check')
                repo = Repository.objects.get(repo_name=name)

                # if it is, check pushed_at. If database time is older, then update fields. Check for differences first????
                if repo.pushed_at < pushed_at:
                    repo.update(description=description, pushed_at=pushed_at, url=url)
                    repo.save()
            else:
                self.stdout.write('add')
                new_entry = Repository(repo_name=name, description=description, pushed_at=pushed_at, url=url)
                new_entry.save()

        for repo in Repository.objects.all():
            if repo.repo_name not in repo_list:
                Repository.objects.get(repo_name=name).delete()



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
