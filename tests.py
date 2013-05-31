#!/usr/bin/env python

import unittest
import beatport


class BeatportTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_artist(self):
        """Should be able to fetch an artist by ID"""
        a = beatport.Artists(id=69549)
        name = a.data[0]['name']
        self.assertEqual(name, 'Dyed Soundorom')

    def test_get_artist_tracks(self):
        """Should be able to fetch an artists list of tracks"""
        a = beatport.Artists(id=69549)
        tracks = a.tracks
        self.assertEqual(type(tracks), list)

    def test_get_artist_images(self):
        """Should be able to fetch an artists dict of images"""
        a = beatport.Artists(id=69549)
        tracks = a.images
        self.assertEqual(type(tracks), dict)
        self.assertEqual(len(tracks), 3)

    def test_search(self):
        """Should be able to perform a search for list of tracks"""
        s = beatport.Search(query='my money')
        results = s.results
        self.assertEqual(type(results), list)


if __name__ == '__main__':
    unittest.main()
