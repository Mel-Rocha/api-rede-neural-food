from tortoise.contrib.pydantic import pydantic_model_creator

from apps.nutrition.models import Nutrition

NutritionSchema = None


def initialize_nutrition_schema():
    global NutritionSchema
    NutritionSchema = pydantic_model_creator(Nutrition)


initialize_nutrition_schema()
