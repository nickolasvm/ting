from ting_file_management.file_management import txt_importer

# from queue import Queue


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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# path = "statics/nome_pedro.txt"
# queue = Queue()

# process(path, queue)
