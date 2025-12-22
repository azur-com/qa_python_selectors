from pathlib import Path


def script_dir(file_n):

    script_dir = Path(__file__).parent.joinpath(f'{file_n}').absolute()
    return script_dir
