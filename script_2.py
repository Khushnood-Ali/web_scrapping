
# Create comprehensive project structure and README content
import csv

project_structure = {
    "directories": [
        "jira_scraper/",
        "jira_scraper/core/",
        "jira_scraper/utils/",
        "jira_scraper/transformers/",
        "tests/",
        "data/",
        "data/checkpoints/",
        "data/output/",
        "config/",
        "logs/"
    ],
    "files": [
        "README.md",
        "requirements.txt",
        "setup.py",
        ".env.example",
        ".gitignore",
        "jira_scraper/__init__.py",
        "jira_scraper/core/jira_client.py",
        "jira_scraper/core/retry_handler.py",
        "jira_scraper/core/checkpoint_manager.py",
        "jira_scraper/transformers/issue_transformer.py",
        "jira_scraper/transformers/task_generator.py",
        "jira_scraper/utils/jsonl_writer.py",
        "jira_scraper/utils/logger.py",
        "jira_scraper/main.py",
        "config/projects.yaml",
        "tests/test_jira_client.py",
        "tests/test_transformer.py"
    ]
}


edge_cases = [
    {
        "category": "Network Errors",
        "case": "Connection Timeout",
        "handling": "Retry with exponential backoff (max 5 attempts)",
        "implementation": "requests.Session with timeout=30, urllib3.Retry"
    },
    {
        "category": "Network Errors",
        "case": "HTTP 429 (Rate Limit)",
        "handling": "Exponential backoff with jitter, respect Retry-After header",
        "implementation": "Custom retry logic checking response headers"
    },
    {
        "category": "Network Errors",
        "case": "HTTP 5xx Server Error",
        "handling": "Retry up to 5 times with exponential backoff",
        "implementation": "Retry adapter with status_forcelist=[500,502,503,504]"
    },
    {
        "category": "Data Issues",
        "case": "Empty/Null Description",
        "handling": "Use empty string, skip certain tasks (e.g., summarization)",
        "implementation": "if not text: return '' pattern in transformer"
    },
    {
        "category": "Data Issues",
        "case": "Malformed JSON Response",
        "handling": "Log error, skip record, continue processing",
        "implementation": "try/except json.JSONDecodeError with logging"
    },
    {
        "category": "Data Issues",
        "case": "HTML in Text Fields",
        "handling": "Strip HTML tags, decode entities, normalize whitespace",
        "implementation": "re.sub(r'<[^>]+>', ''), html.unescape()"
    },
    {
        "category": "Data Issues",
        "case": "Missing Comments",
        "handling": "Treat as empty list, continue processing",
        "implementation": "comments.get('comments', [])"
    },
    {
        "category": "Pagination",
        "case": "Inconsistent Total Count",
        "handling": "Use isLast field or compare startAt with total",
        "implementation": "Check both conditions in pagination loop"
    },
    {
        "category": "Pagination",
        "case": "Empty Results Page",
        "handling": "Break pagination loop gracefully",
        "implementation": "if not issues: break"
    },
    {
        "category": "Recovery",
        "case": "Process Interruption",
        "handling": "Save checkpoint after each batch, resume from last position",
        "implementation": "CheckpointManager with atomic file writes"
    },
    {
        "category": "Recovery",
        "case": "Corrupted Checkpoint",
        "handling": "Fallback to starting from beginning with warning",
        "implementation": "try/except on load_checkpoint with logging"
    },
    {
        "category": "Authentication",
        "case": "Invalid/Expired Token",
        "handling": "Clear error message, exit gracefully",
        "implementation": "Check HTTP 401/403, raise custom AuthError"
    }
]


optimizations = [
    {
        "strategy": "Concurrent Requests",
        "description": "Use asyncio/aiohttp for parallel API calls",
        "benefit": "5-10x faster scraping for multiple projects",
        "tradeoff": "More complex code, need rate limiting coordination"
    },
    {
        "strategy": "Batch Processing",
        "description": "Process issues in batches (100-200 per API call)",
        "benefit": "Reduces number of API calls by 50-100x",
        "tradeoff": "Larger memory footprint per request"
    },
    {
        "strategy": "Incremental Updates",
        "description": "Only scrape issues updated since last run",
        "benefit": "90%+ reduction in data fetched for updates",
        "tradeoff": "Need to track timestamps, more complex logic"
    },
    {
        "strategy": "Connection Pooling",
        "description": "Reuse HTTP connections via requests.Session",
        "benefit": "15-20% faster requests due to TCP reuse",
        "tradeoff": "Minimal - best practice"
    },
    {
        "strategy": "Buffered Writing",
        "description": "Write JSONL in batches (100 records at a time)",
        "benefit": "Reduces I/O operations by 99%",
        "tradeoff": "Small risk of data loss if crash occurs"
    },
    {
        "strategy": "Field Filtering",
        "description": "Only request needed fields from Jira API",
        "benefit": "30-40% smaller response payloads",
        "tradeoff": "Need to know exact field names upfront"
    },
    {
        "strategy": "Compression",
        "description": "Enable gzip compression for API responses",
        "benefit": "50-70% bandwidth reduction",
        "tradeoff": "Slight CPU overhead for decompression"
    }
]


apache_projects = [
    {
        "project_key": "KAFKA",
        "name": "Apache Kafka",
        "description": "Distributed streaming platform",
        "reason": "Very active, diverse issue types, rich discussions"
    },
    {
        "project_key": "SPARK",
        "name": "Apache Spark",
        "description": "Unified analytics engine for big data",
        "reason": "Large volume of issues, technical depth, good for LLM training"
    },
    {
        "project_key": "HADOOP",
        "name": "Apache Hadoop",
        "description": "Framework for distributed storage and processing",
        "reason": "Long history, varied issue complexity, extensive metadata"
    },
    {
        "project_key": "CASSANDRA",
        "name": "Apache Cassandra",
        "description": "Distributed NoSQL database",
        "reason": "Active development, detailed technical discussions"
    },
    {
        "project_key": "AIRFLOW",
        "name": "Apache Airflow",
        "description": "Platform to programmatically author, schedule and monitor workflows",
        "reason": "Modern project, good documentation in issues"
    }
]

with open('edge_cases_handling.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['category', 'case', 'handling', 'implementation'])
    writer.writeheader()
    writer.writerows(edge_cases)


with open('optimization_strategies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['strategy', 'description', 'benefit', 'tradeoff'])
    writer.writeheader()
    writer.writerows(optimizations)


with open('recommended_apache_projects.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['project_key', 'name', 'description', 'reason'])
    writer.writeheader()
    writer.writerows(apache_projects)

print(f"Documentation created:")
print(f"- {len(edge_cases)} edge cases documented")
print(f"- {len(optimizations)} optimization strategies")
print(f"- {len(apache_projects)} Apache projects recommended")
print(f"\nRecommended Apache Jira Projects:")
for p in apache_projects[:3]:
    print(f"  {p['project_key']}: {p['name']}")
