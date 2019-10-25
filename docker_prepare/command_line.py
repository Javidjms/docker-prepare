import click


@click.group(invoke_without_command=True)
@click.option(
    '-i',
    '--input',
    'input_docker_template_path',
    type=click.Path(exists=True),
    default='Dockertemplate',
)
@click.pass_context
def main(ctx, *args, **kwargs):
    if ctx.invoked_subcommand is None:
        ctx.forward(generate)
