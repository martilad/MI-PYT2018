import click

@click.command()
@click.option('-c', '--count', type=int, default=0, metavar='COUNT', help='nevim.')
@click.option('-n', '--name', required = True, metavar='Name', help='nevim.')
#prompt co se vypise pro spusteni
@click.option('--color/--no-color', help='make colored output')
#@click.argument('color', type=click.Choice(['red', 'pink', 'blue']))
def main(count, name, color):
	if color:
		name = click.style(name, fg='blue')
	print (name)

@click.command()
@click.argument('src', type=click.File('r'))
@click.argument('dst')
def mv(src, dst):
	click.echo(f'moving {src} to  {dst}')
	print(src.read())

@click.group()
@click.option('-v', '-verbose')
def my_git():
	pass

@my_git.command()
def commit():
	click.edit("whats up")
	click.echo(f'commit {msg}')

@my_git.command()
@click.argument('files', nargs=-1, type=click.Path())
def add(files):
	for f in files:
		click.echo(f'add {f}')


if __name__ == '__main__':
	my_git()
