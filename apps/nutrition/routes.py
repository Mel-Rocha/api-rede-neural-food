import os
import logging
import asyncio
import difflib
import psycopg2
import pandas as pd
from io import BytesIO
from itertools import chain
from dotenv import load_dotenv
from collections import defaultdict
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import Page, add_pagination, paginate
from fastapi import APIRouter, HTTPException, Path, UploadFile, File
from tortoise.exceptions import IntegrityError, ValidationError, OperationalError

from apps.nutrition.models import Nutrition
from apps.nutrition.schema import NutritionSchema

load_dotenv()

router = APIRouter()

ENDPOINT_TABELA_SOMOS = os.getenv('ENDPOINT_TABELA_SOMOS')


@router.get("/")
async def get_nutrition_all() -> Page[NutritionSchema]:
    nutrition_all = await Nutrition.all()

    return paginate(nutrition_all)


add_pagination(router)


@router.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    pass


