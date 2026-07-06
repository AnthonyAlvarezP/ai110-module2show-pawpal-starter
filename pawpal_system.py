from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List


@dataclass
class Task:
    description: str
    time: str        # HH:MM format
    frequency: str   # "daily", "weekly", "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    age: int
    weight: float
    animal_type: str
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)


@dataclass
class Owner:
    user_id: str
    name: str
    email: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner's pet list."""
        self.pets.remove(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across every pet owned."""
        return [task for pet in self.pets for task in pet.tasks]


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the scheduler with an owner."""
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all of the owner's pets."""
        return self.owner.get_all_tasks()

    def get_tasks_by_pet(self, pet_name: str) -> List[Task]:
        """Return tasks for the pet matching the given name, or an empty list."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                return pet.tasks
        return []

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Return tasks sorted in chronological order by time."""
        return sorted(tasks, key=lambda task: tuple(int(x) for x in task.time.split(":")))

    def filter_by_status(self, tasks: List[Task], completed: bool) -> List[Task]:
        """Return tasks matching the given completion status."""
        return [task for task in tasks if task.completed == completed]

    def check_conflicts(self, tasks: List[Task]) -> str:
        """Return a warning message listing any time slots with overlapping tasks, or empty string if none."""
        seen = {}
        for task in tasks:
            if task.time in seen:
                seen[task.time].append(task.description)
            else:
                seen[task.time] = [task.description]
        warnings = [
            f"⚠️ Conflict at {time}: {', '.join(names)}"
            for time, names in seen.items()
            if len(names) > 1
        ]
        return "\n".join(warnings)

    def reschedule(self, task: Task, pet: Pet) -> None:
        """Mark a recurring task complete and add a new instance for the next occurrence."""
        task.mark_complete()
        if task.frequency == "daily":
            next_date = task.due_date + timedelta(days=1)
        elif task.frequency == "weekly":
            next_date = task.due_date + timedelta(weeks=1)
        else:
            return
        new_task = Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            due_date=next_date,
        )
        pet.add_task(new_task)
