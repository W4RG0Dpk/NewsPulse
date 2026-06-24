import re


def clean_text(text):

    if not text:
        return ""

    # normalize whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # normalize smart quotes
    text = text.replace("“", '"')
    text = text.replace("”", '"')
    text = text.replace("’", "'")

    # remove leading/trailing spaces
    text = text.strip()

    return text