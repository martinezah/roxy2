import requests
import settings

class Artifact():
    @staticmethod
    def get_by_url(url):
        response = {}
        headers = {'Authorization': 'Token {}'.format(settings.MEMEX_API_TOKEN), 'Content-Type': 'application/json'}
        try:
            if url is not None:
                response = requests.get('{}{}'.format(settings.MEMEX_API_URL, url), headers=headers, verify=False).json()
        except:
            pass
        return response

    @staticmethod
    def get_by_key(key):
        headers = {'Authorization': 'Token {}'.format(settings.MEMEX_API_TOKEN), 'Content-Type': 'application/json'}
        try:
            if key is not None:
                response = requests.get('{}/artifacts/{}'.format(settings.MEMEX_API_URL, key), headers=headers, verify=False).json()
            else:
                response = requests.get('{}/artifacts/?limit=1&expand=1'.format(settings.MEMEX_API_URL), headers=headers, verify=False).json()[0]
                key = response.get('key')
            if key is not None:
                response['adjacent'] = requests.get('{}/artifacts/adjacent/to/{}'.format(settings.MEMEX_API_URL, key), headers=headers, verify=False).json()[0]
        except:
            response = {}
        return response

