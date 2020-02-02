import enum


class Languages(enum.Enum):
    ukrainian = 1


class StopwordsCleaner:
    @classmethod
    def __choose_language(cls,
                          language) -> list:
        """
        Lemmatizer choosing
        :type language: str
        """
        # NOT DONE YET
        if language == Languages.ukrainian.name:
            return []
        else:
            from nltk.corpus import \
                stopwords
            return stopwords.words(language)

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
              language) -> str:
        """
        Apply the chosen lemmatizer per your corpora
        :type input: object
        :type language: str
        """
        """
        Choose the stopwords vocabulary list, which contains all available stop-words of entered language
        """
        stopwords = cls.__choose_language(
            language=language
        )
        """
        Lemmatize received tokens from function self.__tokenize()
        """
        cleaned = [
            token
            for token in cls.__tokenize(input)
            if not (token in stopwords)
        ]
        """
        Extract the text from the lemmatized tokens
        """
        return ' '.join(cleaned)
