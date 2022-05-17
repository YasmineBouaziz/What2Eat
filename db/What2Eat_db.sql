CREATE DATABASE What2Eat;
USE What2Eat;

CREATE TABLE users (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(30) NOT NULL,
username VARCHAR(30) NOT NULL,
pword VARCHAR(30) NOT NULL
);

Create Table course (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(25)
);

CREATE TABLE category (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(25)
);

Create Table recipe (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (id) REFERENCES course(id),
FOREIGN KEY(id) REFERENCES category(id),
r_name VARCHAR(25) NOT NULL,
r_description VARCHAR(50) NOT NULL,
prep_time int,
cook_time int
);

CREATE Table ingredient (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name varchar(20)
);


CREATE TABLE recipe_ingredient (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (id) REFERENCES recipe(id),
FOREIGN KEY (id) REFERENCES ingredient(id),
quantity float
);

CREATE TABLE actions (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
cooking_action varchar(50)
);

CREATE TABLE recipe_steps (
id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (id) REFERENCES recipe(id),
FOREIGN KEY (id) REFERENCES ingredient(id),
FOREIGN KEY (id) REFERENCES actions(id),
step_order int,
step_time int
);


select * From recipe;
SELECT DATA_TYPE from INFORMATION_SCHEMA.columns WHERE table_schema = 'What2Eat' and table_name = 'actions';


INSERT INTO users
(id, email, username, pword)
VALUES
( NULL, 'yas.bo@gmail.com', 'yasbo', '1234');


INSERT INTO course
(id, name)
VALUES
(NULL, 'Breakfast'),
(NULL, 'Lunch'),
(NULL, 'Snack'),
(NULL, 'Appetizer'),
(NULL, 'Dinner'),
(NULL, 'Dessert');



INSERT INTO category
(id, name)
VALUES
(NULL, 'Veggie'),
(NULL, 'Mediterranean'),
(NULL, 'Pizza'),
(NULL, 'Kebab'),
(NULL, 'Japanese'),
(NULL, 'Chinese'),
(NULL, 'American'),
(NULL, 'Indian'),
(NULL, 'Caribbean'),
(NULL, 'Chicken'),
(NULL, 'Sandwiches');
SELECT * FROM category;
