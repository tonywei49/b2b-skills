#!/usr/bin/env python3
# tavily.py -- Tavily Search API Wrapper

import sys
import json
import argparse
import urllib.request
import urllib.error
import time

BASE_URL = "https://api.tavily.com"
API_KEY = "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"

def poll_result(request_id, max_wait=60):
    """轮询 research 任务结果"""
    poll_url = BASE_URL + "/research/" + request_id + "/result"
    headers = {"Authorization": "Bearer " + API_KEY}
    waited = 0
    interval = 2
    while waited < max_wait:
        req = urllib.request.Request(poll_url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                status = result.get("status", "")
                if status == "completed":
                    print(json.dumps(result, ensure_ascii=False, indent=2))
                    return result
                elif status == "failed":
                    print("Research task failed: {}".format(result), file=sys.stderr)
                    sys.exit(1)
                else:
                    print("Research {}... waiting {}s".format(status, interval), file=sys.stderr)
                    time.sleep(interval)
                    waited += interval
        except urllib.error.HTTPError as e:
            print("HTTP Error {}: {}".format(e.code, e.read().decode()), file=sys.stderr)
            sys.exit(1)
    print("Timeout waiting for research result", file=sys.stderr)
    sys.exit(1)

def do_search(query, search_depth="basic", max_results=5, topic="general"):
    url = BASE_URL + "/search"
    payload = {"api_key": API_KEY, "query": query, "search_depth": search_depth, "max_results": max_results, "topic": topic}
    return post(url, payload)

def do_research(topic, model="auto"):
    url = BASE_URL + "/research"
    payload = {"api_key": API_KEY, "input": topic, "model": model}
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + API_KEY}
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("status") == "pending":
                request_id = result.get("request_id")
                print("Research task submitted, polling for result... (request_id: {})".format(request_id), file=sys.stderr)
                return poll_result(request_id)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        print("HTTP Error {}: {}".format(e.code, error_body), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("ERROR: {}".format(e), file=sys.stderr)
        sys.exit(1)

def do_extract(url):
    req_url = BASE_URL + "/extract"
    payload = {"api_key": API_KEY, "urls": [url]}
    return post(req_url, payload)

def do_crawl(url, max_depth=2, max_urls=10):
    map_url = BASE_URL + "/map"
    map_payload = {"api_key": API_KEY, "url": url, "max_depth": max_depth, "max_urls": max_urls}
    map_result = post(map_url, map_payload)
    if "discovered_urls" in map_result and map_result["discovered_urls"]:
        urls_to_crawl = map_result["discovered_urls"][:max_urls]
        crawl_url = BASE_URL + "/crawl"
        crawl_payload = {"api_key": API_KEY, "urls": urls_to_crawl}
        return post(crawl_url, crawl_payload)
    return map_result

def post(url, payload):
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        print("HTTP Error {}: {}".format(e.code, error_body), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("ERROR: {}".format(e), file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Tavily Search API CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_search = sub.add_parser("search", help="Web search")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--depth", default="basic", choices=["basic","advanced","fast","ultra-fast"])
    p_search.add_argument("--max-results", type=int, default=5)
    p_search.add_argument("--topic", default="general", choices=["general","news"])

    p_research = sub.add_parser("research", help="Deep research with auto multi-search + report")
    p_research.add_argument("topic", help="Research topic")
    p_research.add_argument("--model", default="auto", choices=["pro","mini","auto"])

    p_extract = sub.add_parser("extract", help="Extract content from URL(s)")
    p_extract.add_argument("url", help="URL to extract from")

    p_crawl = sub.add_parser("crawl", help="Site map crawl + extract")
    p_crawl.add_argument("url", help="Start URL")
    p_crawl.add_argument("--max-depth", type=int, default=2)
    p_crawl.add_argument("--max-urls", type=int, default=10)

    args = parser.parse_args()
    if args.cmd == "search":
        do_search(args.query, args.depth, args.max_results, args.topic)
    elif args.cmd == "research":
        do_research(args.topic, args.model)
    elif args.cmd == "extract":
        do_extract(args.url)
    elif args.cmd == "crawl":
        do_crawl(args.url, args.max_depth, args.max_urls)

if __name__ == "__main__":
    main()
