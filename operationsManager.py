"""
OperationsManager class for the Hospital Patient Queue Management System.
User interface for interacting with Specialization instances.
"""

from patient import Patient
from specialization import Specialization
from utility import get_int_input, get_choice


class OperationsManager:
    """Manages specializations and provides the main menu and actions."""

    def __init__(self):
        """Initialize with a default set of specializations."""
        self.specializations: dict[str, Specialization] = {}
        self._ensure_specializations()

    def _ensure_specializations(self) -> None:
        """Ensure at least the common specializations exist."""
        defaults = [
            "General",
            "Cardiology",
            "Neurology",
            "Orthopedics",
            "Pediatrics",
            "Emergency",
        ]
        for name in defaults:
            if name not in self.specializations:
                self.specializations[name] = Specialization(name)

    def get_or_create_specialization(self, name: str) -> Specialization:
        """Get existing specialization by name or create a new one."""
        name = name.strip()
        if name not in self.specializations:
            self.specializations[name] = Specialization(name)
        return self.specializations[name]

    def add_patient(self) -> None:
        """Add a new patient to a specialization via user input."""
        name = input("Enter patient name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        patient_id = input("Enter patient ID: ").strip()
        if not patient_id:
            print("Patient ID cannot be empty.")
            return
        age = get_int_input("Enter age: ")
        if age < 0 or age > 150:
            print("Invalid age.")
            return
        spec_name = input("Enter specialization: ").strip()
        if not spec_name:
            print("Specialization cannot be empty.")
            return
        print("Status: 0 = normal, 1 = urgent, 2 = super urgent")
        status = get_int_input("Enter status (0/1/2): ", default=0)
        if status not in (0, 1, 2):
            status = 0

        spec = self.get_or_create_specialization(spec_name)
        patient = Patient(name, patient_id, age, spec_name, status)
        if spec.add_patient(patient):
            print(f"Patient {name} added to {spec_name} queue.")
        else:
            print(f"Cannot add patient: {spec_name} queue is full (capacity {spec.capacity}).")

    def list_patients(self) -> None:
        """List all patients in a specialization."""
        spec_name = input("Enter specialization name: ").strip()
        if not spec_name:
            print("Specialization name cannot be empty.")
            return
        spec = self.specializations.get(spec_name)
        if spec is None:
            print(f"No specialization named '{spec_name}'.")
            return
        patients = spec.get_patients()
        if not patients:
            print(f"No patients in {spec_name}.")
            return
        print(f"\nPatients in {spec_name}:")
        for i, p in enumerate(patients, 1):
            print(f"  {i}. {p}")
        print()

    def get_next_patient(self) -> None:
        """Retrieve and display the next patient from a specialization."""
        spec_name = input("Enter specialization name: ").strip()
        if not spec_name:
            print("Specialization name cannot be empty.")
            return
        spec = self.specializations.get(spec_name)
        if spec is None:
            print(f"No specialization named '{spec_name}'.")
            return
        patient = spec.get_next_patient()
        if patient is None:
            print(f"No patients in {spec_name} queue.")
            return
        print(f"Next patient: {patient}")

    def remove_patient(self) -> None:
        """Remove a patient by name from a specialization."""
        spec_name = input("Enter specialization name: ").strip()
        if not spec_name:
            print("Specialization name cannot be empty.")
            return
        spec = self.specializations.get(spec_name)
        if spec is None:
            print(f"No specialization named '{spec_name}'.")
            return
        name = input("Enter patient name to remove: ").strip()
        if not name:
            print("Patient name cannot be empty.")
            return
        if spec.remove_patient_by_name(name):
            print(f"Patient '{name}' removed from {spec_name}.")
        else:
            print(f"Patient '{name}' not found in {spec_name}.")

    def run(self) -> None:
        """Run the main menu loop until the user exits."""
        print("Hospital Patient Queue Management System")
        print("----------------------------------------")
        while True:
            print("\n1. Add patient")
            print("2. List patients in specialization")
            print("3. Get next patient")
            print("4. Remove patient")
            print("5. Exit")
            choice = get_choice("Choice (1-5): ", valid={"1", "2", "3", "4", "5"})
            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.list_patients()
            elif choice == "3":
                self.get_next_patient()
            elif choice == "4":
                self.remove_patient()
            else:
                print("Goodbye.")
                break
