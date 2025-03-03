import datetime

from src.task import Task


def test_task_init(task) -> None:
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "20.02.2025"


def test_task_create():
    task = Task("Купить билеты", "Купить билеты на самолёт")
    assert task.name == "Купить билеты"
    assert task.description == "Купить билеты на самолёт"
    assert task.status == "Ожидает старта"
    assert task.created_at == datetime.datetime.now().date().strftime("%d.%m.%Y")


def test_task_update(capsys, task):
    task.created_at = "27.02.2024"
    message = capsys.readouterr()
    assert message.out.strip() == "Нельзя изменить дату создания на дату из прошлого."

    task.created_at = datetime.datetime.now().date().strftime("%d.%m.%Y")
    assert task.created_at == datetime.datetime.now().date().strftime("%d.%m.%Y")


def test_task_str(task):
    assert str(task) == "Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 20.02.2025"


def test_task_add(task_with_runtime1, task_with_runtime2):
    assert task_with_runtime1 + task_with_runtime2 == 130
