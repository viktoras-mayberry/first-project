"""
Patient class for the Hospital Patient Queue Management System.
Represents an individual patient with attributes and status formatting.
"""


class Patient:
    """Represents a patient in the hospital queue."""

    STATUS_NORMAL = 0
    STATUS_URGENT = 1
    STATUS_SUPER_URGENT = 2

    def __init__(self, name: str, patient_id: str, age: int, specialization: str, status: int = 0):
        """
        Initialize a Patient.

        Args:
            name: Full name of the patient.
            patient_id: Unique identifier for the patient.
            age: Age of the patient.
            specialization: Medical specialization the patient is assigned to.
            status: 0 (normal), 1 (urgent), or 2 (super-urgent). Defaults to 0.
        """
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.specialization = specialization
        self.status = status if status in (0, 1, 2) else 0

    def get_status_str(self) -> str:
        """Return a human-readable string for the patient's status."""
        if self.status == self.STATUS_SUPER_URGENT:
            return "super urgent"
        if self.status == self.STATUS_URGENT:
            return "urgent"
        return "normal"

    def __str__(self) -> str:
        """String representation of the patient."""
        return f"{self.name} (ID: {self.patient_id}, Age: {self.age}, Status: {self.get_status_str()})"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Patient(name={self.name!r}, patient_id={self.patient_id!r}, status={self.status})"
