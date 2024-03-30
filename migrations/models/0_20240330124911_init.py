from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "nutrition" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "NDB_No" INT NOT NULL,
    "Shrt_Desc" VARCHAR(255) NOT NULL,
    "Water_g" DOUBLE PRECISION NOT NULL,
    "Energ_Kcal" INT NOT NULL,
    "Protein_g" DOUBLE PRECISION NOT NULL,
    "Lipid_Tot_g" DOUBLE PRECISION NOT NULL,
    "Ash_g" DOUBLE PRECISION NOT NULL,
    "Carbohydrt_g" DOUBLE PRECISION NOT NULL,
    "Fiber_TD_g" DOUBLE PRECISION NOT NULL,
    "Sugar_Tot_g" DOUBLE PRECISION NOT NULL,
    "Calcium_mg" DOUBLE PRECISION NOT NULL,
    "Iron_mg" DOUBLE PRECISION NOT NULL,
    "Magnesium_mg" DOUBLE PRECISION NOT NULL,
    "Phosphorus_mg" DOUBLE PRECISION NOT NULL,
    "Potassium_mg" DOUBLE PRECISION NOT NULL,
    "Sodium_mg" DOUBLE PRECISION NOT NULL,
    "Zinc_mg" DOUBLE PRECISION NOT NULL,
    "Copper_mg" DOUBLE PRECISION NOT NULL,
    "Manganese_mg" DOUBLE PRECISION NOT NULL,
    "Selenium_μg" DOUBLE PRECISION NOT NULL,
    "Vit_C_mg" DOUBLE PRECISION NOT NULL,
    "Thiamin_mg" DOUBLE PRECISION NOT NULL,
    "Riboflavin_mg" DOUBLE PRECISION NOT NULL,
    "Niacin_mg" DOUBLE PRECISION NOT NULL,
    "Panto_Acid_mg" DOUBLE PRECISION NOT NULL,
    "Vit_B6_mg" DOUBLE PRECISION NOT NULL,
    "Folate_Tot_μg" DOUBLE PRECISION NOT NULL,
    "Folic_Acid_μg" DOUBLE PRECISION NOT NULL,
    "Food_Folate_μg" DOUBLE PRECISION NOT NULL,
    "Folate_DFE_μg" DOUBLE PRECISION NOT NULL,
    "Choline_Tot_mg" DOUBLE PRECISION NOT NULL,
    "Vit_B12_μg" DOUBLE PRECISION NOT NULL,
    "Vit_A_IU" DOUBLE PRECISION NOT NULL,
    "Vit_A_RAE" DOUBLE PRECISION NOT NULL,
    "Retinol_μg" DOUBLE PRECISION NOT NULL,
    "Alpha_Carot_μg" DOUBLE PRECISION NOT NULL,
    "Beta_Carot_μg" DOUBLE PRECISION NOT NULL,
    "Beta_Crypt_μg" DOUBLE PRECISION NOT NULL,
    "Lycopene_μg" DOUBLE PRECISION NOT NULL,
    "Lut_Zea_μg" DOUBLE PRECISION NOT NULL,
    "Vit_E_mg" DOUBLE PRECISION NOT NULL,
    "Vit_D_μg" DOUBLE PRECISION NOT NULL,
    "Vit_D_IU" DOUBLE PRECISION NOT NULL,
    "Vit_K_μg" DOUBLE PRECISION NOT NULL,
    "FA_Sat_g" DOUBLE PRECISION NOT NULL,
    "FA_Mono_g" DOUBLE PRECISION NOT NULL,
    "FA_Poly_g" DOUBLE PRECISION NOT NULL,
    "Cholestrl_mg" DOUBLE PRECISION NOT NULL,
    "GmWt_1" DOUBLE PRECISION NOT NULL,
    "GmWt_Desc1" VARCHAR(255) NOT NULL,
    "GmWt_2" DOUBLE PRECISION NOT NULL,
    "GmWt_Desc2" VARCHAR(255) NOT NULL,
    "Refuse_Pct" DOUBLE PRECISION NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
