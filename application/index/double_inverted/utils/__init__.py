from collections import defaultdict

from ...double_inverted import \
    build_doubly_matrix_incidence_df


def build_doubly_inverted_index(
        working_dir,
        file_extension
) -> defaultdict:
    """
    Construction of the double inverted index
    :type working_dir: str
    :type file_extension: str
    """
    invert_index = defaultdict()
    matrix_df = build_doubly_matrix_incidence_df(
        working_dir=working_dir,
        file_extension=file_extension
    )

    for index, row in matrix_df.iterrows():
        invert_index[index] = [
            file_index
            for file_index, file_value in enumerate(list(row))
            if file_value
        ]
    return invert_index
