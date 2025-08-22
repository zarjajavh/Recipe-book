#!/usr/bin/env python3
"""
Entry point for the console application.
"""
import sys
import logging
from recipe_book_ui import (
    display_welcome_message as ui_display_welcome_message,
    get_user_meal_category_choice as ui_get_user_meal_category_choice,
    display_recipes_by_category as ui_display_recipes_by_category,
    get_user_preferred_ingredient as ui_get_user_preferred_ingredient,
    get_user_recipe_choice as ui_get_user_recipe_choice,
    display_recipe_details as ui_display_recipe_details
)
from recipe_data import get_breakfast_recipes, get_lunch_recipes, get_dinner_recipes, filter_recipes_by_ingredient


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger(__name__)


# Wrapper functions to make mocking easier in tests
def display_welcome_message():
    """Wrapper for display_welcome_message from recipe_book_ui."""
    return ui_display_welcome_message()


def get_user_meal_category_choice(input_func=input):
    """Wrapper for get_user_meal_category_choice from recipe_book_ui."""
    return ui_get_user_meal_category_choice(input_func=input_func)


def display_recipes_by_category(category):
    """Wrapper for display_recipes_by_category from recipe_book_ui."""
    return ui_display_recipes_by_category(category)


def get_user_preferred_ingredient(input_func=input, default_ingredient=None):
    """Wrapper for get_user_preferred_ingredient from recipe_book_ui."""
    return ui_get_user_preferred_ingredient(input_func=input_func, default_ingredient=default_ingredient)


def get_user_recipe_choice(recipes, input_func=input):
    """Wrapper for get_user_recipe_choice from recipe_book_ui."""
    return ui_get_user_recipe_choice(recipes, input_func=input_func)


def display_recipe_details(recipe):
    """Wrapper for display_recipe_details from recipe_book_ui."""
    return ui_display_recipe_details(recipe)


# Re-export functions from recipe_data for easier mocking
def get_breakfast_recipes_wrapper():
    """Wrapper for get_breakfast_recipes from recipe_data."""
    return get_breakfast_recipes()

def filter_recipes_by_ingredient_wrapper(recipes, ingredient):
    """Wrapper for filter_recipes_by_ingredient from recipe_data."""
    return filter_recipes_by_ingredient(recipes, ingredient)


def main():
    """
    Main entry point for the application.
    
    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    try:
        logger = setup_logging()

        logger.debug("Application started")
        
        # Display welcome message
        display_welcome_message()
        
        # Ask user to choose a meal category (this will be mocked in tests)
        selected_category = get_user_meal_category_choice(input_func=input)
        
        # Display recipes for the selected category
        recipes = display_recipes_by_category(selected_category) 
        
        preferred_ingredient = get_user_preferred_ingredient(input_func=input)
        
        # If user provided an ingredient, filter and display matching recipes
        if preferred_ingredient:
            filtered_recipes = filter_recipes_by_ingredient_wrapper(recipes, preferred_ingredient)
            if filtered_recipes:
                print(f"\n=== {selected_category.capitalize()} Recipes with '{preferred_ingredient}' ===")
                for i, recipe in enumerate(filtered_recipes, 1):
                    print(f"{i}. {recipe['name']} ({recipe['DifficultyLevel']} difficulty)")
            else:
                print(f"\nNo {selected_category} recipes found containing '{preferred_ingredient}'.")
        
        # Display recipes to choose from (either filtered or all)
        recipes_to_choose_from = filtered_recipes if preferred_ingredient and filtered_recipes else recipes
        
        # Ask user to choose a specific recipe
        recipe_index = get_user_recipe_choice(recipes_to_choose_from, input_func=input)
        
        # If user selected a valid recipe, display its details
        if recipe_index >= 0:
            selected_recipe = recipes_to_choose_from[recipe_index]
            display_recipe_details(selected_recipe)
        
        logger.debug("Application completed successfully")
        return 0
    except Exception as e:
        # If logger is not defined (e.g., setup_logging failed), use root logger
        try:
            logger.error(f"An error occurred: {e}", exc_info=True)
        except UnboundLocalError:
            # Fallback to root logger if logger is not defined
            logging.error(f"An error occurred during application startup: {e}", exc_info=True)
        
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)