"""Contains values to not be made publicly available on github."""
from secrets import api_key

"""Scrapes and parses Google search results"""
from serpapi import GoogleSearch


def get_search_results():
    return GoogleSearch({
        "q": "coffee",
        "location": "Austin,Texas",
        "api_key": api_key
    }).get_dict()


def store_search_results(results):
    with open("results.txt", "w") as file:
        for key, value in results.items():
            file.write('%s: %s\n' % (key, value))


def main():
    results = get_search_results()
    store_search_results(results)
    print(results)


if __name__ == "__main__":
    main()
