from pathlib import Path
from nltk import word_tokenize

from .dir import \
    dir_size, \
    dir_create


def log_directory_stats_to(
        log_dir,
        filename,
        working_dir,
        mode="a"
):
    """
    Directory statistics
    :type log_dir: str
    :type filename: str
    :type working_dir: str
    :type mode: str
    """
    dir_create(log_dir)
    filepath = Path(log_dir) / filename
    print(f"Appending the statistics about directory {working_dir} to the file {filename}...")
    with open(filepath, mode) as file:
        file.write(f"Directory summary weight: {dir_size(working_dir) / 1000} k-bytes\n")
    print(f"Directory statistics calculation was completed successfully!")
    return None


def log_corpora_stats_to(
        log_dir,
        filename,
        corpora,
        mode="a"
):
    """
    Corpora statistics
    :type log_dir: str
    :type filename: str
    :type corpora: str
    :type mode: str
    """
    dir_create(log_dir)
    filepath = Path(log_dir) / filename
    print(f"Appending the statistics about given corpora to the file {filename}...")
    with open(filepath, mode) as file:
        file.write(f"Total corpora length: {word_tokenize(corpora).__len__()} words\n")
    print(f"Corpora statistics calculation was completed successfully!")
    return None


def log_token_stats_to(
        log_dir,
        filename,
        tokens,
        mode="a"
):
    """

    :type log_dir: str
    :type filename: str
    :type tokens: list
    :type mode: str
    """
    dir_create(log_dir)
    filepath = Path(log_dir) / filename
    print(f"Appending the statistics about given tokens to the file {filepath}...")
    with open(filepath, mode) as file:
        file.write(f"Dictionary (tokens) length: {tokens.__len__()} words\n")
    print(f"Token statistics calculation was completed successfully!")
    return None
