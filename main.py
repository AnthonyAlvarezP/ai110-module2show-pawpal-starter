from pawpal_system import Task, Pet, Owner, Scheduler

# --- Tasks ---
walk = Task(description="Morning walk", time="07:30", frequency="daily")
feeding = Task(description="Feed breakfast", time="08:00", frequency="daily")
vet = Task(description="Vet checkup", time="15:00", frequency="once")
grooming = Task(description="Brush coat", time="18:00", frequency="weekly")

# --- Pets ---
buddy = Pet(name="Buddy", age=3, weight=28.5, animal_type="dog", breed="Golden Retriever")
buddy.add_task(walk)
buddy.add_task(feeding)
buddy.add_task(vet)

whiskers = Pet(name="Whiskers", age=5, weight=4.2, animal_type="cat", breed="Siamese")
whiskers.add_task(grooming)

# --- Owner ---
owner = Owner(user_id="u001", name="Jordan", email="jordan@email.com")
owner.add_pet(buddy)
owner.add_pet(whiskers)

# --- Scheduler ---
scheduler = Scheduler(owner=owner)

# --- Print Today's Schedule ---
print("=== Today's Schedule ===\n")
for pet in owner.pets:
    tasks = scheduler.get_tasks_by_pet(pet.name)
    print(f"{pet.name} ({pet.breed})")
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"  {status} {task.time} — {task.description} [{task.frequency}]")
    print()
