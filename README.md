# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

=== Today's Schedule ===

Buddy (Golden Retriever)
  ○ 07:30 — Morning walk [daily]
  ○ 08:00 — Feed breakfast [daily]
  ○ 15:00 — Vet checkup [once]

Whiskers (Siamese)
  ○ 18:00 — Brush coat [weekly]

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:
====================================================== test session starts ======================================================
platform win32 -- Python 3.14.0, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\antho\OneDrive\Desktop\AI110\Projects\ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 8 items                                                                                                                

tests\test_pawpal.py ........                                                                                              [100%]

======================================================= 8 passed in 0.05s =======================================================
```
# Paste your pytest output here
```
====================================================== test session starts ======================================================
platform win32 -- Python 3.14.0, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\antho\OneDrive\Desktop\AI110\Projects\ai110-module2show-pawpal-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\antho\OneDrive\Desktop\AI110\Projects\ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 8 items                                                                                                                

tests/test_pawpal.py::test_mark_complete PASSED                                                                            [ 12%]
tests/test_pawpal.py::test_task_count PASSED                                                                               [ 25%]
tests/test_pawpal.py::test_check_conflicts_ignores_different_dates PASSED                                                  [ 37%]
tests/test_pawpal.py::test_remove_pet_missing_does_not_raise PASSED                                                        [ 50%]
tests/test_pawpal.py::test_reschedule_idempotent PASSED                                                                    [ 62%]
tests/test_pawpal.py::test_sort_by_time_chronological PASSED                                                               [ 75%]
tests/test_pawpal.py::test_reschedule_daily_adds_next_day PASSED                                                           [ 87%]
tests/test_pawpal.py::test_check_conflicts_flags_same_time_same_date PASSED                                                [100%]

======================================================= 8 passed in 0.06s =======================================================

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.
=== Today's Schedule ===

Buddy (Golden Retriever)
  ○ 07:00 — Vet checkup [once]
  ○ 08:00 — Feed breakfast [daily]
  ○ 15:30 — Morning walk [daily]

Whiskers (Siamese)
  ○ 6:00 — Brush coat [weekly]

=== Filter by Completion ===

Pending:
  ○ 15:30 — Morning walk
  ○ 07:00 — Vet checkup
  ○ 6:00 — Brush coat

Completed:
  ✓ 08:00 — Feed breakfast

=== Recurring Task Logic ===

Before reschedule — Buddy's task count: 3
Walk completed: False, due: 2026-07-06

After reschedule — Buddy's task count: 4
Walk completed: True
New walk due: 2026-07-07 — Morning walk [daily]

=== Conflict Check ===

⚠️ Conflict at 15:30: Morning walk, Morning walk
## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. This is a pet care app that allows users to create special schedules for their pets.
2. Start by adding your pets in the "add pet" section
3. Then, add the tasks 
4. Lastly, the app with take the infomation and generate a schedule that automaticly filters and sorts the task depending on the time.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
