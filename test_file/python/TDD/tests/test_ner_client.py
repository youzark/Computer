#!/usr/bin/env python
import unittest
from ner_client import NamedEntityClient

class TestNerClient(unittest.TestCase):
    def test_get_entity_returns_dictionary_given_empty_string(self):
        model = NerModelTestDouble()
        new_client  = NamedEntityClient()
        entities  = new_client.get_entities("")
        self.assertIsInstance(entities,dict)

    def test_get_entity_returns_list_given_nonempty_string(self):
        new_client  = NamedEntityClient()
        entities  = new_client.get_entities("Madison is a city in Wisconsin")
        self.assertIsInstance(entities,dict)


