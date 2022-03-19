import pypi_rss
import requests
from celery import shared_task
from .models import Package


@shared_task
def collect_data(message):
    Package.objects.all().delete()
    for p in pypi_rss.get_newest_packages():
        try:
            url = 'https://pypi.org/pypi/' + p['name'] + '/json'
            r = requests.get(url).json()['info']

            Package.objects.create(title=r['name'], description=p['description'], author_name=r['author'],
                                   author_email=r['author_email'], version=r['version'],
                                   maintainer_email=r['maintainer_email'], maintainer_name=r['maintainer'],
                                   link=p['link'])
        except Exception as e:
            print(f'package details not found: {e}')
    print('package index updated')