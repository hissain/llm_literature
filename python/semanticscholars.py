# from semanticscholar import SemanticScholar
# sch = SemanticScholar()
# query = "machine learning algorithms"
# search_results = sch.search_paper(query, limit=10)

# for paper in search_results:
#     print(paper.title)



try:
    from semanticscholar import SemanticScholar
    from markdown2 import markdown
    from weasyprint import HTML
except ModuleNotFoundError:
    print("Error: Required packages not found. Please install them using:")
    print("pip install semanticscholar markdown2 weasyprint")
    exit(1)

def search_papers(query, year_limit=None):
    sch = SemanticScholar()
    search_results = sch.search_paper(query, limit=10)

    filtered_results = []
    for paper in search_results:
        if year_limit is None or (paper.year is not None and paper.year >= year_limit):
             filtered_results.append(paper)
    return filtered_results

def create_review_document(query, year_limit=None):
    papers = search_papers(query, year_limit)

    if not papers:
        return "No papers found."

    review = "# Technical Review on " + query + "\n\n"
    review += "## Introduction\n\n"
    review += "This review explores recent advancements in " + query + ". It summarizes key findings from relevant publications, highlighting current trends and challenges in the field.\n\n"

    review += "## Paper Summaries\n\n"

    summary_texts = []
    for paper in papers:
        review += f"### {paper.title}\n\n"
        review += f"* **Authors:** {', '.join(paper.authors)}\n" if paper.authors else ""
        review += f"* **Year:** {paper.year}\n" if paper.year else ""
        review += f"* **Venue:** {paper.venue}\n" if paper.venue else ""
        review += f"* **DOI:** [{paper.doi}]({paper.doi})\n\n" if paper.doi else ""
        abstract = paper.abstract if paper.abstract else "Abstract not available."
        review += f"* **Abstract:** {abstract}\n\n"

        summary_texts.append(abstract)

    review += "## Summary of Publications\n\n"

    overall_summary = f"Research in {query} has shown significant progress. "
    overall_summary += ". ".join([f"[{i+1}] explored {summary}" for i, summary in enumerate(summary_texts)])
    word_count = len(overall_summary.split())
    if word_count > 150:
        overall_summary = " ".join(overall_summary.split()[:150]) + "..."


    review += overall_summary + "\n\n"
    references = ""
    for i, paper in enumerate(papers):
        references += f"[{i+1}] {', '.join(paper.authors)}, \"{paper.title},\""
        references += f" *{paper.venue}*, " if paper.venue else ""
        references += str(paper.year) if paper.year is not None else ""
        references += ".\n"

    review += "## References\n\n"
    review += references

    return review


def create_pdf(markdown_content, filename):
    html = markdown(markdown_content)
    HTML(string=html).write_pdf(filename)

query = "BCG Signal Processing"
review_document = create_review_document(query, year_limit=2018)

if review_document:
    create_pdf(review_document, "BCG_Signal_Processing_review2.pdf")
    print("TERMINATE")
else:
    print("CONTINUE")
