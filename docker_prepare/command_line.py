import click


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx, *args, **kwargs):
    if ctx.invoked_subcommand is None:
        ctx.forward(generate)
