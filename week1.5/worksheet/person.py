# Worksheet 1.5: Person class

from datetime import date
from datetime import datetime

class Person:
    """A person with a name and a date of birth."""

    def __init__(self, name: str, birth: date):
        """Initialize a Person with a name and birth date.

        Args:
            name: The person's name (must be a non-empty string).
            birth: The person's date of birth (must be a date object).

        Raises:
            TypeError: If name is not a str or birth is not a date.
            ValueError: If name is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a str")
        if len(name) == 0:
            raise ValueError("name must not be empty")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date object")
        self.name = name
        self.birth = birth

    def initials(self) -> str:
        """Return the uppercased initial letters of each part of the name.

        For example, 'Alan John Smith' returns 'AJS'.
        """
        return ''.join(word[0].upper() for word in self.name.split())

    def is_birthday(self) -> bool:
        """Return True if today is the person's birthday, False otherwise."""
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day


    # Write a constructor here to create and initialize name and

    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
