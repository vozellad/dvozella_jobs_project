"""Contains values to not be made pubicly available on github."""
from secrets import api_key

"""..."""
from serpapi import GoogleSearch

search = GoogleSearch({
    "q": "coffee",
    "location": "Austin,Texas",
    "api_key": "<your secret api key>"
})
result = search.get_dict()


def main():
    print("Hello, world!")
    print(api_key)


if __name__ == "__main__":
    main()
