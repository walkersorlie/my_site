import requests
import json as json_py
import os
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
from homepage.models import Repository


def handle_repo(repo):
    repo = repo['node']

    db_repo, created = Repository.objects.update_or_create(
        repo_name = repo['name'],
        defaults = {
            'repo_name' : repo['name'],
            'description' : repo['description'] if repo['description'] is not None else '',
            'pushed_at' : timezone.make_aware(datetime.strptime(repo['pushedAt'], '%Y-%m-%dT%H:%M:%SZ')),
            'url' : repo['url'],
        }
    )
    # print('%s created: %s', str(db_repo.repo_name), str(created))

    return db_repo.repo_name


class Command(BaseCommand):
    help = 'Gets repository information from GitHub'


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
        # self.stderr.write(r.text)
        # self.stderr.write(str(r.json()))
        # print (result['data']['viewer']['repositories']['edges'][0])
        # print (result['data']['viewer']['repositories']['edges'][1])
        # print (result['data']['viewer']['repositories']['totalCount'])
        # print (result['data']['viewer']['repositories']['edges'][0])
        # print (result['data']['viewer']['repositories']['pageInfo']['endCursor'])
        # print (result['data']['viewer']['repositories']['pageInfo']['hasNextPage'])

        result = json_py.loads(r.text)

        total_count = result['data']['viewer']['repositories']['totalCount']
        repo_list = [result['data']['viewer']['repositories']['edges'][i] for i in range(total_count)]
        # self.stdout.write(str(test_list))

        # Make the Pool of workers
        pool = ThreadPool()
        current_repos_list = pool.map(handle_repo, repo_list)
        pool.close()
        pool.join()

        # Thread this too???
        all_repos = Repository.objects.all()
        for repo_name in all_repos:
            if repo_name.repo_name not in current_repos_list:
                Repository.objects.get(repo_name=repo_name).delete()

        """
        if has_next_page:
            query = {
                "query": "{viewer {repositories(first: 3 after: \"" + end_cursor + "\") {totalCount edges {node {name description pushedAt url} cursor} pageInfo {endCursor hasNextPage}}}}"
            }
            r = requests.post(url=url, json=query, headers=headers)

            result = json_py.loads(r.text)
            has_next_page = result['data']['viewer']['repositories']['pageInfo']['hasNextPage']
            print (result['data']['viewer']['repositories']['pageInfo'])
            end_cursor = result['data']['viewer']['repositories']['pageInfo']['endCursor']
            print (r.json())
            print ()
        else:
            break
        """
