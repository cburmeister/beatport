# Beatport API Client

This is a python wrapper around the Beatport.com API.

## Usage

### Setup

    >>> import beatport

### Examples

    >>> g = beatport.Genres(id=12)
    >>> print g.data
    {u'slug': u'deep-house', u'subgenres': [], u'type': u'genre', u'id': 12, u'name': u'Deep House'}

    >>> a = beatport.Artists(id=69549)
    >>> print a.data[0]['name']
    Dyed Soundorom

    >>> tracks = beatport.Tracks(artist_id=111537)
    >>> print tracks[7]['title']
    >>> print tracks.data[7]['title']
    Kik Me Up (Part 2 ) feat. Meital De-Razon (Original Mix)
