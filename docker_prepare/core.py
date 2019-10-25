class Core:
    @staticmethod
    def write_file(file_path, rendered_content):
        with open(file_path, "w") as text_file:
            text_file.write(rendered_content)
