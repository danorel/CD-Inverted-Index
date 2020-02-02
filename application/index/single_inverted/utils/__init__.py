from collections import defaultdict

from ...single_inverted import \
    build_singly_matrix_incidence_df


def build_singly_inverted_index(
        working_dir,
        file_extension
) -> defaultdict:
    """
    Construction of the singly inverted index
    :type working_dir: str
    :type file_extension: str
    """
    invert_index = defaultdict()
    matrix_df = build_singly_matrix_incidence_df(
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
