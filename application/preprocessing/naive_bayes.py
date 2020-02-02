import enum


class NaiveBayesAvailable(enum.Enum):
    Laplace = 1


class NaiveBayes:
    @classmethod
    def __choose_bayes(cls,
                       bayes):
        """
        Lemmatizer choosing
        :type bayes: str
        """
        if bayes == NaiveBayesAvailable.Laplace.name:
            from nltk.classify import \
                NaiveBayesClassifier
            return NaiveBayesClassifier

    @classmethod
    def apply(cls,
              input,
              bayes) -> str:
        """
        Apply the chosen lemmatizer per your corpora
        :type input: object
        :type bayes: str
        """
        """
        Choose the available algorithm, which user has entered
        """
        algorithm = cls.__choose_bayes(
            bayes=bayes
        )()
        probability = algorithm.prob_classify(
            featureset={
                'unknown_words': True
            }
        ).prob(input)
        return probability
