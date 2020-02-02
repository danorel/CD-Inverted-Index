from pathlib import Path

from application.helpers.dir import dir_create


def save_tokens(
        save_dir,
        filename,
        tokens
):
    """

    :type save_dir: str
    :type filename: str
    :type tokens: list
    """
    dir_create(save_dir)
    filepath = Path(save_dir) / filename
    print(f"Starting writing the given tokens to the file {filename} in the directory {save_dir}")
    with open(filepath, "w") as file:
        file.write(str(tokens))
    return None


def save_matrix_incidence(
        save_dir,
        filename,
        matrix_df
):
    """
    Saving the created incidence matrix in the csv file
    :type save_dir: str
    :type filename: str
    :type matrix_df: pandas.DataFrame
    """
    dir_create(save_dir)
    filepath = Path(save_dir) / filename
    print(f"Starting writing the given incidence matrix to the file {filename} in the directory {save_dir}")
    matrix_df.to_csv(filepath)
    return None


def save_inverted_index(
        save_dir,
        filename,
        inverted_index
):
    """

    :type save_dir: str
    :type filename: str
    :type inverted_index: defaultdict
    """
    dir_create(save_dir)
    filepath = Path(save_dir) / filename
    print(f"Starting writing the given inverted index to the file {filename} in the directory {save_dir}")
    with open(filepath, "w") as file:
        for token, indexing in inverted_index.items():
            file.write(f"{str(token)}: {str(indexing)}\n")
    return None
