# Cybersecurity Automation, SOAR & DevSecOps Utilities

Welcome! This repository contains a curated collection of production-oriented automation scripts, data parsers, and infrastructure provisioning utilities developed for **Security Operations (SecOps)**, **Cortex XSOAR/XSIAM**, and **DevSecOps** environments.

**Note for Reviewers & Hiring Teams:** Due to strict NDA and enterprise confidentiality agreements across financial, healthcare, and government engagements, proprietary client playbooks and private integrations are excluded. The utilities in this repository represent sanitized, reusable engineering patterns for log parsing, data normalization, and containerized engine setup.

---

## Repository Overview

| File | Category | Description |
| :--- | :--- | :--- |
| **JSON2csv.py** | Cortex XSOAR / Data Engineering | Recursively flattens complex, nested JSON payloads and arrays into normalized, in-memory CSV War Room attachments for SOC analyst reporting and downstream ingestion. |
| **paralell2SerializedJSON.py** | Cortex XSOAR / Log Parsing | Converts line-delimited / parallel JSON streams (NDJSON) into validated, serialized JSON arrays with fault-tolerant line-by-line error handling for SIEM/SOAR pipelines. |
| **Download&ConvertJSONToCSV.py** | Data Collection & Transformation | Retrieves remote text- or JSON-style datasets from external URLs, parses line-delimited content, and exports the results into CSV format for threat-intelligence collection, reporting, and downstream analytics workflows. |
| **FetchURLDataToCSV.py** | Data Collection & Automation | Reusable utility function for fetching URL-based datasets and converting retrieved line-by-line content into CSV files, enabling rapid ingestion of external intelligence feeds and network indicator lists. |
| **UrlToCSV.py** | Threat Intelligence & Data Collection | Python utility that retrieves remote URL-hosted datasets, processes line-based content, and exports results into CSV format. Useful for collecting threat intelligence feeds, IOC lists, blocklists, and other security-related datasets for analysis and automation workflows. |
| **URLDataScrapper.py** | Web Scraping & Data Extraction | Uses Requests and BeautifulSoup to scrape structured HTML table data from web pages and convert the extracted records into CSV output. Demonstrates lightweight web data extraction techniques for intelligence gathering, reporting, and downstream analytics pipelines. |
| **placeHolderClass.py** | API Integration & Automation | Object-oriented HTTP client wrapper (`apiHandler`) using `requests` to execute `GET`, `POST`, and `DELETE` operations against JSONPlaceholder endpoints, including timestamp injection (`dd/mm/yyyy HH:MM:SS`) and response header/status inspection[cite: 2]. |
| **caller.py** | API Integration & Automation | Executable demonstration script that imports `apiHandler` from `placeHolderClass.py` to run sample `GET` (including status code branching), `POST`, and `DELETE` requests and print formatted outputs[cite: 1]. |
| **dockerInstall.sh** | DevSecOps / Infrastructure | Idempotent Bash automation script for provisioning and hardening Docker Engine, `containerd`, and Docker Compose on Ubuntu Linux servers (used for containerized SOAR reverse-proxy engines). |
| **installPandasAndUvicorn.py** | API & Data Tooling | Environment bootstrap utility for deploying FastAPI/Uvicorn microservices and Pandas data-analysis dependencies. |

---

## Core Engineering Patterns Demonstrated

- **Defensive Coding & Fault Tolerance:** Graceful handling of malformed log lines, empty payloads, and strict exit-on-error (`set -e`) shell execution.
- **Memory-Safe Data Transformation:** In-memory buffer streaming (`io.StringIO`) and dynamic schema extraction to normalize heterogeneous security telemetry without disk I/O bottlenecks.
- **SOAR Ecosystem Native:** Built using standard Palo Alto Cortex XSOAR (`CommonServerPython`) conventions (`CommandResults`, `fileResult`, `return_error`) for seamless playbook integration.
- **Repeatable Infrastructure Provisioning:** Automated GPG keyring verification, repository pinning, and least-privilege user group configuration for Linux container hosts.

---

## About the Author

**Norman Castro Aguilar**  
*Senior Cybersecurity Automation Engineer | DevSecOps Architect | Security Operations Lead*

- **Core Stack:** Palo Alto Cortex XSIAM & XSOAR, PANW XDR, Python, Bash, PowerShell, Docker, Podman, Terraform, AWS, Azure, GCP, XQL/SQL, MITRE ATT&CK, Agentic AI SecOps.
- **LinkedIn:** https://www.linkedin.com/in/normancastro
- **Contact:** normancastroa@mail.com
