import click
from .core import Core


@click.group(invoke_without_command=True)
@click.option(
    '-i',
    '--input',
    'input_docker_template_path',
    type=click.Path(exists=True),
    default='Dockertemplate',
    help='path of the Dockertemplate',
)
@click.option(
    '-o',
    '--output',
    'output_docker_file_path',
    type=click.Path(),
    default='Dockerfile',
    help='path of the Dockerfile',
)
@click.option(
    '-e',
    '--env',
    'env_vars',
    multiple=True,
    help='environment variable (key=value)',
)
@click.option(
    '-ef',
    '--env_file',
    'env_files',
    type=click.Path(exists=True),
    multiple=True,
    help='path of the .env file',
)
@click.option(
    '-v',
    '--verbose',
    is_flag=True,
    help='Enables verbose mode',
)
@click.pass_context
def main(ctx, *args, **kwargs):
    """
    This script generate a Dockerfile from Dockertemplate (jinja template).
    """
    if ctx.invoked_subcommand is None:
        ctx.forward(generate)


@main.command()
@click.option(
    '-i',
    '--input',
    'input_docker_template_path',
    type=click.Path(exists=True),
    default='Dockertemplate',
    help='path of the Dockertemplate',
)
@click.option(
    '-o',
    '--output',
    'output_docker_file_path',
    type=click.Path(),
    default='Dockerfile',
    help='path of the Dockerfile',
)
@click.option(
    '-e',
    '--env',
    'env_vars',
    multiple=True,
    help='environment variable (key=value)',
)
@click.option(
    '-ef',
    '--env_file',
    'env_files',
    type=click.Path(exists=True),
    multiple=True,
    help='path of the .env file',
)
@click.option(
    '-v',
    '--verbose',
    is_flag=True,
    help='Enables verbose mode',
)
def generate(*args, **kwargs):
    """
    This script generate a Dockerfile from Dockertemplate (jinja template).
    """
    Core.run(*args, **kwargs)


@main.command()
def sample():
    """
    This script generate a sample Dockertemplate.
    """
    click.echo('Not Implemented Yet')
