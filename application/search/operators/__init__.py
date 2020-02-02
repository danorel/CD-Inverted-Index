from ...extractors import extract_set_from


def intersection(
        f_inverted_index,
        s_inverted_index
) -> list:
    """
    Operator "AND"
    :type f_inverted_index: list
    :type s_inverted_index: list
    """
    if (not f_inverted_index) and (not s_inverted_index):
        return []
    if not f_inverted_index:
        return s_inverted_index
    if not s_inverted_index:
        return f_inverted_index
    intersections = []
    i, j = 0, 0
    while i < len(f_inverted_index) and j < len(s_inverted_index):
        if f_inverted_index[i] == s_inverted_index[j]:
            intersections.append(f_inverted_index[i])
            i += 1
            j += 1
        elif f_inverted_index[i] < s_inverted_index[j]:
            i += 1
        else:
            j += 1
    return intersections


def union(
        f_inverted_index,
        s_inverted_index
) -> list:
    """
    Operator "OR"
    :type f_inverted_index: list
    :type s_inverted_index: list
    """
    if (not f_inverted_index) and (not s_inverted_index):
        return []
    if not f_inverted_index:
        return s_inverted_index
    if not s_inverted_index:
        return f_inverted_index
    unions = []
    i, j = 0, 0
    while i < len(f_inverted_index) and j < len(s_inverted_index):
        if f_inverted_index[i] < s_inverted_index[j]:
            unions.append(f_inverted_index[i])
            i += 1
        elif s_inverted_index[j] < f_inverted_index[i]:
            unions.append(s_inverted_index[j])
            j += 1
        elif s_inverted_index[j] == f_inverted_index[i]:
            unions.append(f_inverted_index[i])
            i += 1
            j += 1
    while i < len(f_inverted_index):
        unions.append(f_inverted_index[i])
        i += 1
    while j < len(s_inverted_index):
        unions.append(s_inverted_index[j])
        j += 1
    return extract_set_from(unions)


def difference(
        f_inverted_index,
        s_inverted_index
) -> list:
    """
    Operator "OR"
    :type f_inverted_index: list
    :type s_inverted_index: list
    """
    if (not f_inverted_index) and (not s_inverted_index):
        return []
    if not f_inverted_index:
        return []
    if not s_inverted_index:
        return f_inverted_index
    differences = f_inverted_index[:]
    for index in s_inverted_index:
        if index in differences:
            differences.remove(index)
    return differences
