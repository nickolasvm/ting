import pytest

from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import process


def test_basic_priority_queueing():
    queue = PriorityQueue()

    process("statics/arquivo_teste_maior.txt", queue)
    assert len(queue.regular_priority) == 1

    process("statics/arquivo_teste.txt", queue)
    assert len(queue.high_priority) == 1

    queue.dequeue()
    assert len(queue.high_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(3)

    process("statics/arquivo_teste.txt", queue)
    assert queue.is_priority(queue.search(0))
