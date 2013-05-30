#!/usr/bin/env python

import requests
import json

api_uri = 'http://api.beatport.com'
#api_uri = 'http://api.beatport.com/catalog/3/artists?id=2'

class beatportAPI(object):

    @property
    def uri_name(self):
        return self.__class__.__name__.lower()

    @property
    def response(self):
        return requests.get(self.uri, params=self.payload)

    @property
    def status(self):
        return self.response.status_code

    @property
    def data(self):
        if self.response.content and self.status == 200:
            json_data = json.loads(self.response.content)
            json_data = json_data.get('results')[0]
            return json_data
        else:
            return HTTPError(self.status)

class Artists(beatportAPI):
    def __init__(self, **kwargs):
        self.payload = kwargs
        self.uri = api_uri + '/catalog/3/' + self.uri_name

class Tracks(beatportAPI):
    def __init__(self, **kwargs):
        self.payload = kwargs
        self.uri = api_uri + '/catalog/3/' + self.uri_name

class Genres(beatportAPI):
    def __init__(self, **kwargs):
        self.payload = kwargs
        self.uri = api_uri + '/catalog/3/' + self.uri_name

if __name__ == '__main__':
    pass
