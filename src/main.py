from config.spark_config import get_spark_session
from service.crops_processor import CropsProcessor

def main():
    spark = get_spark_session()
    file_path = "minas_gerais_permanents_crops.csv"
    processor = CropsProcessor(spark, file_path)
    processor.run()

if __name__ == "__main__":
    main()
