from datetime import date
from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete():
    task = Task(description="Walk dog", time="08:00", frequency="daily")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_task_count():
    pet = Pet(name="Buddy", age=3, weight=28.5, animal_type="dog", breed="Golden Retriever")
    assert len(pet.tasks) == 0
    pet.add_task(Task(description="Morning walk", time="07:30", frequency="daily"))
    assert len(pet.tasks) == 1
    pet.add_task(Task(description="Feed breakfast", time="08:00", frequency="daily"))
    assert len(pet.tasks) == 2


def test_check_conflicts_ignores_different_dates():
    owner = Owner(user_id="1", name="Alex", email="a@a.com")
    scheduler = Scheduler(owner)
    day1 = date(2026, 7, 6)
    day2 = date(2026, 7, 7)
    tasks = [
        Task(description="Walk", time="08:00", frequency="daily", due_date=day1),
        Task(description="Feed", time="08:00", frequency="weekly", due_date=day2),
    ]
    assert scheduler.check_conflicts(tasks) == ""


def test_remove_pet_missing_does_not_raise():
    owner = Owner(user_id="1", name="Alex", email="a@a.com")
    pet = Pet(name="Rex", age=2, weight=10.0, animal_type="dog", breed="Poodle")
    owner.remove_pet(pet)


def test_reschedule_idempotent():
    pet = Pet(name="Milo", age=1, weight=5.0, animal_type="cat", breed="Tabby")
    task = Task(description="Feed", time="07:00", frequency="daily", due_date=date(2026, 7, 6))
    pet.add_task(task)
    owner = Owner(user_id="1", name="Alex", email="a@a.com")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    scheduler.reschedule(task, pet)
    assert len(pet.tasks) == 2

    scheduler.reschedule(task, pet)
    assert len(pet.tasks) == 2


def test_sort_by_time_chronological():
    owner = Owner(user_id="1", name="Alex", email="a@a.com")
    scheduler = Scheduler(owner)
    tasks = [
        Task(description="Evening walk", time="18:00", frequency="daily"),
        Task(description="Feed breakfast", time="08:00", frequency="daily"),
        Task(description="Midnight med", time="00:00", frequency="daily"),
        Task(description="Noon check", time="12:00", frequency="daily"),
    ]
    sorted_tasks = scheduler.sort_by_time(tasks)
    times = [t.time for t in sorted_tasks]
    assert times == ["00:00", "08:00", "12:00", "18:00"]


def test_reschedule_daily_adds_next_day():
    today = date(2026, 7, 6)
    pet = Pet(name="Buddy", age=3, weight=28.5, animal_type="dog", breed="Golden Retriever")
    task = Task(description="Morning walk", time="07:30", frequency="daily", due_date=today)
    pet.add_task(task)
    owner = Owner(user_id="1", name="Alex", email="a@a.com")
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    scheduler.reschedule(task, pet)

    assert task.completed is True
    assert len(pet.tasks) == 2
    new_task = pet.tasks[1]
    assert new_task.due_date == date(2026, 7, 7)
    assert new_task.completed is False
    assert new_task.description == task.description


def test_check_conflicts_flags_same_time_same_date():
    today = date(2026, 7, 6)
    owner = Owner(user_id="1", name="Alex", email="a@a.com")
    scheduler = Scheduler(owner)
    tasks = [
        Task(description="Walk", time="08:00", frequency="daily", due_date=today),
        Task(description="Feed", time="08:00", frequency="daily", due_date=today),
    ]
    result = scheduler.check_conflicts(tasks)
    assert "08:00" in result
    assert "Walk" in result
    assert "Feed" in result
