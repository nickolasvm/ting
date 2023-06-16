import pytest

from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import process


def test_basic_priority_queueing():
    queue = PriorityQueue()

    # test if file with 5 lines or more queue in regular priority
    process("statics/arquivo_teste_maior.txt", queue)
    assert len(queue.regular_priority) == 1
    assert not queue.is_priority(queue.search(0))

    # test if file with less than 5 lines queue in high priority
    process("statics/arquivo_teste.txt", queue)
    assert len(queue.high_priority) == 1
    assert queue.is_priority(queue.search(0))

    # test if dequeue remove the priority file first
    queue.dequeue()
    assert len(queue.high_priority) == 0

    # test if search with a index that does not exist, it throws an error
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(3)
