import unittest
from unittest import TestCase, mock, main
from functions_no_class import retrieve_value, retrieve_list, scale_ingredients, \
    filter_by_ingredients, ingredient_substitution, add_uservalue, like_a_recipe

class Test_DB_Retrieval(unittest.TestCase):
    def test_retrieve_value(self):
        expected = 4
        actual = retrieve_value("""SELECT id FROM recipe_id WHERE recipe = "Lemon Cake";""")
        self.assertEqual(expected, actual)

    def test_retrieve_list(self):
        expected = 5
        actual = len(retrieve_list(""" SELECT ingredient FROM ingredients WHERE recipe_id = 4; """))
        self.assertEqual(expected, actual)

class Test_Adding2DB(unittest.TestCase):
    def test_adding_new_user(self):
        expected = "Well done! You successfully made an account!"
        actual = add_uservalue()
        self.assertEqual(expected, actual)

class DB_Functions(unittest.TestCase):
    def test_scaling_ingredients(self):
        expected = 450.0
        actual = scale_ingredients()
        self.assertEqual(expected, actual)

    def test_if_liked_recipe(self):
       expected = "You have liked this recipe!"
       actual = like_a_recipe()
       self.assertEqual(expected, actual)
        
    def test_filter_by_ingredients(self):
        expected = 2
        actual = filter_by_ingredients()
        self.assertEqual(expected, actual)

    def test_ingredient_substituion(self):
        expected = 'tofu'
        actual = ingredient_substitution()
        self.assertEqual(expected, actual)

    def test_choose_diet_preference(self):
        pass

if __name__ == '__main__':
    unittest.main()
