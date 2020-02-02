

class NGramPreprocess:
    _ngrams = None
    _n      = None

    @classmethod
    def __choose_ngram(cls,
                       input,
                       n) -> list:
        """
        Split the input data into the n-grams
        :type input: object
        :type n: int
        """
        from nltk import \
            ngrams
        if isinstance(input, list):
            input = '\s'.join([
                str(token)
                for token in input
            ])
        from nltk import word_tokenize
        return ngrams(
            sequence=word_tokenize(input),
            n=n
        )

    @classmethod
    def __next(cls,
               text,
               probabilities,
               unknown_symbol="</Unk>") -> str:
        """
        Predict the next word from the probabilities Counter
        :type text: str
        :type probabilities: collections.Counter
        :type unknown_symbol: str
        """
        from re import \
            split
        last = split(
            pattern='\s',
            string=text
        )[-1]
        # Markov ngram model of evaluating the next `word`
        elements = [
            ngram[-1] # Taking the last element from ngram tuple
            for ngram, freq in probabilities.most_common(
                n=len(probabilities.keys())
            )
            if ngram[-2] == last # Check if the previous element equals the finding one
        ]
        if elements:
            return elements[0] # Returning the element with the biggest frequency rate
        else:
            return unknown_symbol # If not found - returning the </Unk> symbol

    @classmethod
    def apply(cls,
              input,
              n):
        """
        Apply the chosen lemmatizer per your corpora
        :type input: object
        :type n: int
        """
        """
        Choose the available algorithm, which user has entered
        """
        cls._ngrams = cls.__choose_ngram(
            input=input,
            n=n
        )
        cls._n = n

    @classmethod
    def predict(cls,
                text,
                k=3) -> str:
        if not cls._ngrams:
            raise AttributeError(
                "Prediction could not be started!. Apply some corpus per class!"
            )
        """
        Define the counter per each ngram
        Calculating the general frequency rate for each ngram
        """
        from collections import \
            Counter
        probabilities = Counter(cls._ngrams)
        """
        Making the prediction per received ngram frequencies
        """
        answer = text
        for iteration in range(0, k):
            answer = ' '.join([
                answer,
                cls.__next(
                    text=answer,
                    probabilities=probabilities
                )
            ])
        return answer
