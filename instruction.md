There is an Apache-style access log at /app/access.log. Parse it and write a JSON
summary to /app/report.json with the following keys:

- "total_requests": total number of log entries (integer)
- "unique_ips":     number of distinct client IP addresses (integer)
- "top_path":       the most frequently requested URL path (string)