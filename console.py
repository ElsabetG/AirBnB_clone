#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""
import cmd
import json
import re
import models
# from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '

    def my_errors(self, line, num_of_args):
        """Displays error messages to user

        Args:
        line(any): gets user input using command line
        num_of_args(int): number of input arguments

        Description:
        Displays output to the use based on
        the input commands.

        """
        classes = ["BaseModel", "User", "State", "City",
