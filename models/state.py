#!/usr/bin/python3
"""Defines the State class."""

from models.base_model import BaseModel
class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

        """Update sorting error"""
    def to_dict(self):
        """Return a dictionary representation of the State instance.

        Includes the key/value pair '__class__' representing
        the class name of the object.
        """
        result_dict = super().to_dict()
        result_dict['name'] = self.name
        return result_dict
