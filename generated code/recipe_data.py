"""
Module for managing recipe data and collections.
"""
import logging, re
from typing import List, Dict, Any
from breakfast_recipes import BREAKFAST_RECIPES
from lunch_recipes import LUNCH_RECIPES
from dinner_recipes import DINNER_RECIPES


def get_breakfast_recipes() -> List[Dict[str, Any]]:
    """
    Returns a collection of 10 breakfast recipes.
    
    Returns:
        List[Dict[str, Any]]: A list of 10 breakfast recipe dictionaries
    """
    logger = logging.getLogger(__name__)
    logger.debug("Generating breakfast recipes collection")
    
    try:
        logger.debug(f"Successfully generated {len(BREAKFAST_RECIPES)} breakfast recipes")
        return BREAKFAST_RECIPES
    except Exception as e:
        logger.error(f"Error generating breakfast recipes: {e}", exc_info=True)
        # Return an empty list as a fallback
        return []


def get_lunch_recipes() -> List[Dict[str, Any]]:
    """
    Returns a collection of 10 lunch recipes.
    
    Returns:
        List[Dict[str, Any]]: A list of 10 lunch recipe dictionaries
    """
    logger = logging.getLogger(__name__)
    logger.debug("Generating lunch recipes collection")
    
    try:
        logger.debug(f"Successfully generated {len(LUNCH_RECIPES)} lunch recipes")
        return LUNCH_RECIPES
    except Exception as e:
        logger.error(f"Error generating lunch recipes: {e}", exc_info=True)
        return []


def get_dinner_recipes() -> List[Dict[str, Any]]:
    """
    Returns a collection of 10 dinner recipes.
    
    Returns:
        List[Dict[str, Any]]: A list of 10 dinner recipe dictionaries
    """
    logger = logging.getLogger(__name__)
    logger.debug("Generating dinner recipes collection")
    
    try:
        logger.debug(f"Successfully generated {len(DINNER_RECIPES)} dinner recipes") 
        return DINNER_RECIPES
    except Exception as e:
        logger.error(f"Error generating dinner recipes: {e}", exc_info=True)
        return []


def filter_recipes_by_ingredient(recipes: List[Dict[str, Any]], ingredient: str) -> List[Dict[str, Any]]:
    """
    Filters a collection of recipes to include only those containing the specified ingredient.
    
    Args:
        recipes (List[Dict[str, Any]]): The collection of recipes to filter
        ingredient (str): The ingredient to filter by
        
    Returns:
        List[Dict[str, Any]]: A filtered list of recipes containing the specified ingredient
    """
    logger = logging.getLogger(__name__)
    logger.debug(f"Filtering recipes by ingredient: {ingredient}")
    
    try:
        # Create a case-insensitive pattern for the ingredient
        pattern = re.compile(re.escape(ingredient), re.IGNORECASE)
        
        # Filter recipes that have the ingredient in any of their ingredients
        filtered_recipes = [recipe for recipe in recipes if any(pattern.search(ing) for ing in recipe["ingredients"])]
        
        logger.debug(f"Found {len(filtered_recipes)} recipes containing '{ingredient}'")
        return filtered_recipes
    except Exception as e:
        logger.error(f"Error filtering recipes by ingredient: {e}", exc_info=True)
        return []