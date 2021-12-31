#!/usr/bin/env python
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

import click

words = ['youzark','hyx','white']
completer = WordCompleter(words)

styles = Style.from_dict(
        {
            "bottom-toolbar":"#333333 bg:#ffcc00"
            }
        )

def buttom_toolbar():
    toolbar_content = [
            ("class:bottom-toolbar","ctl-d or ctl-c to exit")
            ]
    return toolbar_content

session = PromptSession( completer = completer,
        bottom_toolbar = buttom_toolbar,
        style = styles
        )

@click.command()
@click.option("--party",help = 'Party file to load')
def main_loop():
    settings = {
            'party_file': party
            }
    while True:
        user_input = session.prompt("")
        print(f"you have enterd '{user_input}'")
