import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content_list = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content_list),
        "linhas_do_arquivo": content_list,
    }

    if len(instance) > 0:
        for i in range(len(instance)):
            if (
                instance.search(i)["nome_do_arquivo"]
                == result["nome_do_arquivo"]
            ):
                return

    instance.enqueue(result)
    print(result)


def remove(instance):
    if len(instance) < 1:
        print("Não há elementos")
        return

    removed_file = instance.dequeue()

    print(f'Arquivo {removed_file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
