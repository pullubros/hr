import argparse

class ExportAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        namespace.export = True

def create_parser():
    parser = argparse.ArgumentParser(description='manage users on a server based on an “inventory” JSON file')
    parser.add_argument('--export', '-e', action=ExportAction, default=False, nargs=0, help='export output')
    parser.add_argument('path', help='path to inventory JSON file')
    return parser

