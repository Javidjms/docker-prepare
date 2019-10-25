from dotenv import dotenv_values
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class Core:
    @staticmethod
    def run(*args, **kwargs):
        env_files = kwargs.get('env_files')
        input_docker_template_path = kwargs.get('input_docker_template_path')
        output_docker_file_path = kwargs.get('output_docker_file_path')
        env_vars = Core.get_environment_variables(env_files)
        rendered_docker_file = Core.render_docker_file(
            input_docker_template_path,
            env_vars,
        )
        Core.write_file(
            output_docker_file_path,
            rendered_docker_file,
        )

    @staticmethod
    def get_environment_variables(env_files):
        env_vars = {}
        for env_file in env_files:
            env_path = Path(env_file)
            env_values = dotenv_values(dotenv_path=env_path)
            env_vars.update(env_values)
        return env_vars

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
