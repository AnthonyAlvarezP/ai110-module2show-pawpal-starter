import importlib
import sys
from datetime import date
import streamlit as st

if "pawpal_system" in sys.modules:
    importlib.reload(sys.modules["pawpal_system"])

from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(user_id="u001", name="", email="")

scheduler = Scheduler(owner=st.session_state.owner)

st.title("🐾 PawPal+")

# --- Add a Pet ---
st.subheader("Add a Pet")

col1, col2 = st.columns(2)
with col1:
    pet_name = st.text_input("Pet name", value="")
    animal_type = st.text_input("Animal type", value="")
with col2:
    breed = st.text_input("Breed", value="")
    age = st.number_input("Age", min_value=0, max_value=30, value=2)
    weight = st.number_input("Weight (lbs)", min_value=0.1, max_value=300.0, value=20.0)

if st.button("Add Pet"):
    new_pet = Pet(name=pet_name, age=age, weight=weight, animal_type=animal_type, breed=breed)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"{pet_name} added!")

if st.session_state.owner.pets:
    st.markdown("**Current pets:**")
    st.table([
        {"Name": p.name, "Type": p.animal_type, "Breed": p.breed, "Age": p.age, "Weight (lbs)": p.weight}
        for p in st.session_state.owner.pets
    ])

st.divider()

# --- Schedule a Task ---
st.subheader("Schedule a Task")

pet_names = [p.name for p in st.session_state.owner.pets]

if not pet_names:
    st.info("Add a pet first before scheduling tasks.")
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_pet = st.selectbox("Assign to pet", pet_names)
    with col2:
        task_description = st.text_input("Task description", value="Morning walk")
        task_time = st.text_input("Time (HH:MM)", value="08:00")
    with col3:
        frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])

    if st.button("Add Task"):
        new_task = Task(description=task_description, time=task_time, frequency=frequency)
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet:
                pet.add_task(new_task)
                st.success(f"Task '{task_description}' added to {selected_pet}!")
                break

st.divider()

# --- Today's Schedule ---
st.subheader("Today's Schedule")

all_tasks = scheduler.get_all_tasks()

if not all_tasks:
    st.info("No tasks found. Add a pet and some tasks first.")
else:
    conflicts = scheduler.check_conflicts(all_tasks)
    if conflicts:
        for line in conflicts.split("\n"):
            st.warning(line)
    else:
        st.success("No scheduling conflicts detected.")

    status_filter = st.radio("Show tasks", ["All", "Pending", "Completed"], horizontal=True)

    for pet in st.session_state.owner.pets:
        tasks = scheduler.get_tasks_by_pet(pet.name)
        if not tasks:
            continue

        sorted_tasks = scheduler.sort_by_time([t for t in tasks if t.due_date == date.today()])

        if status_filter == "Pending":
            display_tasks = scheduler.filter_by_status(sorted_tasks, completed=False)
        elif status_filter == "Completed":
            display_tasks = scheduler.filter_by_status(sorted_tasks, completed=True)
        else:
            display_tasks = sorted_tasks

        if not display_tasks:
            continue

        st.markdown(f"#### {pet.name} — {pet.breed}")
        st.table([
            {
                "Time": t.time,
                "Task": t.description,
                "Frequency": t.frequency,
                "Due": str(t.due_date),
                "Status": "✅ Done" if t.completed else "⏳ Pending",
            }
            for t in display_tasks
        ])

        pending_recurring = [
            t for t in sorted_tasks
            if not t.completed and t.frequency in ("daily", "weekly")
        ]
        if pending_recurring:
            st.markdown("**Mark complete & reschedule:**")
            for i, task in enumerate(pending_recurring):
                label = f"{task.description} at {task.time} ({task.frequency})"
                if st.button(label, key=f"reschedule_{pet.name}_{i}"):
                    scheduler.reschedule(task, pet)
                    st.success(f"'{task.description}' marked done — next {task.frequency} occurrence added.")
                    st.rerun()
