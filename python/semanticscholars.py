# from semanticscholar import SemanticScholar
# sch = SemanticScholar()
# query = "BCG Signal Processing"
# search_results = sch.search_paper(query, limit=10)

# for paper in search_results:
#     print(paper.title)


from semanticscholar import SemanticScholar
import markdown2
import os
from weasyprint import HTML

def search_and_summarize_papers(query, limit=5):
    sch = SemanticScholar()
    search_results = sch.search_paper(query, limit=limit)

    papers = []
    count = 0
    for paper in search_results:
        if count >= limit:
            break
        # print(paper)
        papers.append({
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "year": paper.year,
            "abstract": paper.abstract,
            "sch_url": paper.url,
            "citationCount": paper.citationCount,
            "bibtex": paper.citationStyles["bibtex"],
            "url": "https://doi.org/" + paper.externalIds["DOI"],
            "venue": paper.venue,
            "volume": paper.journal["volume"]
        })
        count += 1

    if not papers:
        return "No results found."
    else:
        print(f"Processed {len(papers)} papers")
        return papers


def create_markdown_report(papers, query):
    report = f"# Technical Review on {query}\n\n"
    report += "## Introduction\nThis report reviews recent publications on " + query + ".\n\n"

    for i, paper in enumerate(papers):
        report += f"## Paper {i+1}: {paper['title']}\n"
        report += f"**Authors:** {', '.join(paper['authors'])}\n"
        if paper['year']:
            report += f"**Year:** {paper['year']}\n"
        report += f"**URL:** {paper['url']}\n"
        report += f"**Abstract:** {paper['abstract']}\n\n"

    summary = "## Summary\n"
    summary += "Recent research in BCG signal processing focuses on diverse areas. "
    for i, paper in enumerate(papers):
        short_title = paper['title'].split(':')[0] if ':' in paper['title'] else paper['title']
        summary += f"[{i+1}] explored {short_title}. "


    report += summary

    return report


def create_pdf(markdown_content, filename):
    html = markdown2.markdown(markdown_content)
    HTML(string=html).write_pdf(filename)


query = "Detecting HR using BCG and IMU"
papers = search_and_summarize_papers(query, limit=1)
print(papers)

# if isinstance(papers, str): # Handle the case where no results are returned
#     print(papers)
# else:
#     markdown_report = create_markdown_report(papers, query)

#     with open("BCG_Signal_Processing_review.md", "w") as f:
#         f.write(markdown_report)
    
#     create_pdf(markdown_report, "BCG_Signal_Processing_review.pdf")

#     print("TERMINATE")

