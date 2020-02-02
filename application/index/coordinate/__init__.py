

from collections import defaultdict

from .utils import build_coordinate_matrices_df


def build_coordinate_index(
        working_dir,
        file_extension
) -> defaultdict:
    """
    Construction of the double inverted index.
    [
        "token1": (
            documentID1,
            frequency: [position1, position2, ..., positionN]
        ),
        "token2": (
            documentID2,
            frequency: [position1, position2, ..., positionM]
        ),
    ]
    Structure:
    dict(
        key="str" (token name)
        value="tuple" (documentID, frequency, positionList)
    )
    :type working_dir: str
    :type file_extension: str
    """
    invert_index = defaultdict()

    df_incidence, df_frequency, df_position = build_coordinate_matrices_df(
        working_dir=working_dir,
        file_extension=file_extension
    )

    for (i_index, i_row), (f_index, f_row), (p_index, p_row) in zip(df_incidence.iterrows(), df_frequency.iterrows(), df_position.iterrows()):
        IDs = [
            file_index
            for file_index, file_value in enumerate(list(i_row))
            if file_value
        ]
        frequencies = [
            freq_value
            for freq_index, freq_value in enumerate(list(f_row))
            if freq_index in IDs
        ]
        positions = [
            pos_value
            for pos_index, pos_value in enumerate(list(p_row))
            if pos_index in IDs
        ]
        invert_index[i_index] = [
            (identifier, freq, pos)
            for identifier, freq, pos in zip(IDs, frequencies, positions)
        ]

    return invert_index
