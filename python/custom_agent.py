import autogen
from semanticscholar import SemanticScholar

class TechnicalReviewAgent(autogen.AssistantAgent):
    def __init__(self, topic):
        super().__init__(name="TechnicalReviewAgent")
        self.topic = topic
        self.filename = 'technical_review.md'
        self.sch = SemanticScholar()

    def create_file(self):
        with open(self.filename, 'w') as f:
            f.write('')

    def get_publications(self):
        results = self.sch.search_paper(query=self.topic, limit=5)
        publications = []
        for r in results:
            print(r)
            publications.append({
                'title': r['title'],
                'authors': r['authors'],
                'abstract': r['abstract'],
                'url': r['url']
            })
            if len(publications) == 5:
                break
        return publications

    def append_title(self):
        with open(self.filename, 'a') as f:
            f.write("# Technical Review: " + self.topic + "\n\n")

    def append_publications(self, publications):
        with open(self.filename, 'a') as f:
            for pub in publications:
                f.write("## " + pub['title'] + "\n")
                f.write("Authors: " + ", ".join(pub['authors']) + "\n")
                f.write("Abstract: " + pub['abstract'] + "\n")
                f.write("URL: " + pub['url'] + "\n\n")

    def summarize_abstracts(self, publications):
        abstracts = " ".join([pub['abstract'] for pub in publications])
        summary = "Summary: " + abstracts[:300] + "..."
        return summary

    def append_summary(self, summary):
        with open(self.filename, 'a') as f:
            f.write("## Summary\n")
            f.write(summary + "\n\n")

    def generate_references(self, publications):
        references = []
        for pub in publications:
            references.append(pub['url'])
        return references

    def append_references(self, references):
        with open(self.filename, 'a') as f:
            f.write("## References\n")
            for ref in references:
                f.write("- " + ref + "\n")

    def run(self):
        self.create_file()
        publications = self.get_publications()
        self.append_title()
        self.append_publications(publications)
        summary = self.summarize_abstracts(publications)
        self.append_summary(summary)
        references = self.generate_references(publications)
        self.append_references(references)

if __name__ == "__main__":
    agent = TechnicalReviewAgent("BCG and IMU for HRV detection")
    agent.run()
