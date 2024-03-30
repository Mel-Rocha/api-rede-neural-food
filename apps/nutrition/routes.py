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
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = None
        if file.filename.endswith(".xls") or file.filename.endswith(".xlsx"):
            df = pd.read_excel(BytesIO(contents), engine="xlrd")
        elif file.filename.endswith(".csv"):
            df = pd.read_csv(BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Por favor, envie um arquivo Excel ou CSV válido.")

        data = []
        for _, row in df.iterrows():
            nutrition = Nutrition(
                NDB_No=row['NDB_No'],
                Shrt_Desc=row['Shrt_Desc'],
                Water_g=row['Water_(g)'],
                Energ_Kcal=row['Energ_Kcal'],
                Protein_g=row['Protein_(g)'],
                Lipid_Tot_g=row['Lipid_Tot_(g)'],
                Ash_g=row['Ash_(g)'],
                Carbohydrt_g=row['Carbohydrt_(g)'],
                Fiber_TD_g=row['Fiber_TD_(g)'],
                Sugar_Tot_g=row['Sugar_Tot_(g)'],
                Calcium_mg=row['Calcium_(mg)'],
                Iron_mg=row['Iron_(mg)'],
                Magnesium_mg=row['Magnesium_(mg)'],
                Phosphorus_mg=row['Phosphorus_(mg)'],
                Potassium_mg=row['Potassium_(mg)'],
                Sodium_mg=row['Sodium_(mg)'],
                Zinc_mg=row['Zinc_(mg)'],
                Copper_mg=row['Copper_mg)'],
                Manganese_mg=row['Manganese_(mg)'],
                Selenium_µg=row['Selenium_(µg)'],
                Vit_C_mg=row['Vit_C_(mg)'],
                Thiamin_mg=row['Thiamin_(mg)'],
                Riboflavin_mg=row['Riboflavin_(mg)'],
                Niacin_mg=row['Niacin_(mg)'],
                Panto_Acid_mg=row['Panto_Acid_mg)'],
                Vit_B6_mg=row['Vit_B6_(mg)'],
                Folate_Tot_µg=row['Folate_Tot_(µg)'],
                Folic_Acid_µg=row['Folic_Acid_(µg)'],
                Food_Folate_µg=row['Food_Folate_(µg)'],
                Folate_DFE_µg=row['Folate_DFE_(µg)'],
                Choline_Tot_mg=row['Choline_Tot_ (mg)'],
                Vit_B12_µg=row['Vit_B12_(µg)'],
                Vit_A_IU=row['Vit_A_IU'],
                Vit_A_RAE=row['Vit_A_RAE'],
                Retinol_µg=row['Retinol_(µg)'],
                Alpha_Carot_µg=row['Alpha_Carot_(µg)'],
                Beta_Carot_µg=row['Beta_Carot_(µg)'],
                Beta_Crypt_µg=row['Beta_Crypt_(µg)'],
                Lycopene_µg=row['Lycopene_(µg)'],
                Lut_Zea_µg=row['Lut+Zea_ (µg)'],
                Vit_E_mg=row['Vit_E_(mg)'],
                Vit_D_µg=row['Vit_D_µg'],
                Vit_D_IU=row['Vit_D_IU'],
                Vit_K_µg=row['Vit_K_(µg)'],
                FA_Sat_g=row['FA_Sat_(g)'],
                FA_Mono_g=row['FA_Mono_(g)'],
                FA_Poly_g=row['FA_Poly_(g)'],
                Cholestrl_mg=row['Cholestrl_(mg)'],
                GmWt_1=row['GmWt_1'],
                GmWt_Desc1=row['GmWt_Desc1'],
                GmWt_2=row['GmWt_2'],
                GmWt_Desc2=row['GmWt_Desc2'],
                Refuse_Pct=row['Refuse_Pct']
            )
            data.append(nutrition)

        await Nutrition.bulk_create(data)
        return JSONResponse(
            content={"message": "Todos os dados foram cadastrados com sucesso"},
            status_code=201
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))