#!/usr/bin/env python
import click

@click.group()
def cli():
    pass


@cli.group()
def lunch():
    pass

@cli.group()
def dinner():
    pass

@click.command()
def burger():
    print("enjoy your burger")

lunch.add_command(burger)
dinner.add_command(burger)

if __name__ == '__main__':
    cli()
