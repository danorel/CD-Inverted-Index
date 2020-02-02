from pathlib import Path
from pdftotext import PDF
from nltk import word_tokenize

from ..helpers.dir import dir_files_by_extension


def extract_corpora_from_dir(
        working_dir,
        file_extension="pdf"
) -> str:
    corpora = str()

    filename_list = dir_files_by_extension(
        working_dir=working_dir,
        file_extension=file_extension
    )

    for (index, filename) in enumerate(filename_list):
        corpora += extract_corpora_from_file(
            filepath=str(Path(filename)),
            file_index=index,
            file_extension=file_extension
        )
    return corpora


def extract_corpora_from_file(
        filepath,
        file_index,
        file_extension="pdf"
) -> str:
    """

    :type filepath: str
    :type file_index: int
    :type file_extension: str
    """
    corpora = str()
    if file_extension == "pdf":
        with open(filepath, "rb") as file:
            pdf_file = PDF(file)
        corpora = "\n".join(pdf_file)
    else:
        with open(str(filepath), "r+", encoding='utf-8') as file:
            corpora = file.read()
    print(f"Processing of file [{file_index}] -> \'{filepath}\' was completed successfully!")
    return corpora


def extract_set_from(
        obj
) -> list:
    """
    Dictionary extraction with different input cases
    :type obj: object
    """
    tokens = []
    if isinstance(obj, list):
        for x in obj:
            if x not in tokens:
                tokens.append(x)
    if isinstance(obj, str):
        return extract_set_from(
            obj=word_tokenize(obj)
        )
    # Other isinstance(object, type) are here...
    return tokens
