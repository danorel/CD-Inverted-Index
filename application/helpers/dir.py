import os

from pathlib import Path
from glob import glob


def dir_create(
        dirname
):
    """
    Directory creation interface
    :type dirname: str
    """
    directory = Path(dirname)
    if not directory.exists():
        print(f"Creating the non-existing directory {dirname}")
        directory.mkdir(
            parents=True,
            exist_ok=False
        )
    else:
        print(f"Directory with name {dirname} already exist! Creation cancelled!")
    return None


def dir_files_by_extension(
        working_dir,
        file_extension
) -> list:
    """
    Extract the filenames, which belong to the directory
    :type working_dir: str
    :type file_extension: str
    """
    path = Path(working_dir) / f"*.{file_extension}"
    filename_list = glob(str(path))
    if not filename_list:
        print(f"[Warning]: Cannot find any files with extension {file_extension} in the directory {working_dir}")
        exit(-1)
    return filename_list


def dir_size(
        working_dir
) -> int:
    """
    Calculate the amount of directory size in bytes
    :type working_dir: str
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(working_dir):
        for filename in filenames:
            fp = os.path.join(dirpath, filename)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

