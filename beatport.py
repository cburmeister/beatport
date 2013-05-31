#!/usr/bin/env python

import requests
import json

api_host = 'http://api.beatport.com'
api_version = '3'


class HTTPError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class beatportAPI(object):
    def __init__(self, **kwargs):
        self.cached_response = None
        self.payload = kwargs

    @property
    def uri_name(self):
        return self.__class__.__name__.lower()

    @property
    def uri(self):
        return '%s/%s/%s/%s' % (api_host, 'catalog', api_version, self.uri_name)

    @property
    def response(self):
        if not self.cached_response:
            return requests.get(self.uri, params=self.payload)
        return self.cached_response

    def clear_cache(self):
        self.cached_response = None

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def data(self):
        if self.response.content and self.status_code == 200:
            json_data = json.loads(self.response.content)
            return json_data.get('results')
        else:
            return HTTPError(self.status_code)

    @property
    def meta(self):
        if self.response.content and self.status_code == 200:
            json_data = json.loads(self.response.content)
            return json_data.get('metadata')
        else:
            return HTTPError(self.status_code)


class Genres(beatportAPI):
    def __init__(self, **kwargs):
        beatportAPI.__init__(self, **kwargs)


class Tracks(beatportAPI):
    def __init__(self, **kwargs):
        beatportAPI.__init__(self, **kwargs)


class Artists(beatportAPI):
    def __init__(self, **kwargs):
        beatportAPI.__init__(self, **kwargs)

    @property
    def images(self, **kwargs):
        """Returns dict of images: small, med, large"""
        return self.data[0]['images']

    @property
    def tracks(self, **kwargs):
        """Returns list of tracks by artist"""
        tracks = Tracks(**kwargs)
        return Tracks(artist_id=self.data[0]['id']).data


class Search(beatportAPI):
    def __init__(self, **kwargs):
        beatportAPI.__init__(self, **kwargs)

    @property
    def results(self):
        """Returns list of tracks matching query"""
        tracks = []
        for t in self.data:
            track = Tracks(id=t['id'])
            tracks.append(track.data[0])
        return tracks


if __name__ == '__main__':
    pass
