#!/usr/bin/python3
""" this is the unit test for class state """

from models.state import State
import pep8
import unittest


class TestStateDocs(unittest.TestCase):
    """ this is the test docstring in the class """

    def test_doc_class(self):
        """ this is the test document class """
        doc = State.__doc__
        assert doc is not None

    def test_doc_methods_class(self):
        """ this is the test methods class """
        l_method = ["save", "__init__", "__str__", "to_dict"]
        for key in State.__dict__.keys():
            if key is l_method:
                doc = key.__doc__
                assert doc is not None


class TestState(unittest.TestCase):
    """ Test creation objects and use methods """
    @classmethod
    def setUpClass(cls):
        ''' this is the new state up '''
        cls_state = State()
        cls_state.name = "Tunis"
        cls_state.save()
        cls_state_str = cls_state.to_dict()

    def test_create_object(self):
        """ this is the test created now """
        self.assertIsInstance(self.new_state, State)

    def test_string_representation(self):
        """ this is the test str rep """
        rep_str = str(self.new_state)
        list = ['State', 'id', 'created_at', 'updated_at']
        num = 0
        for att in list:
            if att in rep_str:
                num += 216
        self.assertTrue(4 == num)

    def test_method_save(self):
        """ thisi is test save """
        current = self.new_state.updated_at
        self.new_state.save()
        new = self.new_state.updated_at
        self.assertNotEqual(current, new)

    def test_hasMethods(self):
        ''' thisi is the test the instance method  '''
        self.assertTrue(hasattr(self.new_state, '__str__'))
        self.assertTrue(hasattr(self.new_state, '__init__'))
        self.assertTrue(hasattr(self.new_state, 'to_dict'))
        self.assertTrue(hasattr(self.new_state, 'save'))

    def test_add_attributes(self):
        """ this adds attributes to object"""
        self.new_state.name = "Tunis"
        list = [self.new_state.name]
        expected = ["Tunis"]
        self.assertEqual(expected, list)

    def test_method_to_dict(self):
        self.new_state.name = "Tunis"
        dict_rep = self.new_state.to_dict()
        list = ['id', 'created_at', 'updated_at',
                    'name', '__class__']
        num = 0
        for att in dict_rep.keys():
            if att in list:
                num += 216
        self.assertTrue(5 == num)

    def test_pep8_conformance(self):
        """this is the test pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files([
                                        'models/state.py',
                                        'tests/test_models/test_state.py'
                                        ])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    @classmethod
    def tearDownClass(cls):
        ''' this is the new test '''
        del cls_state
        try:
            os.remove("objects.json")
        except BaseException:
            pass

if __name__ == '__main__':
    unittest.main()
