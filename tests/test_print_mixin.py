from src.deadline_task import DeadlineTask
from src.periodic_task import PeriodicTask
from src.task import Task


def test_print_mixin(capsys, task, task_periodic1, task_deadline1):
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[0]
        == "Task(Купить огурцы, Купить огурцы для салата, Ожидает старта, 20.02.2025)"
    )
    assert (
        message.out.strip().split("\n")[1]
        == "PeriodicTask(Купить огурцы, Купить огурцы для салата, Ожидает старта, 20.02.2025)"
    )
    assert (
        message.out.strip().split("\n")[2]
        == "DeadlineTask(Купить перец, Купить перец для салата, Ожидает старта, 20.02.2025)"
    )
