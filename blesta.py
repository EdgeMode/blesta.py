import collections
import requests
from datetime import datetime


def flatten(d, parent_key=''):
    items = []
    for k, v in d.items():
        new_key = parent_key + '[' + k + ']' if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)


class api(object):

    def __init__(self):
        self.server = 'my.blesta.server'
        self.user = 'MyBlestaApiUser'
        self.key = 'MyBlestaApiKey'

    def call(self, verb, classname, method, value_dict={}):
        api_target = 'http://' + self.server + '/api'
        urlstring = '/' + classname + '/' + method + '.json'

        if verb.lower() == 'get':
            querystring = '?'
            for key, value in flatten(value_dict).items():
                querystring += key + '=' + str(value) + '&'
            r = requests.get(url=api_target + urlstring + querystring, auth=(self.user, self.key))

        elif verb.lower() == 'delete':
            querystring = '?'
            for key, value in flatten(value_dict).items():
                querystring += key + '=' + str(value) + '&'
            r = requests.delete(url=api_target + urlstring + querystring, auth=(self.user, self.key))

        elif verb.lower() == 'post':
            postdata = flatten(value_dict).items()
            r = requests.post(url=api_target + urlstring, auth=(self.user, self.key), data=postdata)

        elif verb.lower() == 'put':
            postdata = flatten(value_dict).items()
            r = requests.put(url=api_target + urlstring, auth=(self.user, self.key), data=postdata)

        else:
            raise Exception("Unrecognised HTTP verb: %s" % str(verb))

        if r.status_code is not 200:
            raise Exception("Blesta API returned HTTP error response: %s" % str(r.status_code) + r.text)

        response_dict = dict(r.json())
        response_dict['status'] = r.status_code
        if 'response' not in response_dict.keys():
            response_dict['response'] = ''

        return response_dict


def blestadate_to_pythondate(blestadate):
    pythondate = datetime.strptime(str(blestadate), '%Y-%m-%d %H:%M:%S')
    return pythondate


def blestacurrency_to_dollars(blestacurrency):
    dollars = '$' + blestacurrency[:-2]
    return dollars
