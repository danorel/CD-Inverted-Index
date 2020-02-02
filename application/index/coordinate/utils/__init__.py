import numpy
import pandas as pd

from application.preprocessing import \
    pipeline_input, \
    tokenize_corpora, \
    tokenize_corpora_into_dict
from application.extractors import \
    extract_corpora_from_dir, \
    extract_corpora_from_file
from application.helpers.dir import dir_files_by_extension


def build_coordinate_matrix_incidence(
        working_dir,
        file_extension
) -> tuple:
    """
    Construction of the matrix incidence between files in working directory and their tokens
    :type working_dir: str
    :type file_extension: str
    """
    filepath_list = dir_files_by_extension(
        working_dir=working_dir,
        file_extension=file_extension
    )

    corpora = pipeline_input(
        input=extract_corpora_from_dir(
            working_dir=working_dir,
            file_extension=file_extension
        )
    )
    tokens = tokenize_corpora_into_dict(corpora)

    files_corporas = []
    for file_index, filepath in enumerate(filepath_list):
        file_corpora = extract_corpora_from_file(
            filepath=filepath,
            file_index=file_index,
            file_extension=file_extension
        )
        files_corporas.append(file_corpora)

    incidence_matrix = build_coordinate_matrix_incidence_ndarray(
        files_corporas=files_corporas,
        tokens=tokens
    )

    frequency_matrix = build_coordinate_matrix_frequency_ndarray(
        files_corporas=files_corporas,
        tokens=tokens
    )

    position_matrix = build_coordinate_matrix_positions_ndarray(
        files_corporas=files_corporas,
        tokens=tokens
    )
    return incidence_matrix, frequency_matrix, position_matrix, tokens


def build_coordinate_matrix_incidence_ndarray(
        files_corporas,
        tokens
) -> numpy.ndarray:
    """

    :type files_corporas: list
    :type tokens: list
    """
    print("Initialization of the incidence matrix...")
    incidence_matrix = numpy.zeros(
        (
            files_corporas.__len__(),
            tokens.__len__()
        )
    )
    print(incidence_matrix)
    print(f"Matrix shape: {incidence_matrix.shape}")

    print("Processing the matrix...")
    # Calculate the token-document existence
    for file_index, file_corpora in enumerate(files_corporas):
        file_output = pipeline_input(file_corpora)
        file_dict = tokenize_corpora_into_dict(file_output)
        for token_index, token in enumerate(tokens):
            incidence_matrix[file_index][token_index] = token in file_dict
    print("Processing ended successfully!")

    print(incidence_matrix)
    return incidence_matrix


def build_coordinate_matrix_frequency_ndarray(
        files_corporas,
        tokens
) -> numpy.ndarray:
    """

    :type files_corporas: list
    :type tokens: list
    """
    print("Initialization of the frequency matrix...")
    frequency_matrix = numpy.zeros(
        (
            files_corporas.__len__(),
            tokens.__len__()
        )
    )
    print(frequency_matrix)
    print(f"Matrix shape: {frequency_matrix.shape}")

    for file_index, file_corpora in enumerate(files_corporas):
        file_output = pipeline_input(file_corpora)
        file_tokens = tokenize_corpora(file_output)
        for token_index, token in enumerate(tokens):
            frequency_matrix[file_index][token_index] = calculate_token_freq(
                file_tokens=file_tokens,
                token=token
            )
    print("Processing ended successfully!")

    print(frequency_matrix)
    return frequency_matrix


def build_coordinate_matrix_positions_ndarray(
        files_corporas,
        tokens
) -> numpy.ndarray:
    """

    :type files_corporas: list
    :type tokens: list
    """
    print("Initialization of the position matrix...")
    position_matrix = numpy.zeros(
        (
            files_corporas.__len__(),
            tokens.__len__()
        ),
        dtype="object"
    )
    print(position_matrix)
    print(f"Matrix shape: {position_matrix.shape}")

    for file_index, file_corpora in enumerate(files_corporas):
        file_output = pipeline_input(file_corpora)
        file_tokens = tokenize_corpora(file_output)
        for token_index, token in enumerate(tokens):
            position_matrix[file_index][token_index] = calculate_token_positions(
                file_tokens=file_tokens,
                token=token
            )
    print("Processing ended successfully!")

    print(position_matrix)
    return position_matrix


def build_coordinate_matrices_df(
        working_dir,
        file_extension,
) -> tuple:
    """
    Construction of the matrix incidence between files in working directory and their tokens
    :type working_dir: str
    :type file_extension: str
    """
    filepath_list = dir_files_by_extension(
        working_dir=working_dir,
        file_extension=file_extension
    )

    incidence_matrix, frequency_matrix, position_matrix, tokens = build_coordinate_matrix_incidence(
        working_dir=working_dir,
        file_extension=file_extension
    )

    print("Converting the generated numpy incidence matrix into pandas data frame")
    df_incidence = pd.DataFrame(
        data=incidence_matrix.T,
        index=tokens,
        columns=range(filepath_list.__len__())
    )
    columns = filepath_list
    df_incidence.columns = columns
    print("Incidence data frame was generated successfully!")

    print("Converting the generated numpy frequency matrix into pandas data frame")
    df_frequency = pd.DataFrame(
        data=frequency_matrix.T,
        index=tokens,
        columns=range(filepath_list.__len__())
    )
    columns = filepath_list
    df_frequency.columns = columns
    print("Frequency data frame was generated successfully!")

    print("Converting the generated numpy position matrix into pandas data frame")
    df_position = pd.DataFrame(
        data=position_matrix.T,
        index=tokens,
        columns=range(filepath_list.__len__())
    )
    columns = filepath_list
    df_position.columns = columns
    print("Position data frame was generated successfully!")

    return df_incidence, df_frequency, df_position


def calculate_token_freq(
        token,
        file_tokens
) -> int:
    """
    Calculate the token frequency in the file corpus
    :type token: str
    :type file_tokens: list
    """
    counter = 0
    for file_token in file_tokens:
        if token == file_token:
            counter += 1
    return counter


def calculate_token_positions(
        token,
        file_tokens
) -> list:
    positions = []
    for file_index, file_token in enumerate(file_tokens):
        if token == file_token:
            positions.append(str(file_index))
    return positions
