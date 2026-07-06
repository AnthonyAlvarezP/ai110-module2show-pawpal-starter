from pawpal_system import Task, Pet, Owner, Scheduler

# --- Tasks ---
walk = Task(description="Morning walk", time="15:30", frequency="daily")
feeding = Task(description="Feed breakfast", time="08:00", frequency="daily")
vet = Task(description="Vet checkup", time="07:00", frequency="once")
grooming = Task(description="Brush coat", time="6:00", frequency="weekly")

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
    tasks = scheduler.sort_by_time(scheduler.get_tasks_by_pet(pet.name))
    print(f"{pet.name} ({pet.breed})")
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"  {status} {task.time} — {task.description} [{task.frequency}]")
    print()

# --- Filter by Completion ---
print("=== Filter by Completion ===\n")
feeding.mark_complete()

all_tasks = scheduler.get_all_tasks()
pending  = scheduler.filter_by_status(all_tasks, completed=False)
done     = scheduler.filter_by_status(all_tasks, completed=True)

print("Pending:")
for task in pending:
    print(f"  ○ {task.time} — {task.description}")

print("\nCompleted:")
for task in done:
    print(f"  ✓ {task.time} — {task.description}")

print()

# --- Recurring Task Logic ---
print("=== Recurring Task Logic ===\n")
print(f"Before reschedule — Buddy's task count: {len(buddy.tasks)}")
print(f"Walk completed: {walk.completed}, due: {walk.due_date}\n")

scheduler.reschedule(walk, buddy)

print(f"After reschedule — Buddy's task count: {len(buddy.tasks)}")
print(f"Walk completed: {walk.completed}")
new_walk = buddy.tasks[-1]
print(f"New walk due: {new_walk.due_date} — {new_walk.description} [{new_walk.frequency}]")
print()

# --- Conflict Check ---
print("=== Conflict Check ===\n")
all_tasks = scheduler.get_all_tasks()
warning = scheduler.check_conflicts(all_tasks)
if warning:
    print(warning)
else:
    print("No conflicts found.")
