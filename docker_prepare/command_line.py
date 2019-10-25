import click
from .core import Core


@click.group(invoke_without_command=True)
@click.option(
    '-i',
    '--input',
    'input_docker_template_path',
    type=click.Path(exists=True),
    default='Dockertemplate',
)
@click.option(
    '-o',
    '--output',
    'output_docker_file_path',
    type=click.Path(),
    default='Dockerfile',
)
@click.option(
    '-e',
    '--env_file',
    'env_files',
    type=click.Path(exists=True),
    multiple=True,
)
@click.pass_context
def main(ctx, *args, **kwargs):
    if ctx.invoked_subcommand is None:
        ctx.forward(generate)


@main.command()
@click.option(
    '-i',
    '--input',
    'input_docker_template_path',
    type=click.Path(exists=True),
    default='Dockertemplate',
)
@click.option(
    '-o',
    '--output',
    'output_docker_file_path',
    type=click.Path(),
    default='Dockerfile',
)
@click.option(
    '-e',
    '--env_file',
    'env_files',
    type=click.Path(exists=True),
    multiple=True,
)
def generate(*args, **kwargs):
    Core.run(*args, **kwargs)


@main.command()
def sample():
    click.echo('sample')
