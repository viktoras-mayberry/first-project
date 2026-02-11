"""
Specialization class for the Hospital Patient Queue Management System.
Manages patient queues within a single medical specialization.
"""
from __future__ import annotations

from patient import Patient


class Specialization:
    """Manages a queue of patients for one medical specialization."""

    def __init__(self, name: str, capacity: int = 10):
        """
        Initialize a specialization queue.

        Args:
            name: Name of the specialization (e.g. "Cardiology", "General").
            capacity: Maximum number of patients in the queue. Default 10.
        """
        self.name = name
        self.capacity = capacity
        self._queue: list[Patient] = []

    def _insert_by_priority(self, patient: Patient) -> None:
        """Insert patient so queue stays ordered by status (super-urgent, urgent, normal)."""
        for i, p in enumerate(self._queue):
            if patient.status > p.status:
                self._queue.insert(i, patient)
                return
        self._queue.append(patient)

    def add_patient(self, patient: Patient) -> bool:
        """
        Add a patient to the queue. Ordered by urgency (2 > 1 > 0).

        Returns:
            True if added, False if queue is at capacity.
        """
        if not self.has_capacity():
            return False
        self._insert_by_priority(patient)
        return True

    def get_next_patient(self) -> Patient | None:
        """
        Retrieve and remove the next patient (highest priority).

        Returns:
            The next patient, or None if queue is empty.
        """
        if not self._queue:
            return None
        return self._queue.pop(0)

    def remove_patient_by_name(self, name: str) -> bool:
        """
        Remove the first patient matching the given name (case-insensitive).

        Returns:
            True if a patient was removed, False otherwise.
        """
        name_lower = name.strip().lower()
        for i, p in enumerate(self._queue):
            if p.name.lower() == name_lower:
                self._queue.pop(i)
                return True
        return False

    def has_capacity(self) -> bool:
        """Return True if the queue can accept more patients."""
        return len(self._queue) < self.capacity

    def is_empty(self) -> bool:
        """Return True if the queue has no patients."""
        return len(self._queue) == 0

    def get_patients(self) -> list[Patient]:
        """Return a copy of the current queue (in order)."""
        return list(self._queue)

    def __len__(self) -> int:
        return len(self._queue)
