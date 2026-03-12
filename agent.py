from tools.search import search_web
from tools.scraper import scrape_page
from services.summarizer import summarize_research


def research_topic(query):

    links = search_web(query)

    collected_text = ""

    for link in links[:3]:

        page_text = scrape_page(link)

        collected_text += page_text

    summary = summarize_research(collected_text)

    return summary, links