# Minas Agriculture Data Analyser

A PySpark-based project to process and analyze agricultural production data from Minas Gerais, Brazil.

## 📌 Objectives

- Parse and clean official CSV data on permanent crops.
- Calculate key agronomic metrics such as:
  - Harvest rate (%)
  - Value per ton (R$/t)
  - Value per hectare (R$/ha)
- Enable structured and reproducible data pipelines using Spark.

## 📂 Project Structure

```
agronomic_analysis/
├── main.py                         # Entry point
├── config/                         # Spark session configuration
├── schema/                         # Spark schema definition
├── builder/                        # DataFrame builder pattern
├── service/                        # Business logic for processing
├── setup/                          # Setup and execution scripts
├── requirements.txt                # Runtime dependencies
├── dev-requirements.txt           # Dev/test dependencies
└── README.md
```

## 🚀 How to Run

```bash
# Step 1: Setup the environment
bash setup/setup_env.sh

# Step 2: Run the project
bash setup/run_project.sh
```

## 🧪 Running Tests

```bash
source venv/bin/activate
pytest
```

## 📄 Data Source

Official CSV extracted from [IBGE or regional government datasets].
