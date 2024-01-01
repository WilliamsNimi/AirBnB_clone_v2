#!/usr/bin/python3
""" Test file for console """
import unittest
import datetime
import console
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
import json
import os


class TestConsole(unittest.TestCase):
    """ Test for HBNBCommand Class """

    def setUp(self):
        """ The setUp function """
        self.model1 = HBNBCommand()

    def test_do_quit(self):
        """This function tests the do_quit method of the console"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("quit")
            self.assertEqual("", file.getvalue())

    def test_create(self):
        """Tests the create method"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("create")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("create ruler")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())

    def test_show(self):
        """Tests the show method"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("show")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("show farell")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("show BaseModel astrid-456")
            self.assertEqual("** no instance found **\n", file.getvalue())

    def test_destroy(self):
        """Tests the destroy method"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("destroy")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("destroy astrid")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("destroy BaseModel 4567")
            self.assertEqual("** no instance found **\n", file.getvalue())

    def test_all(self):
        """ Test the all method """
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("all heisenberg")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("all Review")
            self.assertEqual("[]\n", file.getvalue())

    def test_update(self):
        """ This the update method"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("update")
            self.assertEqual("** class name missing **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("update astrid")
            self.assertEqual("** class doesn't exist **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("update Review")
            self.assertEqual("** instance id missing **\n", file.getvalue())
        with patch('sys.stdout', new=StringIO()) as file:
            self.model1.onecmd("update Review 5678")
            self.assertEqual("** no instance found **\n", file.getvalue())

    def tearDown(self):
        """ Tear down function to destroy the model instance"""
        del self.model1


if __name__ == "__main__":
    unittest.main()
