import pytest

from src.deadline_task import DeadlineTask
from src.periodic_task import PeriodicTask
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
            Task("Купить огурцы", "Купить огурцы для салата", created_at="28.02.2025", run_time=40),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="28.02.2025", run_time=60),
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
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="20.02.2025", run_time=60)


@pytest.fixture
def task_with_runtime1():
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="20.02.2025", run_time=60)


@pytest.fixture
def task_with_runtime2():
    return Task("Купить перец", "Купить перец для салата", created_at="20.02.2025", run_time=70)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)


@pytest.fixture
def task_periodic1():
    return PeriodicTask(
        "Купить огурцы", "Купить огурцы для салата", "01.04.2024", "01.05.2024", run_time=60, created_at="20.02.2025"
    )


@pytest.fixture
def task_periodic2():
    return PeriodicTask(
        "Купить помидоры",
        "Купить помидоры для салата",
        "01.04.2024",
        "01.05.2024",
        run_time=40,
        created_at="20.02.2025",
    )


@pytest.fixture
def task_deadline1():
    return DeadlineTask("Купить перец", "Купить перец для салата", "20.04.2024", run_time=60, created_at="20.02.2025")


@pytest.fixture
def task_deadline2():
    return DeadlineTask("Купить лук", "Купить лук для салата", "20.04.2024", run_time=60, created_at="20.02.2025")


@pytest.fixture
def user_without_tasks():
    return User("Some", "some@mail.ru", "Some", "User")
