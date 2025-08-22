"""
User interface functions for the Recipe Book application.
"""
import logging
import sys
from recipe_data import get_breakfast_recipes, get_lunch_recipes, get_dinner_recipes


def display_welcome_message():
    """
    Display a welcome message to the user.
    
    Returns:
        str: The welcome message
    """
    welcome_message = "Welcome to the Recipe Book Application!"
    print(welcome_message)
    return welcome_message


def get_user_meal_category_choice(input_func=input, default_choice=None) -> str:
    """
    Prompt the user to choose a meal category.
    
    Returns:
        str: The selected meal category ("breakfast", "lunch", or "dinner")
    """
    logger = logging.getLogger(__name__)
    valid_categories = ["breakfast", "lunch", "dinner"]

    # If a default choice is provided (useful for testing), use it
    if default_choice is not None and default_choice in valid_categories:
        logger.info(f"Using default meal category: {default_choice}")
        return default_choice
    
    # In test environments, we still want to use the provided input_func
    # rather than returning a default value
    
    for _ in range(3):  # Limit attempts to prevent infinite loops in tests
        print("\nPlease choose a meal category:")
        for i, category in enumerate(valid_categories, 1):
            print(f"{i}. {category.capitalize()}")
        
        try:
            # Add timeout handling for input to prevent hanging in tests
            try: 
                choice = input_func("\nEnter your choice (1-3): ")
            except (EOFError, KeyboardInterrupt):
                logger.warning("Input interrupted. Defaulting to breakfast.")
                return "breakfast"
            
            # Check if input is a number between 1-3
            if choice.isdigit() and 1 <= int(choice) <= 3:
                selected_category = valid_categories[int(choice) - 1]
                logger.info(f"User selected meal category: {selected_category}")
                return selected_category
            else:
                print(f"Invalid choice: '{choice}'. Please enter a number between 1 and 3.")
        except Exception as e:
            logger.error(f"Error processing user input: {e}", exc_info=True)
            print("An error occurred. Please try again.")
    
    # Default to breakfast if no valid input after attempts (helps with testing)
    logger.warning("No valid input after multiple attempts. Defaulting to breakfast.")
    return "breakfast"


def display_recipes_by_category(category: str) -> list:
    """
    Display recipes for the selected meal category.
    
    Args:
        category (str): The meal category to display recipes for
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Displaying recipes for category: {category}")
    
    recipes = {"breakfast": get_breakfast_recipes, "lunch": get_lunch_recipes, "dinner": get_dinner_recipes}
    selected_recipes = recipes[category]()
    
    print(f"\n=== {category.capitalize()} Recipes ===")
    for i, recipe in enumerate(selected_recipes, 1):
        print(f"{i}. {recipe['name']} ({recipe['DifficultyLevel']} difficulty)")
    
    return selected_recipes


def get_user_preferred_ingredient(input_func=input, default_ingredient=None) -> str:
    """
    Prompt the user to enter a preferred ingredient.
    
    Args:
        input_func: Function to use for input (useful for testing)
        default_ingredient: Default ingredient to use (useful for testing)
        
    Returns:
        str: The preferred ingredient entered by the user
    """
    logger = logging.getLogger(__name__)
    
    # If a default ingredient is provided (useful for testing), use it
    if default_ingredient is not None:
        logger.info(f"Using default ingredient: {default_ingredient}")
        return default_ingredient
    
    try:
        print("\nWould you like to filter recipes by a specific ingredient? (yes/no)")
        try:
            filter_choice = input_func("Enter yes/no: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            logger.warning("Input interrupted. Defaulting to no filtering.")
            return ""
        
        if filter_choice in ["yes", "y"]:
            print("\nEnter your preferred ingredient:")
            ingredient = input_func("Ingredient: ").strip()
            logger.info(f"User entered preferred ingredient: {ingredient}") 
            return ingredient
        else:
            return ""
    except Exception as e:
        logger.error(f"Error getting user preferred ingredient: {e}", exc_info=True)
        return ""


def get_user_recipe_choice(recipes: list, input_func=input, default_choice=None) -> int:
    """
    Prompt the user to choose a specific recipe from the displayed list.
    
    Args:
        recipes (list): The list of recipes to choose from
        input_func: Function to use for input (useful for testing)
        default_choice: Default choice to use (useful for testing)
        
    Returns:
        int: The index of the selected recipe in the recipes list, or -1 if invalid
    """
    logger = logging.getLogger(__name__)
    
    # If no recipes are available, return -1
    if not recipes:
        logger.warning("No recipes available to choose from")
        return -1
    
    # If a default choice is provided (useful for testing), use it
    if default_choice is not None and 0 <= default_choice < len(recipes):
        logger.info(f"Using default recipe choice: {default_choice}")
        return default_choice
    
    try:
        print("\nWould you like to view a specific recipe? (yes/no)")
        try:
            view_choice = input_func("Enter yes/no: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            logger.warning("Input interrupted. Defaulting to no recipe selection.")
            return -1
        
        if view_choice in ["yes", "y"]:
            print(f"\nEnter the number of the recipe you'd like to view (1-{len(recipes)}):")
            choice = input_func("Enter recipe number: ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= len(recipes):
                recipe_index = int(choice) - 1  # Convert from 1-based to 0-based indexing
                logger.info(f"User selected recipe index: {recipe_index}")
                return recipe_index
            else:
                print(f"Invalid choice: '{choice}'. Please enter a number between 1 and {len(recipes)}.")
                return -1
        else:
            return -1
    except Exception as e:
        logger.error(f"Error getting user recipe choice: {e}", exc_info=True)
        return -1


def display_recipe_details(recipe: dict):
    """
    Display the full details of a recipe.
    
    Args:
        recipe (dict): The recipe to display
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Displaying details for recipe: {recipe['name']}")
    
    print(f"\n{'=' * 50}")
    print(f"{recipe['name']} ({recipe['DifficultyLevel']} difficulty)")
    print(f"{'=' * 50}")
    
    print("\nIngredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    
    print("\nInstructions:")
    for i, instruction in enumerate(recipe['instructions'], 1):
        print(f"{i}. {instruction}")
    
    print(f"\nMeal Category: {recipe['MealCategory'].capitalize()}")