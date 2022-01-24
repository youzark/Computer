#!/usr/bin/env python

import click
from attr import attrs, attrib
import toml

@attrs
class Character:
    name = attrib(default='hyx')
    level = attrib(default=1)

def load_party(party_file):
    with open(party_file, 'r') as fin:
        party = toml.load(fin)
        return {x["name"]: Character(**x) for x in party.values()}


