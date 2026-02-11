"""
Hospital Patient Queue Management System - Entry point.
Run this module to start the command-line application.
"""

# importing operations manager to handle the main application logic
from operationsManager import OperationsManager


# main function to initialize and run the operations manager
def main() -> None:
    """Start the queue management system."""
    manager = OperationsManager()
    manager.run()


if __name__ == "__main__":
    main()
