from langchain_community.document_loaders import FireCrawlLoader
from dotenv import load_dotenv

load_dotenv()
#TODO: FIx it
def ingest_data() -> None:

    tanibilet_offers_base_url = "https://tanibilet.eu/oferty-dnia/"
    print(f"Crawling data from {tanibilet_offers_base_url}")

    loader = FireCrawlLoader(
        url=tanibilet_offers_base_url,
        mode="crawl",
        params={
            "crawlerOptions": {"limit": 3},
            "onlyMainContent": True,
        },
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    return documents

if __name__ == "__main__":
    ingest_data()

