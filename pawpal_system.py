from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str        # HH:MM format
    frequency: str   # "daily", "weekly", "once"
    completed: bool = False

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
