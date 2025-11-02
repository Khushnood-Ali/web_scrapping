
# Create a comprehensive architecture overview as structured data
import json

architecture_overview = {
    "system_components": {
        "scraper": {
            "description": "Core scraping engine that fetches Jira data",
            "responsibilities": [
                "HTTP request management with retry logic",
                "Pagination handling (startAt/maxResults)",
                "Rate limit detection and exponential backoff",
                "Checkpoint-based state management"
            ],
            "key_classes": ["JiraClient", "PaginationManager", "RetryHandler"]
        },
        "transformer": {
            "description": "Data transformation pipeline",
            "responsibilities": [
                "Parse raw Jira JSON responses",
                "Extract relevant fields (issue, comments, metadata)",
                "Clean and normalize text content",
                "Generate LLM training tasks (summarization, QnA, classification)"
            ],
            "key_classes": ["IssueTransformer", "CommentExtractor", "TaskGenerator"]
        },
        "storage": {
            "description": "Persistent state and output management",
            "responsibilities": [
                "Checkpoint state persistence (pickle/json)",
                "JSONL output writing",
                "Progress tracking",
                "Error logging"
            ],
            "key_classes": ["CheckpointManager", "JSONLWriter", "Logger"]
        }
    },
    "data_flow": [
        "1. Initialize scraper with project keys",
        "2. Load last checkpoint (if exists)",
        "3. Fetch issues via Jira REST API with pagination",
        "4. For each issue: fetch comments and metadata",
        "5. Transform raw data to structured format",
        "6. Generate LLM training tasks",
        "7. Write to JSONL file",
        "8. Save checkpoint after each batch",
        "9. Repeat until all issues scraped"
    ],
    "edge_cases_handled": [
        "Network timeouts and connection errors",
        "HTTP 429 (rate limiting) with exponential backoff",
        "HTTP 5xx server errors with retry",
        "Empty/null fields in issue data",
        "Malformed JSON responses",
        "Interrupted execution (resume from checkpoint)",
        "Missing comments or metadata",
        "Special characters in text fields"
    ]
}

# Save as JSON
with open('architecture_overview.json', 'w') as f:
    json.dump(architecture_overview, f, indent=2)

print("Architecture Overview Created")
print(json.dumps(architecture_overview, indent=2))
