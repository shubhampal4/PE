# Kubernetes, Observability, and Airflow Architecture Task Bundle

## 📁 Overview

This repository contains manifests and code snippets for mastering:
- Kubernetes Pod scheduling and network policies
- OpenTelemetry-based observability and tracing in Python
- Prometheus SLO-based alerting strategy
- Apache Airflow DAG design and debugging

---

## 🚀 1. Kubernetes Mastery

### 1.1 Pod Scheduling & Resource Management

✅ **Objective**:  
Create a pod that:
- Runs only on `env=prod` nodes with GPU
- Has resource requests and limits (500Mi/250m → 2Gi/1CPU)
- Is not evicted under memory pressure
- Mounts a secret volume

📄 **File**: `k8s/pod_gpu.yaml`

### 1.2 Network Policy & Secure Exposure

✅ **Objective**:  
Deploy a frontend app exposed via Ingress, and restrict access to it using a `NetworkPolicy` that only allows pods with label `access: true` from the `backend` namespace.

📄 **Files**:
- `k8s/frontend_ingress.yaml`
- `k8s/network_policy.yaml`

---

## 🔍 2. Observability & Tracing

### 2.1 OpenTelemetry Instrumentation in Python

✅ **Objective**:  
Instrument a Python function to:
- Create a span inside `process_payment(user_id)`
- Add baggage and attributes
- Export trace data to local OpenTelemetry Collector (OTLP)

📄 **File**: `observability/opentelemetry_payment.py`  
➡️ Uses: `OTLPSpanExporter`, `BatchSpanProcessor`, and `baggage`.

### 2.2 SLOs & Alert Design

✅ **Objective**:  
Design Prometheus alerts for an API endpoint `/checkout` with:
- 2 SLIs: latency and error rate
- Corresponding SLO targets
- A multi-window burn rate alert

📄 **File**: `observability/slo_alerts.yaml`

---

## ⚙️ 3. Airflow Architecture & DAG Design

### 3.1 DAG: Extract → Transform → Load to S3

✅ **Objective**:  
Create a DAG that:
- Extracts data from an API
- Transforms data
- Loads to AWS S3
- Retries with exponential backoff

📄 **File**: `airflow/api_to_s3_dag.py`  
➡️ Uses `@task`, `boto3`, `requests`, and DAG structuring best practices.

### 3.2 DAG Debugging Scenario

✅ **Problem**:  
“A task is skipped randomly despite the previous one succeeding.”

🛠 **Explanation**:
- Might be due to improper `trigger_rule` (default: `all_success`)
- Use `TriggerRule.ALL_DONE` to ensure task always runs

📄 **File**: `airflow/debugging_notes.md`

---

## 📦 Folder Structure

project-root/
├── k8s/
│ ├── pod_gpu.yaml
│ ├── frontend_ingress.yaml
│ └── networkpolicy.yaml
├── observability/
│ ├── opentelemetry_payment.py
│ └── slo_alerts.yaml
├── airflow/
│ ├── api_to_s3_dag.py
│ └── debugging_notes.md
└── README.md ← This file