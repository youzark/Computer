#!/usr/bin/env python
import click

@click.command()
@click.argument("name")
@click.option('--number',type=int,help="message repeat time",default=1)
@click.option('--weather',type=click.Choice(['sunny','rainy','snowy']))
def main(name,number,weather):
    '''
    Help message
    '''
    for iter in range(number):
        print(f"Hello {name},today is {weather}!")

if __name__ == '__main__':
    main()

