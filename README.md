# Hospital Patient Queue Management System

A Python command-line application for managing patient queues in a hospital. It uses object-oriented programming (OOP) with three main classes: **Patient**, **Specialization**, and **OperationsManager**.

## Project Structure

- **main.py** – Application entry point; starts the menu-driven interface.
- **patient.py** – `Patient` class (name, patient_id, age, specialization, status).
- **specialization.py** – `Specialization` class; manages one queue per specialization.
- **operationsManager.py** – `OperationsManager` class; user interface and menu actions.
- **utility.py** – Helper functions for input handling.
- **readme.md** – This file.

## Classes

### Patient

Represents a single patient.

- **Attributes:** `name`, `patient_id`, `age`, `specialization`, `status`
- **Status values:** `0` = normal, `1` = urgent, `2` = super-urgent
- **Methods:** `get_status_str()`, `__str__`, `__repr__`

### Specialization

Manages the queue for one medical specialization (e.g. General, Cardiology).

- Add patients (ordered by urgency: super-urgent → urgent → normal).
- Get next patient (highest priority).
- Remove patient by name.
- Check capacity (default queue capacity: 10).

### OperationsManager

Provides the text menu and coordinates actions with specializations.

- Add new patients to a specialization.
- List patients in a specialization.
- Get next patient from a specialization.
- Remove a patient by name.
- Exit the program.

## How to Run

From the project directory:

```bash
python main.py
```

Then use the menu (1–5) to add patients, list queues, get next patient, remove a patient, or exit.

## Requirements

- Python 3.8 or later.
