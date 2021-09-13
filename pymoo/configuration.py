import os


class Configuration:
    show_compile_hint = True
    parse_custom_docs = False
    server = 'http://release.pymoo.org/_static/data/'


# returns the directory to be used for imports
def get_pymoo():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
