import json
from pathlib import Path


def _load_report():
    path = Path("/app/report.json")
    assert path.exists(), "no report.json found"
    data = json.loads(path.read_text())
    assert isinstance(data, dict), "report.json must be a JSON object"
    return data


def test_total_requests():
    """Agent correctly counted total requests."""
    data = _load_report()
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """Agent correctly counted unique IPs."""
    data = _load_report()
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """Agent correctly identified the most-requested path."""
    data = _load_report()
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )