def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        element = instance.search(i)
        lines = element["linhas_do_arquivo"]
        occurences = []

        for line_index, line in enumerate(lines):
            if word.lower() in line.lower():
                occurences.append({"linha": line_index + 1})

        if occurences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": element["nome_do_arquivo"],
                    "ocorrencias": occurences,
                }
            )

    return result


# se a isntancia for maior q zero, prossiga
# faz um loop na instancia
# para cada elemento na instancia, seleciona linhas_do_arquivo
# faz um loop nas linhas do aruqivo
# para cada linha, verifica se existe a palavra
# se existir


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# [{
#   "palavra": "de",
#   "arquivo": "arquivo_teste.txt",
#   "ocorrencias": [
#     {
#       "linha": 2
#     },
#     {
#       "linha": 7
#     }
#   ]
# }]
