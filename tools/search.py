from duckduckgo_search import DDGS


def search_web(query, max_results=5):

    links = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)

        for r in results:
            links.append(r["href"])

    return links