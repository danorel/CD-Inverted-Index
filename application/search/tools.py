from .config import QUERY_SYMBOLS, DICTIONARY
from ..preprocessing import pipeline_input


def parse_query(
        query
) -> dict:
    """
    Parse the AND, OR and NOT operators
    :type query: str
    """
    token_value = dict()
    # If not operators defined in the query
    if (not (QUERY_SYMBOLS.OR in query)) and (not (QUERY_SYMBOLS.AND in query) and (not (QUERY_SYMBOLS.NOT in query))):
        print("No operator in usage")
        tokens = [
            pipeline_input(token)
            for token in query.split()
        ]
        for token in tokens:
            token_value[token] = True
        return token_value
    # If some operator from {AND, OR, NOT} was defined
    word = str()
    isAND, isNOT, isOR = False, False, False
    symbols = list(query_pipeline(query))
    for index, symbol in enumerate(symbols):
        if symbol == DICTIONARY[QUERY_SYMBOLS.NOT]:
            isNOT = True
        elif symbol == DICTIONARY[QUERY_SYMBOLS.OR]:
            if isNOT:
                token_value[pipeline_input(word)] = QUERY_SYMBOLS.NOT
            else:
                token_value[pipeline_input(word)] = QUERY_SYMBOLS.OR
            word, isNOT, isOR = "", False, True
        elif symbol == DICTIONARY[QUERY_SYMBOLS.AND]:
            if isNOT:
                token_value[pipeline_input(word)] = QUERY_SYMBOLS.NOT
            else:
                token_value[pipeline_input(word)] = QUERY_SYMBOLS.AND
            word, isNOT, isAND = "", False, True
        else:
            word += symbol
            if index == len(symbols) - 1:
                if isAND:
                    token_value[word] = QUERY_SYMBOLS.AND
                if isOR:
                    token_value[word] = QUERY_SYMBOLS.OR
                if isNOT:
                    token_value[word] = QUERY_SYMBOLS.NOT
    return token_value


def query_pipeline(
        query
):
    """
    Pipeline
    :type query: str
    """
    query = query.replace('(|)', '"')
    query = query.replace(
        QUERY_SYMBOLS.AND,
        DICTIONARY[QUERY_SYMBOLS.AND]
    )
    query = query.replace(
        QUERY_SYMBOLS.NOT,
        DICTIONARY[QUERY_SYMBOLS.NOT]
    )
    query = query.replace(
        QUERY_SYMBOLS.OR,
        DICTIONARY[QUERY_SYMBOLS.OR]
    )
    return ''.join(query.split())


def form_priority_query_dict(
        query_dict
) -> dict:
    """
    OR -> AND -> NOT
    :type query_dict: dict
    """
    priority_query_dict = dict()
    for key, value in query_dict.items():
        if value == QUERY_SYMBOLS.OR:
            priority_query_dict[key] = value
    for key, value in query_dict.items():
        if value == QUERY_SYMBOLS.AND:
            priority_query_dict[key] = value
    for key, value in query_dict.items():
        if value == QUERY_SYMBOLS.NOT:
            priority_query_dict[key] = value
    return priority_query_dict
