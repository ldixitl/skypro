import pytest

from src.task import Task
from src.user import User


@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=(
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
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
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить лук", "Купить лук для салата"),
            Task("Купить перец", "Купить перец для салата"),
        ),
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="20.02.2025")
