import pytest

from src.task import Task
from src.task_iterator import TaskIterator
from src.user import User


@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=(
            Task("Купить огурцы", "Купить огурцы для салата", created_at="28.02.2025"),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="28.02.2025"),
        ),
    )


@pytest.fixture
def second_user():
    return User(
        username="John",
        email="john@mail.ru",
        first_name="John",
        last_name="Kint",
        task_list=(
            Task("Купить огурцы", "Купить огурцы для салата", created_at="28.02.2025"),
            Task("Купить лук", "Купить лук для салата", created_at="28.02.2025"),
            Task("Купить перец", "Купить перец для салата", created_at="28.02.2025"),
        ),
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="20.02.2025")


@pytest.fixture
def task_with_runtime1():
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="20.02.2025", run_time=60)


@pytest.fixture
def task_with_runtime2():
    return Task("Купить перец", "Купить перец для салата", created_at="20.02.2025", run_time=70)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)
