import requests
import json as json_py
import os
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
from datetime import datetime
from homepage.models import Repository


from multiprocessing.dummy import Pool as ThreadPool

def handle_repo(repo):
    # self.stdout.write(str(repo_num))

    repo = repo['node']
    # self.stdout.write(str(current_repo))
    # self.stdout.write(current_repo['node']['name'])

    # repo_name = repo['name']

    # description = repo['description']
    # if description is None:
    #     description = ''

    # dt = repo['pushedAt']
    # pushed_at = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%SZ')
    # pushed_at = timezone.make_aware(pushed_at)

    # url = repo['url']

    # repo_list.append(name)

    # try:
    #     Repository.objects.get(repo_name=repo_name).update(description=description, pushed_at=pushed_at, url=url)
    # except Repository.DoesNotExist:
    #     db_repo = Repository(repo_name=repo_name, description=description, pushed_at=pushed_at, url=url)
    #     db_repo.save()

    # Use with MySQL READ COMMITTED, rather than REPEATABLE READ
    db_repo, created = Repository.objects.update_or_create(
        repo_name = repo['name'],
        defaults = {
            'description' : repo['description'] if repo['description'] is not None else '',
            'pushed_at' : timezone.make_aware(datetime.strptime(repo['pushedAt'], '%Y-%m-%dT%H:%M:%SZ')),
            'url' : repo['url'],
        }
    )
    print('created: %s', str(created))

    # if Repository.objects.filter(repo_name=repo_name):
    #     db_repo = Repository.objects.get(repo_name=repo_name)
    #
    #     if db_repo.pushed_at < pushed_at:
    #         db_repo.description = description
    #         db_repo.pushed_at = pushed_at
    #         db_repo.url = url
    #         db_repo.save()
    # else:
    #     new_entry = Repository(repo_name=repo_name, description=description, pushed_at=pushed_at, url=url)
    #     new_entry.save()
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

        repo_list = []
        total_count = result['data']['viewer']['repositories']['totalCount']

        # figure out threading this sheeeet
        test_list = [result['data']['viewer']['repositories']['edges'][i] for i in range(total_count)]
        # self.stdout.write(str(test_list))


        # Make the Pool of workers
        pool = ThreadPool(4)
        # Open the urls in their own threads
        # and return the results
        current_repos_list = pool.map(handle_repo, test_list)
        # close the pool and wait for the work to finish
        pool.close()
        pool.join()

        self.stdout.write(str(current_repos_list))

        all_repos = Repository.objects.all()
        for repo_name in all_repos:
            # self.stderr.write(str(repo_name.repo_name))
            if repo_name not in current_repos_list:
                # self.stdout.write('delete: ' + str(repo.repo_name))
                # test = Repository.objects.get(repo_name=repo_name)
                # self.stderr.write(str(test))
                Repository.objects.get(repo_name=repo_name).delete()


        """
        for repo_num in range(total_count):
            # self.stdout.write(str(repo_num))

            current_repo = result['data']['viewer']['repositories']['edges'][repo_num]

            # self.stdout.write(str(current_repo))
            # self.stdout.write(current_repo['node']['name'])

            name = current_repo['node']['name']

            description = current_repo['node']['description']
            if description is None:
                description = ''

            dt = current_repo['node']['pushedAt']
            pushed_at = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%SZ')
            pushed_at = timezone.make_aware(pushed_at)
            # self.stdout.write(str(pushed_at))

            url = current_repo['node']['url']

            repo_list.append(name)

            if Repository.objects.filter(repo_name=name):
                # self.stdout.write('check')
                repo = Repository.objects.get(repo_name=name)

                # if it is, check pushed_at. If database time is older, then update fields. Check for differences first????
                # self.stdout.write(str(repo.pushed_at))
                # self.stdout.write(str(pushed_at))
                if repo.pushed_at < pushed_at:
                    repo.description = description
                    repo.pushed_at = pushed_at
                    repo.url = url
                    repo.save()
            else:
                # self.stdout.write('add')
                new_entry = Repository(repo_name=name, description=description, pushed_at=pushed_at, url=url)
                new_entry.save()

        for repo in Repository.objects.all():
            if repo.repo_name not in repo_list:
                # self.stdout.write('delete: ' + str(repo.repo_name))
                Repository.objects.get(repo_name=name).delete()
        """




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
