# Beatport API Client

This is a python wrapper around the Beatport.com API.

## Usage

### Setup

    >>> import beatport

### Examples

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
