-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: what2eat
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `what2eat`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `what2eat` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `what2eat`;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `Category ID` int DEFAULT NULL,
  `Category` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Breakfast'),(2,'Lunch '),(3,'Snack'),(4,'Appetiser'),(5,'Dinner'),(6,'Dessert');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient_id`
--

DROP TABLE IF EXISTS `ingredient_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredient_id` (
  `ingredient_id` int DEFAULT NULL,
  `food_categroy` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient_id`
--

LOCK TABLES `ingredient_id` WRITE;
/*!40000 ALTER TABLE `ingredient_id` DISABLE KEYS */;
INSERT INTO `ingredient_id` VALUES (1,'Diary '),(2,'Eggs '),(3,'Seafood'),(4,'Poultry '),(5,'Pork '),(6,'Beef'),(7,'Wheat'),(8,'Fruit'),(9,'Vegetables '),(10,'Beans and Legumes');
/*!40000 ALTER TABLE `ingredient_id` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredients` (
  `recipe_id` int DEFAULT NULL,
  `Ingredient` text,
  `Ingredient ID` int DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Unit` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'Cheese',1,25,'grams'),(1,'Bread',7,2,'Slices'),(1,'Butter',1,2,'Tsp'),(2,'Beans',10,1,'Tin'),(2,'Baking Potato',9,2,NULL),(2,'Butter',1,2,'Tsp'),(3,'Pasta',7,600,'grams'),(3,'Butter',1,50,'grams'),(3,'Plain Flour',7,50,'grams'),(3,'Milk ',1,600,'ml'),(3,'Cheese',1,250,'grams'),(3,'Tuna',3,2,'Tin'),(3,'Sweetcorn',9,330,'grams'),(4,'Butter ',1,225,'grams'),(4,'Caster Sugar',NULL,225,'grams'),(4,'Eggs',1,4,NULL),(4,'Flour',7,225,'grams'),(4,'Lemon',8,1,NULL);
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_id`
--

DROP TABLE IF EXISTS `recipe_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe_id` (
  `id` int NOT NULL AUTO_INCREMENT,
  `r_name` text,
  `prep_time` int DEFAULT NULL,
  `cook_time` int DEFAULT NULL,
  `serving` int DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  `Diet` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_id`
--

LOCK TABLES `recipe_id` WRITE;
/*!40000 ALTER TABLE `recipe_id` DISABLE KEYS */;
INSERT INTO `recipe_id` VALUES (1,'Cheese on Toast',5,5,1,2,'Vegetarian, Seafood Allergy'),(2,'Beans and Jacket Potato',5,60,2,2,'Vegetarian, Seafood Allergy, Gluten Free'),(3,'Tuna pasta bake',10,45,4,5,NULL),(4,'Lemon Cake',15,45,8,6,'Vegetarian');
/*!40000 ALTER TABLE `recipe_id` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `steps`
--

DROP TABLE IF EXISTS `steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `steps` (
  `recipe_id` int DEFAULT NULL,
  `step_order` int DEFAULT NULL,
  `cooking_action` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `steps`
--

LOCK TABLES `steps` WRITE;
/*!40000 ALTER TABLE `steps` DISABLE KEYS */;
INSERT INTO `steps` VALUES (1,1,'Put bread under the grill until brown'),(1,2,'Flip bread and spread butter on slices'),(1,3,'Add cheese and put back under grill'),(1,4,'Once cheese has melted to your liking take out of grill and enjoy');
/*!40000 ALTER TABLE `steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_likes`
--

DROP TABLE IF EXISTS `user_likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_likes` (
  `user_id` int DEFAULT NULL,
  `liked_recipes` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_likes`
--

LOCK TABLES `user_likes` WRITE;
/*!40000 ALTER TABLE `user_likes` DISABLE KEYS */;
INSERT INTO `user_likes` VALUES (1,'Beans on Toast');
/*!40000 ALTER TABLE `user_likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` text,
  `username` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'charlotte@email.com','c_wils1'),(2,'t_mils@email.com','tmils4');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-21 22:07:01
