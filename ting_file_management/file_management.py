import sys


def txt_importer(path_file):
    _, extension = path_file.split(".")
    if extension != "txt":
        sys.stderr.write("Formato inválido")
        return

    try:
        with open(path_file, "r") as file:
            content = file.read().split("\n")
            return content

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
