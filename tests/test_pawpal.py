from pawpal_system import Task, Pet


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
