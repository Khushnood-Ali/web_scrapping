
# Create requirements.txt and setup instructions
requirements_txt = """# Core Dependencies
requests>=2.31.0
urllib3>=2.0.0
beautifulsoup4>=4.12.0
lxml>=4.9.0

# Async support (optional but recommended)
aiohttp>=3.9.0
asyncio>=3.4.3

# Data handling
PyYAML>=6.0
python-dotenv>=1.0.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-mock>=3.11.0
responses>=0.23.0

# Development tools
black>=23.0.0
flake8>=6.0.0
mypy>=1.5.0

# Logging and monitoring
colorlog>=6.7.0
"""

setup_instructions = """# Setup Instructions

## Prerequisites
- Python 3.8 or higher
- Git
- Access to Apache Jira (public, no authentication required)

## Installation Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd jira-scraper
```

2. Create a virtual environment:
```bash
python -m venv venv

# Activate on Linux/Mac:
source venv/bin/activate

# Activate on Windows:
venv\\Scripts\\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure project settings:
```bash
cp config/projects.yaml.example config/projects.yaml
# Edit config/projects.yaml to specify which Apache projects to scrape
```

5. Create necessary directories:
```bash
mkdir -p data/checkpoints data/output logs
```

## Configuration

Edit `config/projects.yaml`:
```yaml
projects:
  - KAFKA
  - SPARK
  - HADOOP

batch_size: 100
max_retries: 5
backoff_factor: 2
output_dir: data/output
checkpoint_dir: data/checkpoints
```

## Running the Scraper

Basic usage:
```bash
python -m jira_scraper.main
```

Resume from checkpoint:
```bash
python -m jira_scraper.main --resume
```

Scrape specific project:
```bash
python -m jira_scraper.main --project KAFKA
```

## Testing

Run all tests:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest --cov=jira_scraper tests/
```

## Output

The scraper generates:
- `data/output/<project_key>.jsonl` - Training data in JSONL format
- `data/checkpoints/<project_key>.json` - Checkpoint files for recovery
- `logs/scraper.log` - Detailed execution logs
"""

# Save files
with open('requirements.txt', 'w') as f:
    f.write(requirements_txt)

with open('setup_instructions.md', 'w') as f:
    f.write(setup_instructions)

# Create sample config file
config_yaml = """# Jira Scraper Configuration

# Apache Jira base URL
base_url: "https://issues.apache.org/jira"

# Projects to scrape (choose 3)
projects:
  - KAFKA
  - SPARK
  - HADOOP

# Scraping parameters
batch_size: 100  # Number of issues to fetch per API call
max_retries: 5   # Maximum retry attempts for failed requests
backoff_factor: 2  # Exponential backoff multiplier
timeout: 30  # Request timeout in seconds

# Output configuration
output_dir: "data/output"
checkpoint_dir: "data/checkpoints"
log_dir: "logs"

# Rate limiting
requests_per_minute: 60
respect_retry_after: true

# Data filtering
fields:
  - summary
  - description
  - status
  - priority
  - assignee
  - reporter
  - created
  - updated
  - labels
  - components

# LLM training task types to generate
task_types:
  - summarization
  - classification
  - question_answering
"""

with open('config_projects.yaml', 'w') as f:
    f.write(config_yaml)

print("Setup files created:")
print("- requirements.txt")
print("- setup_instructions.md")
print("- config_projects.yaml")
print("\nRequirements summary:")
print("- Core: requests, beautifulsoup4, PyYAML")
print("- Async: aiohttp (optional)")
print("- Testing: pytest, responses")
