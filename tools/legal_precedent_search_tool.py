# legal precedent search tool

#import libraries
import os

from dotenv import load_dotenv
from crewai.tools import tool
from tavily import TavilyClient 

load_dotenv()

# trusted indian legal domain 
LEGAL_SOURCES = [
    "indiankannon.org"
]

# function to check if url belongs to trusted legal domain 
def is_legal_source(url: str) -> bool:
    return any(domain in url for domain in LEGAL_SOURCES)

@tool("Legal Precedent Search Tool")
def search_legal_precedents(query:str) -> list[dict]:
    """
    Use Tavily Search to find precedent legal cases for a given legal issue.
    sample tool input: "Home trespassing and theft - precedent cases in India"

    Args:
        query (str): The structured legal issue or case summary.

    Returns:
        list[dict]: Relevant case titles, summaries, and links from trusted Indian legal sources.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("Tavily Api key not found")

    client = TavilyClient(api_key=api_key)

    # restrict search to only legal queries 
    search_query = f"site:{' OR site'.join(LEGAL_SOURCES)} {query}"

    response = client.search(
        query=search_query,
        max_results=10
    )
    raw_results= response.get("results", [])
    legal_results = [
        {
            "title":item.get("title"),
            "summary":item.get("content"),
            "link":item.get("url")

        }
        for item in raw_results
        if is_legal_source(item.get("url",""))
    ]

    return legal_results if legal_results else [
        {
            "title":"No relevant legal precedent found",
            "summary":"No matching results found from trusted Indian legal sources.",
            "link":"None" 
        }
    ]




