import mysql.connector
from collections import Counter
from config import HOST, USER, PASSWORD

def _connect_to_db():
    # try:
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database= 'what2eat',
    )

    return connection

class Retrieve_db_data:

    def retrieve_value(query):
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        cur.execute(query)
        result = cur.fetchall()

# this tidies up the data being recieved from the DB
        result = [item for entry in result for item in entry][0]

        return result

    def retrieve_list(query):
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        cur.execute(query)
        result = cur.fetchall()

        # this tidies up the data being recieved from the DB -> removing unnecessary punctuation
        result = [item for entry in result for item in entry]

        return result

class Add2DB:
# general functions to add data to the DB for recursion and to make following functions easier and reduce repetition
    def general_add2DB(query):
        try:
            db_connection = _connect_to_db()
            cur = db_connection.cursor()

            cur.execute(query)
            db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
            cur.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            db_connection.close()
            print("DB connection is closed")

# specific function to add new users to the recipe_app
    def add_uservalue():
        all_users = Retrieve_db_data.retrieve_list(""" SELECT email FROM users;""")
        u_email = input("Enter email:")
        u_username = input("Enter users:")


        for user in all_users:
            if user != u_email:
                Add2DB.general_add2DB(
                    """ INSERT INTO users (email, username) VALUES ( "{}", "{}")""".format(u_email, u_username))
                return ("Well done! You successfully made an account!")

            else:
                return ("This email address already has an account!")

# specific functions for users to add recipes to the DB
# needs seperate function to ensure all information about the recipe is added to the respective tables in the DB
    def add_recipe():
        recipe_name = input("Enter recipe name:")
        serving = int(input("Enter serving size: "))
        recipe_prep_time = int(input("Enter prep time in minutes:"))
        recipe_cook_time = int(input("Enter cooking time in minutes:"))


        ### add recipe type/course to DB
        course_id = int(input("Enter what course your recipe is (1 - 6) "
                              "\n 1 - Breakfast "
                              "\n 2 - Lunch "
                              "\n 3 - Snack "
                              "\n 4 - Appetiser "
                              "\n 5 - Dinner "
                              "\n 6 - Dessert "
                              "\n Add course here: "))

        try:
            if course_id < 1 or course_id > 6:
                raise Exception

        except:
            print("Your number was not in the requestion range")

        Add2DB.general_add2DB(
            """ INSERT INTO recipe_id (r_name, prep_time, cook_time, serving, course_id) VALUES ("{}", {}, {}, {}, {})"""
            .format(recipe_name, recipe_prep_time, recipe_cook_time, serving, course_id))

        recipe_id = Retrieve_db_data.retrieve_value(""" SELECT id FROM recipe_id WHERE r_name = "{}" """. format(recipe_name))
        print(recipe_id)

        ### get ingredients and quantity for recipe and add to DB
        n = int(input("Enter number of ingredients: "))
        for i in range(n):
            ingredients = input("Enter ingredient :")
            quantity = input("Enter ingredient quantity:")
            measurement = input("Enter unit of measurement")
            Add2DB.general_add2DB(""" INSERT INTO ingredients (recipe_id, Ingredient, Quantity, Unit) VALUES ("{}", "{}", "{}", "{}");""".format(recipe_id, ingredients, quantity, measurement))


        ### get recipe steps and actions and add to DB
        n = int(input("Enter number of steps in recipe: "))
        for i in range(n):
            step = input("Enter step number: ")
            action = input("Enter step method: ")
            Add2DB.general_add2DB(""" INSERT INTO steps (recipe_id, step_order, cooking_action) VALUES ({}, {}, "{}"); """.format(recipe_id, step, action))

class User_Functions(Retrieve_db_data, Add2DB):
    # this function allows users to scale up or down recipes
    # i.e. if a recipe serves only two and they want it to serve 6
    # this recipes shows how much of each ingredient they would need for those 4 more people
    def scale_ingredients():

        recipe = input("What recipe would you like to scale up?")

        all_recipes = Retrieve_db_data.retrieve_list(""" SELECT r_name FROM recipe_id""")
        for x in all_recipes:
            if x == recipe:

                id = Retrieve_db_data.retrieve_value("""SELECT id FROM recipe_id WHERE r_name = "{}";""".format(recipe))
                ingredients = Retrieve_db_data.retrieve_list( """ SELECT Ingredient FROM ingredients WHERE recipe_id = {}; """.format(id))
                quantity = Retrieve_db_data.retrieve_list( """ SELECT Quantity FROM ingredients WHERE recipe_id = {} """.format(id))
                serving = Retrieve_db_data.retrieve_value( """SELECT serving FROM recipe_id WHERE id = {}; """.format(id))

                # changing ingredients and quantity for a recipe from database into a dictionary for use in scale_ingredients function

                ingredients_dict = dict(zip(ingredients, quantity))
                print(ingredients_dict)

                to_serve = int(input("How many do you want this recipe to serve?"))

                for value in ingredients_dict:
                    serve_one = ingredients_dict[value] / serving
                    adjusted_serving = serve_one * to_serve

                for value in ingredients_dict:
                    ingredients_dict[value] *= adjusted_serving

                return ("Here are the adjusted ingredients list {}" .format(ingredients_dict))

        else:

            return ("Invalid recipe! This recipe is not in the database")

    # this function filters all the recipes in the database depending on their dietary preferences
    def chooseyourdiet():
        diet = input(" Enter your diet preference (1 - 4) \n 1.Vegetarian \n 2.Vegan \n 3.Gluten Free \n 4.Lactose Free \n Add preference here: ")

        if diet == "1":

            all_recipes = Retrieve_db_data.retrieve_list(""" SELECT r_name FROM recipe_id""")

            recipes = []
            for recipe in all_recipes:
                    diet = str(Retrieve_db_data.retrieve_value(
                        """ SELECT Diet FROM recipe_id WHERE r_name = "{}";""".format(recipe)))
                    if diet.find("Vegetarian") == 0:
                        recipes.append(recipe)

            return ("These recipes {} are vegetarian".format(recipes))


        elif diet == "2":
            all_recipes = Retrieve_db_data.retrieve_list(""" SELECT r_name FROM recipe_id""")

            recipes = []
            for recipe in all_recipes:
                diet = str(Retrieve_db_data.retrieve_value(
                    """ SELECT Diet FROM recipe_id WHERE r_name = "{}";""".format(recipe)))
                if diet.find("Vegan") == 0:
                    recipes.append(recipe)

            return ("These recipes {} are vegan".format(recipes))


        elif diet == "3":
            all_recipes = Retrieve_db_data.retrieve_list(""" SELECT r_name FROM recipe_id""")

            recipes = []
            for recipe in all_recipes:
                diet = str(Retrieve_db_data.retrieve_value(
                    """ SELECT Diet FROM recipe_id WHERE r_name = "{}";""".format(recipe)))
                if diet.find("Gluten Free") == 0:
                    recipes.append(recipe)

            return ("These recipes {} are gluten free".format(recipes))

        elif diet == "4":
            all_recipes = Retrieve_db_data.retrieve_list(""" SELECT r_name FROM recipe_id""")

            recipes = []
            for recipe in all_recipes:
                diet = str(Retrieve_db_data.retrieve_value(
                    """ SELECT Diet FROM recipe_id WHERE r_name = "{}";""".format(recipe)))
                if diet.find("Lactose Free") == 0:
                    recipes.append(recipe)

            return ("These recipes {} are not lactose free".format(recipes))

        else:
            return("Option not found. Choose again")

    # users have the ability to like recipes
    # this function will add their liked recipes to the database, so they can look through the,
    # similar to a pinterest board
    def like_a_recipe():
            all_recipes = Retrieve_db_data.retrieve_list(""" SELECT r_name FROM recipe_id""")

            username = input("What is your username?")
            user_id = Retrieve_db_data.retrieve_value(""" SELECT id FROM users WHERE username = "{}"; """.format(username))
            recipe_to_save = input("What recipe would you like to save?")

        # this ensures users cannot like recipes which aren't in the app/DB already
            for recipe in all_recipes:
                if recipe == recipe_to_save:
                    recipe_id = Retrieve_db_data.retrieve_value(
                        """ SELECT id FROM recipe_id WHERE r_name = "{}";""".format(recipe_to_save))

                    Add2DB.general_add2DB("""INSERT INTO user_likes (user_id, liked_recipes) VALUES ({}, "{}" )""".format(
                    user_id, recipe_to_save))

                    return ("You have liked this recipe!")

            else:
                return ("Invalid recipe! This recipe is not in the database")

    # function if you want to up certain ingredients in your fridge
    # you can search for recipes with these ingredients
    def filter_by_ingredients():

        ingredient2use = input("Enter which ingredient you would like to use: ")

        recipe_id = Retrieve_db_data.retrieve_list(""" SELECT recipe_id FROM ingredients
    WHERE ingredient = "{}";""".format(ingredient2use))

        # this allows the function to list multiple recipes which have the specified ingredient in
        recipes_with_ingredient = []
        for i in recipe_id:
            recipe = Retrieve_db_data.retrieve_value(""" SELECT r_name FROM recipe_id WHERE id = {}""".format(i))
            recipes_with_ingredient.append(recipe)

        return ("You can make these recipes {} with {}". format(recipes_with_ingredient, ingredient2use))

    # function if you're missing an ingredient what to substitute it for
    # this is just an example, the actual app would have a full database full of substitutions
    def ingredient_substitution():
        missing_ingredient = input('Ingredient missing: ')
        substitutions = {"eggs": "tofu", "water": "milk", "chocolate spread": "melted chocolate"}

        return ("Substitution: {}".format(substitutions.get(missing_ingredient)))

