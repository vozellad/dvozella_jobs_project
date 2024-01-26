"""Contains values to not be made publicly available on github."""
from secrets import api_key

"""Scrapes and parses Google search results"""
from serpapi import GoogleSearch


def get_search_results():
    return GoogleSearch({
        "q": "coffee",
        "location": "Austin,Texas",
        "api_key": api_key
    })


def search_results_to_dict(search):
    return search.get_dict()


def verify_results(results):
    assert results["error"] is None


def main():
    search = get_search_results()
    results = search_results_to_dict(search)
    verify_results(results)
    print(results)


if __name__ == "__main__":
    main()
