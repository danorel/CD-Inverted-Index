import argparse


def argument_namespace():
    parser = argparse.ArgumentParser(
        description="Dictionary"
    )
    parser.add_argument(
        '-d',
        '--directory',
        help="Pass the directory name here, which will be the database"
    )
    parser.add_argument(
        '-e',
        '--extension',
        help="Pass the interest extension"
    )
    parser.add_argument(
        '-q',
        '--query',
        help="Pass the query here"
    )
    return parser.parse_args()


def app():
    namespace = argument_namespace()
    from application import start
    start(
        working_dir=namespace.directory,
        file_extension=namespace.extension,
        query=namespace.query
    )
    return None


if __name__ == '__main__':
    app()
