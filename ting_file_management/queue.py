from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        result = self.__data.pop(0)
        return result

    def search(self, index):
        if len(self.__data) == 0 or index > len(self.__data) - 1 or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")

        result = self.__data[index]
        return result
