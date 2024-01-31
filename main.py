"""Contains values to not be made publicly available on github."""
from secrets import api_key

"""Scrapes and parses Google search results"""
from serpapi import GoogleSearch


def get_search_results(page_num):
    # 10 results per page. Every 10 results is start of page.
    page = (page_num - 1) * 10

    return GoogleSearch({
        "engine": "google_jobs",
        "q": "software developer",
        "location": "Boston,Massachusetts",
        "api_key": api_key,
        "start": page
    }).get_dict()


def store_search_results(results, page_num):
    with open(f"results{page_num}.txt", "w") as file:
        for key, value in results.items():
            file.write('%s: %s\n' % (key, value))


def main():
    for page_num in range(1, 6):
        results = get_search_results(page_num)
        store_search_results(results, page_num)


if __name__ == "__main__":
    main()
