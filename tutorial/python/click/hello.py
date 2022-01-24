import click

class Config(object):
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config,ensure = True)




@click.group()
@click.option("--verbose", is_flag=True)
@click.option("--home-directory", type = click.Path())
@pass_config
def cli(config,verbose,home_directory):
    config.verbose = verbose
    config.home_directory =  home_directory



@cli.command()
@click.option("--name",default="hyx",
        help = "the name you want to greet")
@click.option("--repeat",default=1,
        help = "the number of times to repeat")
@click.argument("save_file", type=click.File('w'),
        required=False)
@pass_config
def greet(config,name,repeat,save_file):
    ''' this scripts greets you '''
    click.echo(save_file)
    if config.verbose:
        click.echo("We are in verbose mode")
    click.echo(f"home dir is {config.home_directory}")
    for iter in range(repeat):
        click.echo(f"Hello {name}",file=save_file)
