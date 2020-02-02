import enum


class Stemmers(enum.Enum):
    PorterStem       = 1
    SnowballStemmer  = 2
    LancasterStemmer = 3


class Stemming:
    @classmethod
    def __choose_stemmer(cls,
                         stemmer):
        """
        Lemmatizer choosing
        :type stemmer: str
        """
        if stemmer == Stemmers.PorterStem.name:
            from nltk.stem import \
                PorterStemmer
            return PorterStemmer
        if stemmer == Stemmers.SnowballStemmer.name:
            from nltk.stem import \
                SnowballStemmer
            return SnowballStemmer
        if stemmer == Stemmers.LancasterStemmer.name:
            from nltk.stem import \
                LancasterStemmer
            return LancasterStemmer

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
              stemmer) -> str:
        """
        Apply the chosen lemmatizer per your corpora
        :type input: object
        :type stemmer: str
        """
        """
        Choose the available algorithm, which user has entered
        """
        algorithm = cls.__choose_stemmer(
            stemmer=stemmer
        )()
        """
        Lemmatize received tokens from function self.__tokenize()
        """
        stems = [
            algorithm.stem(
                word=token
            )
            for token in cls.__tokenize(input)
        ]
        """
        Extract the text from the lemmatized tokens
        """
        return ' '.join(stems)
