import enum


class Lemmatizers(enum.Enum):
    WordNetLemmatizer = 1


class Lemmatization:
    @classmethod
    def __choose_lemmatizer(cls,
                            lemmatizer):
        """
        Lemmatizer choosing
        :type lemmatizer: str
        """
        if lemmatizer == Lemmatizers.WordNetLemmatizer.name:
            from nltk import \
                WordNetLemmatizer
            return WordNetLemmatizer

    @classmethod
    def __tokenize(cls,
                   input) -> list:
        """
        Tokenization of input data
        :type input: object
        """
        from nltk.tokenize import \
            word_tokenize
        if isinstance(input, str):
            tokens = word_tokenize(
                text=input,
            )
        elif isinstance(input, list):
            tokens = [
                str(token)
                for token in input[:]
            ]
        else:
            raise AttributeError(
                "[ERROR]: Can't apply the tokenization for your input data. This operation could be applied only for input data type of list or str"
            )
        return tokens

    @classmethod
    def apply(cls,
              input,
              lemmatizer) -> str:
        """
        Apply the chosen lemmatizer per your corpora
        :type input: object
        :type lemmatizer: str
        """
        """
        Choose the available algorithm, which user has entered
        """
        algorithm = cls.__choose_lemmatizer(
            lemmatizer=lemmatizer
        )()
        """
        Lemmatize received tokens from function self.__tokenize()
        """
        lemmas = [
            algorithm.lemmatize(
                word=token
            )
            for token in cls.__tokenize(input)
        ]
        """
        Extract the text from the lemmatized tokens
        """
        corpus = " ".join(lemmas)
        return corpus
