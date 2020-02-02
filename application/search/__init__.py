from .config import QUERY_SYMBOLS, DICTIONARY
from .tools import \
    parse_query, \
    form_priority_query_dict
from .operators import \
    union, \
    intersection, \
    difference


def boolean_search(
        query,
        inverted_index
) -> list:
    """
    Implementation of the boolean search by keywords: {"AND", "OR"}
    :type query: str,
    :type inverted_index: defaultdict
    """
    resulting_index = []
    # Extracting the dict of key/value pairs, where key is token
    query_dict = parse_query(query)
    # Sorting the query dict by priority OR -> AND -> NOT
    query_dict = form_priority_query_dict(query_dict)
    tokens = query_dict.keys()
    indices = [inverted_index.get(token, []) for token in tokens]
    for index, token in zip(indices, tokens):
        print(f"{token} -> {index} : {query_dict[token]}")
        if query_dict[token] == QUERY_SYMBOLS.OR:
            resulting_index = union(
                f_inverted_index=resulting_index,
                s_inverted_index=index
            )
        if query_dict[token] == QUERY_SYMBOLS.NOT:
            resulting_index = difference(
                f_inverted_index=resulting_index,
                s_inverted_index=index
            )
        if query_dict[token] == QUERY_SYMBOLS.AND:
            resulting_index = intersection(
                f_inverted_index=resulting_index,
                s_inverted_index=index
            )
    return resulting_index
