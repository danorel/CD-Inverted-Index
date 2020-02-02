from nltk import ngrams
from nltk.tokenize import RegexpTokenizer
from string import \
    digits, \
    punctuation

from application.preprocessing.lemmatization import \
    Lemmatization
from application.preprocessing.stopwords import \
    StopwordsCleaner
from application.preprocessing.naive_bayes import \
    NaiveBayes
from application.preprocessing.stemming import \
    Stemming

from application.extractors import extract_set_from


def pipeline_input(
        input
) -> str:
    """
    Preprocessing Pipeline
    :type input: str
    """
    output = StopwordsCleaner.apply(
        input=input,
        language='english'
    )
    output = Lemmatization.apply(
        input=output,
        lemmatizer="WordNetLemmatizer"
    )
    output = Stemming.apply(
        input=output,
        stemmer='PorterStem'
    )
    output = output \
        .translate(
            str.maketrans("", "", digits)
        )
    output = output \
        .translate(
            str.maketrans("", "", punctuation)
        )
    return output


def tokenize_corpora(
        corpora
):
    """
    Manual Tokenizator
    :type corpora: str
    """
    return RegexpTokenizer(
        pattern=r"\b[\w+.]+\b"
    ).tokenize(corpora.lower())


def tokenize_corpora_into_dict(
        corpora
):
    """
    Manual Tokenizator
    :type corpora: str
    """
    tokens = RegexpTokenizer(
        pattern=r"\b[\w+.]+\b"
    ).tokenize(corpora.lower())
    return extract_set_from(
        obj=tokens
    )


def ngram_tokens(
        tokens,
        n
) -> list:
    """
    Ngram processing
    :type tokens: list
    :type n: int
    """
    return list(
        ngrams(
            sequence=tokens,
            n=n
        )
    )
