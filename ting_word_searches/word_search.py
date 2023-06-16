def get_word_occurences(instance_element, word):
    lines = instance_element["linhas_do_arquivo"]
    occurences = []

    for line_index, line in enumerate(lines):
        if word.lower() in line.lower():
            occurences.append({"linha": line_index + 1, "conteudo": line})

    return occurences


def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        element = instance.search(i)
        occurences = get_word_occurences(element, word)

        if occurences:
            for occ in occurences:
                del occ["conteudo"]

            result.append(
                {
                    "palavra": word,
                    "arquivo": element["nome_do_arquivo"],
                    "ocorrencias": occurences,
                }
            )

    return result


def search_by_word(word, instance):
    result = []

    for i in range(len(instance)):
        element = instance.search(i)
        occurences = get_word_occurences(element, word)

        if occurences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": element["nome_do_arquivo"],
                    "ocorrencias": occurences,
                }
            )

    return result
