import requests

class PDFDownloader:
    def __init__(self, urls):
        self.urls = urls

    def download(self):
        ml_papers = []
        for i, url in enumerate(self.urls):
            response = requests.get(url)
            filename = f"paper{i+1}.pdf"
            with open(filename, 'wb') as f:
                f.write(response.content)
            ml_papers.append(filename)
        return ml_papers