import re


def create_chunks(
    text,
    max_words=500
):

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text
    )

    chunks = []

    current_chunk = []

    current_words = 0

    for sentence in sentences:

        word_count = len(
            sentence.split()
        )

        if (
            current_words + word_count
            > max_words
        ):

            chunks.append(
                " ".join(
                    current_chunk
                )
            )

            current_chunk = []

            current_words = 0

        current_chunk.append(
            sentence
        )

        current_words += word_count

    if current_chunk:

        chunks.append(
            " ".join(
                current_chunk
            )
        )

    return chunks