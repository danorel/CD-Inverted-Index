from .helpers.log import \
    log_token_stats_to, \
    log_corpora_stats_to, \
    log_directory_stats_to
from .helpers.save import \
    save_tokens, \
    save_matrix_incidence, \
    save_inverted_index
from .helpers.dir import \
    dir_files_by_extension

from .preprocessing import \
    pipeline_input, \
    tokenize_corpora_into_dict

from .extractors import \
    extract_corpora_from_dir

from .index.single_inverted import \
    build_singly_matrix_incidence_df
from .index.single_inverted.utils import \
    build_singly_inverted_index

from .search import \
    boolean_search

from .index.double_inverted import \
    build_doubly_matrix_incidence_df
from .index.double_inverted.utils import \
    build_doubly_inverted_index

from .index.coordinate.utils import \
    build_coordinate_matrices_df
from .index.coordinate import \
    build_coordinate_index


def start(
        working_dir,
        file_extension,
        query
):
    """

    :type query: str
    :type working_dir: str
    :type file_extension: str
    """
    """
    test_singly_matrix_incidence(
        working_dir=working_dir,
        file_extension=file_extension
    )
    test_singly_inverted_index(
        working_dir=working_dir,
        file_extension=file_extension
    )
    test_tokenization(
        working_dir=working_dir,
        file_extension=file_extension
    )
    test_boolean_search(
        query=query,
        working_dir=working_dir,
        file_extension=file_extension
    )
    test_doubly_matrix_incidence(
        working_dir=working_dir,
        file_extension=file_extension
    )
    test_doubly_inverted_index(
        working_dir=working_dir,
        file_extension=file_extension
    )
    """
    test_coordinate_matrix_incidence(
        working_dir=working_dir,
        file_extension=file_extension
    )
    test_coordinate_inverted_index(
        working_dir=working_dir,
        file_extension=file_extension
    )
    return None


def test_tokenization(
        working_dir,
        file_extension,
        save_dir="results/tokens",
        filename_log="log.txt",
        filename_tokens="tokens.txt",
):
    """
    Tokenization/Dictionary test
    :type working_dir: str
    :type file_extension: str
    :type save_dir: str
    :type filename_log: str
    :type filename_tokens: str
    """
    corpora = extract_corpora_from_dir(
        working_dir=working_dir,
        file_extension=file_extension
    )

    output = pipeline_input(corpora)
    tokens = tokenize_corpora_into_dict(output)

    save_tokens(
        save_dir=save_dir,
        filename=filename_tokens,
        tokens=tokens
    )

    log_token_stats_to(
        log_dir=save_dir,
        filename=filename_log,
        tokens=tokens
    )
    log_corpora_stats_to(
        log_dir=save_dir,
        filename=filename_log,
        corpora=corpora
    )
    log_directory_stats_to(
        log_dir=save_dir,
        filename=filename_log,
        working_dir=working_dir
    )
    return None


def test_singly_matrix_incidence(
        working_dir,
        file_extension,
        save_dir="results/singly-index",
        filename_matrix="singly-matrix-incidence.csv"
):
    """
    Matrix incidence test
    :type working_dir: str
    :type file_extension: str
    :type save_dir: str
    :type filename_matrix: str
    """
    matrix_df = build_singly_matrix_incidence_df(
        working_dir=working_dir,
        file_extension=file_extension
    )
    save_matrix_incidence(
        save_dir=save_dir,
        filename=filename_matrix,
        matrix_df=matrix_df
    )
    return None


def test_singly_inverted_index(
        working_dir,
        file_extension,
        save_dir="results/singly-index",
        filename_index="singly-inverted-index.txt"
):
    """
    Singly-inverted index
    :type working_dir: str
    :type file_extension: str
    :type save_dir: str
    :type filename_index: str
    """
    inverted_index = build_singly_inverted_index(
        working_dir=working_dir,
        file_extension=file_extension
    )
    save_inverted_index(
        save_dir=save_dir,
        filename=filename_index,
        inverted_index=inverted_index
    )
    return None


def test_boolean_search(
        query,
        working_dir,
        file_extension
):
    """
    Boolean Search
    :type query: str
    :type working_dir: str
    :type file_extension: str
    """
    print(f"Input query: {query}")

    filepath_list = dir_files_by_extension(
        working_dir=working_dir,
        file_extension=file_extension
    )
    inverted_index = build_singly_inverted_index(
        working_dir=working_dir,
        file_extension=file_extension
    )
    docs_indices = boolean_search(
        query=query,
        inverted_index=inverted_index
    )

    print("Response by input query in files is: ")
    for index, filepath in enumerate(filepath_list):
        if index in docs_indices:
            print(f"{index} : {filepath}")
    return None


def test_doubly_matrix_incidence(
        working_dir,
        file_extension,
        save_dir="results/doubly-index",
        filename_matrix="doubly-matrix-incidence.csv"
):
    """
    Matrix incidence test
    :type working_dir: str
    :type file_extension: str
    :type save_dir: str
    :type filename_matrix: str
    """
    matrix_df = build_doubly_matrix_incidence_df(
        working_dir=working_dir,
        file_extension=file_extension
    )
    save_matrix_incidence(
        save_dir=save_dir,
        filename=filename_matrix,
        matrix_df=matrix_df
    )
    return None


def test_doubly_inverted_index(
        working_dir,
        file_extension,
        save_dir="results/doubly-index",
        filename_index="doubly-inverted-index.txt"
):
    """
    Doubly-inverted index
    :type working_dir: str
    :type file_extension: str
    :type save_dir: str
    :type filename_index: str
    """
    inverted_index = build_doubly_inverted_index(
        working_dir=working_dir,
        file_extension=file_extension
    )
    save_inverted_index(
        save_dir=save_dir,
        filename=filename_index,
        inverted_index=inverted_index
    )
    return None


def test_coordinate_matrix_incidence(
        working_dir,
        file_extension,
        save_dir="results/coordinate-index",
        filename_incidence="coordinate-matrix-incidence.csv",
        filename_frequency="coordinate-matrix-frequency.csv",
        filename_position="coordinate-matrix-position.csv"
):
    """
    Matrices coordinate test
    :type working_dir: str
    :type file_extension: str
    :type save_dir: str
    :type filename_incidence: str
    :type filename_frequency: str
    :type filename_position: str
    """
    df_incidence, df_frequency, df_position = build_coordinate_matrices_df(
        working_dir=working_dir,
        file_extension=file_extension
    )
    save_matrix_incidence(
        save_dir=save_dir,
        filename=filename_incidence,
        matrix_df=df_incidence
    )
    save_matrix_incidence(
        save_dir=save_dir,
        filename=filename_frequency,
        matrix_df=df_frequency
    )
    save_matrix_incidence(
        save_dir=save_dir,
        filename=filename_position,
        matrix_df=df_position
    )
    return None


def test_coordinate_inverted_index(
        working_dir,
        file_extension,
        save_dir="results",
        filename_index="coordinate-index.txt"
):
    """
    Doubly-inverted index
    :type working_dir: str
    :type file_extension: str
    :type save_dir: str
    :type filename_index: str
    """
    inverted_index = build_coordinate_index(
        working_dir=working_dir,
        file_extension=file_extension
    )
    save_inverted_index(
        save_dir=save_dir,
        filename=filename_index,
        inverted_index=inverted_index
    )
    return None
