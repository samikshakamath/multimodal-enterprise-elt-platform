# Multimodal Enterprise ELT Platform

## Overview

Built a multimodal ELT platform that processes logs, customer support transcripts, documents, and images through a Medallion Architecture (Bronze → Silver → Gold).

The platform combines FastAPI, PySpark, Docker, GitHub Actions, and Power BI to automate ingestion, transformation, validation, orchestration, and analytics generation across multiple data modalities.

---

## Architecture

```text
FastAPI
    │
    ▼
Classification Layer
    │
    ├── Logs
    ├── Transcripts
    ├── Documents
    └── Images
            │
            ▼
        Bronze
            │
            ▼
        Silver
            │
            ▼
    Quality Checks
            │
            ▼
         Gold
            │
            ▼
        Power BI
```

---

## Tech Stack

| Layer            | Technologies           |
| ---------------- | ---------------------- |
| API              | FastAPI                |
| Data Processing  | Python, Pandas         |
| Data Engineering | PySpark                |
| Data Quality     | Great Expectations     |
| Orchestration    | Python                 |
| DevOps           | Docker, GitHub Actions |
| Visualization    | Power BI               |

---

## Key Features

* Multimodal data processing
* Bronze–Silver–Gold architecture
* PySpark transformation pipelines
* Automated data quality validation
* Dockerized deployment
* CI/CD with GitHub Actions
* Automated orchestration layer
* Power BI analytics reporting

---

## Supported Data Modalities

| Modality    | Output                     |
| ----------- | -------------------------- |
| Logs        | Event-level analytics      |
| Transcripts | Customer-support analytics |
| Documents   | Document-type analytics    |
| Images      | Image-category analytics   |

---

## Project Structure

```text
app/
src/
├── classification/
├── ingestion/
├── processing/
├── transformations/
├── quality/
└── orchestration/

Dockerfile
requirements.txt
```

---

## Run Locally

```bash
docker build -t multimodal-elt .
docker run -p 8000:8000 multimodal-elt
```

```bash
python src/orchestration/run_pipeline.py
```

---

## CI/CD

GitHub Actions validates:

* FastAPI application
* Processing pipelines
* Transformation scripts
* Data quality modules
* Repository structure

```
```
