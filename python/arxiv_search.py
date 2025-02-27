
import json
import arxiv
from rich.console import Console
from rich.table import Table

def pretty_print(item):
  console = Console()
  with console.pager(styles=False):
    console.print(item, markup=False)

def arxiv_search(query: str, max_results: int = 10) -> list:
    """
    Search arXiv for papers and return the results including additional metadata.
    """
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance)

    results = []
    for paper in client.results(search):
        try:
            results.append(
                {
                    "title": paper.title,
                    "authors": [author.name for author in paper.authors],
                    "published": paper.published.strftime("%Y-%m-%d"),
                    "updated": paper.updated.strftime("%Y-%m-%d"),  # Date of the latest version
                    "abstract": paper.summary,
                    "pdf_url": paper.pdf_url,
                    "primary_category": paper.primary_category,
                }
            )
        except Exception as e:
           print(e)
    
    with open('generated/arxiv_search_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    return results


result = arxiv_search("VFI interpolation of intermediate video frame, literature review")
print(result)