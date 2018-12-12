"""
Unit test for swapi_people
"""

import swapi_people as sp

class TestSwapi:
    
    url = "https://swapi.co/api/people/?format=json"
    
    def test_get_list(self):
        assert "luke skywalker" == sp.prep_name(['luke', 'skywalker'])

    def test_list_characters(self):
        assert 1 == sp.list_characters(self.url)['code']

    def test_get_character(self):
        assert 0 == sp.get_character("luke skywalker", self.url)['code']

    def test_bad_name(self):
        assert 2 == sp.get_character("James T. Kirk", self.url)['code']

    def api_unavailable(self):
        assert 3 == sp.get_character("luke skywalker", "https://swapi.co/apii/people/?format=jason")['code']
