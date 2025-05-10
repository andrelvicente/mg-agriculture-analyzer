from builder.crops_df_builder import CropsDataFrameBuilder
from pyspark.sql import SparkSession
from schema.crops_schema import CropsSchema


class CropsProcessor:
    def __init__(self, spark: SparkSession, file_path: str):
        self.spark = spark
        self.file_path = file_path

    def run(self):
        df = self.spark.read.option("header", True) \
            .schema(CropsSchema.get_schema()) \
            .csv(self.file_path)

        processed_df = (
            CropsDataFrameBuilder(df)
            .cast_columns()
            .compute_metrics()
            .build()
        )

        processed_df.select(
            "UF", "Mesorregião", "Município", "Produto",
            "Área colhida (ha)", "Produção (t)", "Valor produção (R$ mil)",
            "Taxa de colheita (%)", "Valor por tonelada (R$/t)", "Valor por hectare (R$/ha)"
        ).show(20)
