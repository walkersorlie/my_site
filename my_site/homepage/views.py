import requests
import hmac
import json
import os
import logging
from django.utils.encoding import force_bytes
from django.utils import timezone
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.urls import reverse, NoReverseMatch
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Repository
from datetime import datetime
from ipaddress import ip_address, ip_network
from hashlib import sha1


class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'repo_list'

    def get_queryset(self):
        return Repository.objects.order_by('-pushed_at')



@csrf_exempt
def payload(request):

    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))

    try:
        client_ip_address = ip_address(forwarded_for)
    except ValueError:
        return HttpResponseForbidden('Client IP Permission denied.')

    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Client IP 2 Permission Denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Request Signature Permission Denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    token = os.environ['GITHUB_WEBHOOK_TOKEN']
    mac = hmac.new(force_bytes(token), msg=force_bytes(request.body), digestmod=sha1)
    # print(force_bytes(mac.hexdigest()))
    # print(mac.hexdigest())
    # print(force_bytes(signature))
    # print(signature)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        # return HttpResponseForbidden('Request Signature 2 Permission Denied. %s %s' % (mac.hexdigest(), signature))
        return HttpResponseForbidden('Request Signature 2 Permission Denied.')


    """
    Make a delete function too?
    PROBLEM IF I CHANGE THE NAME OF THE REPO. SORT BY GITHUB REPO ID BETTER??? PROBABLY
    """
    json_data = json.loads(request.body)

    repo_name = json_data['repository']['name']
    description = json_data['repository']['description']
    pushed_at = timezone.make_aware(datetime.strptime(json_data['repository']['updated_at'], '%Y-%m-%dT%H:%M:%SZ'))
    url = json_data['repository']['html_url']

    print('updating')
    Repository.objects.filter(repo_name=repo_name).update(description=description, pushed_at=pushed_at, url=url)

    print('good')
    return HttpResponse('good')
