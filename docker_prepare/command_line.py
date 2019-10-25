import click


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
@click.pass_context
def main(ctx, *args, **kwargs):
    if ctx.invoked_subcommand is None:
        ctx.forward(generate)
