from pyspark.sql import DataFrame
from pyspark.sql.functions import col, when

class CropsDataFrameBuilder:
    def __init__(self, df: DataFrame):
        self.df = df

    def cast_columns(self):
        cols_to_cast = [
            "Área destinada (ha)", "Área colhida (ha)", "Produção (t)",
            "Rendimento (kg/ha)", "Valor produção (R$ mil)"
        ]
        for col_name in cols_to_cast:
            self.df = self.df.withColumn(col_name, col(col_name).cast("double"))
        return self

    def compute_metrics(self):
        self.df = self.df.withColumn(
            "Taxa de colheita (%)", (col("Área colhida (ha)") / col("Área destinada (ha)")) * 100
        ).withColumn(
            "Valor por tonelada (R$/t)",
            when(col("Produção (t)") > 0, col("Valor produção (R$ mil)") * 1000 / col("Produção (t)"))
        ).withColumn(
            "Valor por hectare (R$/ha)",
            when(col("Área colhida (ha)") > 0, col("Valor produção (R$ mil)") * 1000 / col("Área colhida (ha)"))
        )
        return self

    def build(self) -> DataFrame:
        return self.df
