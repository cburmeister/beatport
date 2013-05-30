# Beatport API Client

This is a python wrapper around the Beatport.com API. I also added some
utility style properties becuase the Beatport API needs some work.

## Examples

    >>> import beatport

Fetch the deep house genre by ID:

    >>> g = beatport.Genres(id=12)
    >>> print g.data
    {u'slug': u'deep-house', u'subgenres': [], u'type': u'genre', u'id': 12, u'name': u'Deep House'}

Fetch an artist & one of their track names:

    >>> a = beatport.Artists(id=69549)
    >>> print a.data[0]['name']
    Dyed Soundorom
    >>> print a.tracks[1]['title']
    Had It Comin (Original Mix)

Fetch tracks by a particular Artist ID:

    >>> t = beatport.Tracks(artist_id=5112)
    >>> print t.data[0]['label']['name']
    Freerange Records

Query beatport and get a list of all relevant tracks:

    >>> s = beatport.Search(query='my money')
    >>> print s.results[0]['title']
    Prepared To Go (Original Mix)
