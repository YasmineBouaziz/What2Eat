import mysql.connector
# from mysql.connector import Error

HOST = "localhost"
USER = "root"
PASSWORD = "NZ256liw!0"

def _connect_to_db():
    # try:
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database= "recipe_app",
    )

    return connection

### RETRIEVE DATA ###
def retrieve_value(query):

    db_connection = _connect_to_db()
    cur = db_connection.cursor()
    cur.execute(query)
    result = cur.fetchall()

    result = [item for entry in result for item in entry][0]

    return result

def retrieve_list(query):
    db_connection = _connect_to_db()
    cur = db_connection.cursor()
    cur.execute(query)
    result = cur.fetchall()

    result = [item for entry in result for item in entry]

    return result

### ADD DATA TO DB ###
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
        print("Successfully added! DB connection is closed")

def add_uservalue():
    all_users = retrieve_list(""" SELECT email FROM users;""")
    u_email = "charlotte@email.co.uk"
    u_username = "c_wil1"
    u_pword = 1234

    for user in all_users:
        if user != u_email:
            general_add2DB(
                """ INSERT INTO users (email, username, pword ) VALUES ( "{}", "{}", "{}");""".format(u_email, u_username,
                                                                                                     u_pword))
            return("Well done! You successfully made an account!")

        else:
            return("This email address already has an account!")

### USER FUNCTIONS ####
recipe = "Lemon Cake"
servings = 8
ingredients = {"Butter": 225}

def scale_ingredients():
    to_serve = 16

    for value in ingredients:
        serve_one = ingredients[value] / servings
        adjusted_serving = serve_one * to_serve

    for value in ingredients:
        ingredients[value] = adjusted_serving

    return ingredients[value]

def filter_by_ingredients():

        ingredient2use = "Cheese"

        recipe_id = retrieve_list(""" SELECT recipe_id FROM ingredients
    WHERE ingredient = "{}";""".format(ingredient2use))

        # this allows the function to list multiple recipes which have the specified ingredient in
        recipes_with_ingredient = []
        for i in recipe_id:
            recipe = retrieve_value(""" SELECT recipe FROM recipe_id WHERE id = {}""".format(i))
            recipes_with_ingredient.append(recipe)

        return len(recipes_with_ingredient)

def ingredient_substitution():
    missing_ingredient = "eggs"
    substitutions = {"eggs": "tofu", "water": "milk", "chocolate spread": "melted chocolate"}

    return (substitutions.get(missing_ingredient))

def like_a_recipe():
    all_recipes = retrieve_list(""" SELECT recipe FROM recipe_id""")

    username = "c_wil1"
    user_id = retrieve_value(""" SELECT id FROM users WHERE username = "{}"; """.format(username))
    recipe_to_save = "Tuna pasta bake"

    # this ensures users cannot like recipes which aren't in the app/DB already
    for recipe in all_recipes:
        if recipe == recipe_to_save:
            recipe_id = retrieve_value(
                """ SELECT id FROM recipe_id WHERE recipe = "{}";""".format(recipe_to_save))

            general_add2DB(
                """INSERT INTO user_recipe_likes (user_id, liked_recipes) VALUES ({}, "{}" )""".format(
                    user_id, recipe_to_save))

            return ("You have liked this recipe!")

    else:
        return ("Invalid recipe! This recipe is not in the database")
