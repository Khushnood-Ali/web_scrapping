# 🧩 Web Scraping Tutor

## 📘 Overview
This repository automates data collection from Apache Jira projects and transforms it into structured datasets for **LLM training tasks** such as summarization, classification, and question-answering.

It includes scraping utilities, error handling mechanisms, optimization strategies, and configuration templates for scalable and fault-tolerant operation.

---

## 🏗️ Project Structure
```
jira-llm-pipeline/
│
├── script.py                        # Architecture overview generator
├── script_1.py                      # Code example generator
├── script_2.py                      # Project structure and README creator
├── script_3.py                      # LLM training data generator
├── script_4.py                      # Requirements and setup generator
│
├── architecture_overview.json       # Defines system architecture and components
├── config_projects.yaml             # Project & scraper configuration
├── example_llm_training_data.jsonl  # Example formatted Jira issues for LLMs
│
├── code_examples.csv                # Key implementation examples
├── edge_cases_handling.csv          # Error handling definitions
├── optimization_strategies.csv      # Performance tuning strategies
├── recommended_apache_projects.csv  # Selected Apache projects
│
├── requirements.txt                 # Dependencies
├── setup_instructions.md            # Installation and usage steps
│
└── README.md                        # Project overview and documentation
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Git

### Installation
```bash
git clone <repository-url>
cd jira-llm-pipeline
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## ⚙️ Usage
You can run scripts individually to generate data or documentation components.

```bash
python script.py          # Generates architecture overview
python script_1.py        # Creates code examples
python script_2.py        # Builds project structure
python script_3.py        # Produces example JSONL training data
python script_4.py        # Outputs requirements & setup guides
```

---

## 📊 Dataset Schema Example
Each JSONL record contains structured Jira issue data for multiple ML tasks:

```json
{
  "metadata": {"issue_key": "KAFKA-12345", "project": "KAFKA", "status": "Resolved"},
  "title": "Consumer group rebalance takes too long",
  "description": "Details about the bug and fix proposal...",
  "tasks": [
    {"task_type": "summarization", "input": "...", "target": "..."},
    {"task_type": "classification", "input": "...", "target": {"status": "Resolved"}}
  ]
}
```

---

## 🧠 Optimization Strategies
- **Concurrent Requests**: async scraping with aiohttp for speed.
- **Batch Processing**: fetch multiple issues per API call.
- **Incremental Updates**: scrape only changed issues since last run.

---

## 🧰 Edge Case Handling
Robust handling for:
- HTTP rate limits (429)
- Timeouts & server errors
- Partial failures with checkpoint recovery

---

