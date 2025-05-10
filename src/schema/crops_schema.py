from pyspark.sql.types import StructType, StructField, StringType, DoubleType

class CropsSchema:
    @staticmethod
    def get_schema():
        return StructType([
            StructField("UF", StringType(), True),
            StructField("Mesorregião", StringType(), True),
            StructField("Microrregião", StringType(), True),
            StructField("Município", StringType(), True),
            StructField("Produto", StringType(), True),
            StructField("Área destinada (ha)", DoubleType(), True),
            StructField("Área colhida (ha)", DoubleType(), True),
            StructField("Produção (t)", DoubleType(), True),
            StructField("Rendimento (kg/ha)", DoubleType(), True),
            StructField("Valor produção (R$ mil)", DoubleType(), True),
        ])
