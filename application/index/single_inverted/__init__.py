import numpy
import pandas as pd

from application.preprocessing import \
    pipeline_input, \
    tokenize_corpora_into_dict
from application.extractors import \
    extract_corpora_from_dir, \
    extract_corpora_from_file
from application.helpers.dir import dir_files_by_extension


def build_singly_matrix_incidence(
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

    incidence_matrix = build_singly_matrix_incidence_ndarray(
        files_corporas=files_corporas,
        tokens=tokens
    )
    return incidence_matrix, tokens


def build_singly_matrix_incidence_ndarray(
        files_corporas,
        tokens
) -> numpy.ndarray:
    print("Initialization of the matrix...")
    incidence_matrix = numpy.zeros(
        (
            files_corporas.__len__(),
            tokens.__len__()
        )
    )
    print(incidence_matrix)
    print(f"Matrix shape: {incidence_matrix.shape}")

    print("Processing the matrix...")
    for file_index, file_corpora in enumerate(files_corporas):
        file_output = pipeline_input(file_corpora)
        file_tokens = tokenize_corpora_into_dict(file_output)
        for token_index, token in enumerate(tokens):
            incidence_matrix[file_index][token_index] = token in file_tokens
    print("Processing ended successfully!")

    print(incidence_matrix)
    return incidence_matrix


def build_singly_matrix_incidence_df(
        working_dir,
        file_extension,
) -> pd.DataFrame:
    """
    Construction of the matrix incidence between files in working directory and their tokens
    :type working_dir: str
    :type file_extension: str
    """
    filepath_list = dir_files_by_extension(
        working_dir=working_dir,
        file_extension=file_extension
    )

    incidence_matrix, tokens = build_singly_matrix_incidence(
        working_dir=working_dir,
        file_extension=file_extension
    )

    print("Converting the generated numpy matrix into pandas data frame")
    df = pd.DataFrame(
        data=incidence_matrix.T,
        index=tokens,
        columns=range(filepath_list.__len__())
    )
    df.columns = filepath_list
    print("Data frame was generated successfully!")
    return df

