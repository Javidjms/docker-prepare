from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class Core:
    @staticmethod
    def render_docker_file(file_path, env_vars={}):
        file_name = Path(file_path).name
        parent_dir = Path(file_path).parent.absolute().as_posix()

        j2_env = Environment(
            loader=FileSystemLoader(parent_dir),
            trim_blocks=True,
        )
        rendered_docker_file = j2_env\
            .get_template(file_name)\
            .render(**env_vars)
        return rendered_docker_file

    @staticmethod
    def write_file(file_path, rendered_content):
        with open(file_path, "w") as text_file:
            text_file.write(rendered_content)
