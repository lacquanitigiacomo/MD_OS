"""Search the web using DuckDuckGo HTML endpoint (no API key). Falls back to offline mode if no network."""
import re
import requests
from bs4 import BeautifulSoup
from .base import BaseAgent


class WebSearchAgent(BaseAgent):
    def execute(self, inputs, config):
        query = config.get("query", "")
        if not query:
            if inputs:
                first = list(inputs.values())[0]
                if isinstance(first, str):
                    query = first
                elif isinstance(first, dict) and "query" in first:
                    query = first["query"]

        if not query:
            return {"error": "No query provided. Set 'query' in node config or pass a string from a predecessor."}

        max_results = config.get("max_results", 5)
        offline_mode = config.get("offline_mode", False)

        if offline_mode:
            return {
                "agent": "web_search",
                "query": query,
                "results": [
                    {"title": f"Mock result 1 for '{query}'", "url": "https://example.com/1", "snippet": "Offline placeholder result."},
                    {"title": f"Mock result 2 for '{query}'", "url": "https://example.com/2", "snippet": "Another offline placeholder."},
                ],
                "count": 2,
                "note": "offline_mode",
            }

        try:
            url = "https://html.duckduckgo.com/html/"
            resp = requests.post(url, data={"q": query, "kl": "us-en"}, timeout=15, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            })
            resp.raise_for_status()
        except Exception as exc:
            return {
                "agent": "web_search",
                "query": query,
                "results": [],
                "count": 0,
                "error": f"Network request failed: {exc}",
            }

        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for result in soup.select(".result")[:max_results]:
            title_tag = result.select_one(".result__a")
            snippet_tag = result.select_one(".result__snippet")
            if title_tag:
                results.append({
                    "title": title_tag.get_text(strip=True),
                    "url": title_tag.get("href", ""),
                    "snippet": snippet_tag.get_text(strip=True) if snippet_tag else "",
                })

        return {
            "agent": "web_search",
            "query": query,
            "results": results,
            "count": len(results),
        }
