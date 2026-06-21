from newspaper import Article


def extract_article(url):

    try:

        article = Article(url)

        article.download()

        article.parse()

        return {
            "title": article.title,
            "content": article.text,
            "content_length": len(article.text)
        }

    except Exception as e:

        print(f"Extraction Error: {e}")

        return None