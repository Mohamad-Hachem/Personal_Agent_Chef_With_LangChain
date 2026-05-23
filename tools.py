from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient
from dotenv import load_dotenv
import logging

load_dotenv()
tavily_client = TavilyClient()

# configuration for logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for information"""

    logging.info("Agent is searching the web...")
    return tavily_client.search(query)