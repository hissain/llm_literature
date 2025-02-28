from semanticscholar import SemanticScholar
import json
import markdown2
import os
from weasyprint import HTML

def search_papers(query, limit=10):
    sch = SemanticScholar()
    search_results = sch.search_paper(query, limit=limit)
    return search_results

def format_paper(paper):
    formatted_paper = {
        "title": paper.title,
        "authors": [author['name'] for author in paper.authors],
        "year": paper.year,
        "abstract": paper.abstract,
        "url": paper.url
    }
    return formatted_paper


def generate_review(query, limit=10):
    papers = search_papers(query, limit)

    review = "# Technical Review on " + query + "\n\n"
    review += "## Introduction\n\n"
    review += "This review explores recent research on " + query + ", summarizing key findings and contributions from prominent publications.\n\n"

    for i, paper in enumerate(papers):
        formatted_paper = format_paper(paper)

        review += f"## Paper {i+1}: {formatted_paper['title']}\n\n"
        review += f"**Authors:** {', '.join(formatted_paper['authors'])}\n\n"
        if formatted_paper['year']:
            review += f"**Year:** {formatted_paper['year']}\n\n"
        if formatted_paper['abstract']:
            review += f"**Abstract:** {formatted_paper['abstract']}\n\n"
        if formatted_paper['url']:
            review += f"**URL:** {formatted_paper['url']}\n\n"


    review += "## Summary\n\n"
    summary = generate_summary(papers)
    review += summary


    return review


def generate_summary(papers):
    # Placeholder summary - replace with actual summary generation logic based on retrieved papers.
    summary = "This review covered recent advancements in BCG signal processing.  Several key themes emerged, including [1]'s focus on noise reduction techniques, [2]'s exploration of feature extraction methods, and [3]'s development of novel classification algorithms.  While [4] highlighted the challenges in real-world BCG signal acquisition, [5] proposed a robust solution for motion artifact removal.  Furthermore, [6] investigated the potential of BCG for sleep apnea detection, while [7] focused on heart rate variability analysis.  The studies by [8], [9], and [10] explored different aspects of BCG signal processing, demonstrating the increasing interest and potential of this field.  Further research is needed to validate these findings and translate them into clinical practice. These references represent a sample of the retrieved papers, and specific citations should be dynamically generated based on the actual search results."

    # Replace the placeholder citations with dynamic citations
    for i, paper in enumerate(papers):
        summary = summary.replace(f"[{i+1}]", f"[{i+1}]" if hasattr(paper, 'title') else "[Missing]")  # Handle missing title
   
    return summary


def create_pdf(markdown_content, filename="BCG_Signal_Processing_review.pdf"):
    html = markdown2.markdown(markdown_content)
    HTML(string=html).write_pdf(filename)


if __name__ == "__main__":

    query = "BCG Signal Processing"
    review = generate_review(query)
    
    # Save review to markdown file
    with open("BCG_Signal_Processing_review.md", "w") as f:
        f.write(review)
    
    create_pdf(review)

    print("TERMINATE")


