import argparse

def parser():
    parser = argparse.ArgumentParser(description=None)
    positional = parser.add_argument_group('Positional arguments')
    optional = parser.add_argument_group('Optional arguments')
    positional.add_argument('--domain', metavar='\b', type=str, help='domain name to perform scan on', action='store', required=True)
    optional.add_argument('--crawl',help='crawl the domain', action='store_true', required=False)
    optional.add_argument('--dir', help='directory enumeration', action='store_true', required=False)
    optional.add_argument('--full', help='full scan', action='store_true', required=False)
    optional.add_argument('--threads', type=int, help='number of threads to use', action='store', required=False, default=30)
    optional.add_argument('--redirects', help='to enable redirects', action='store_true', required=False, default=False)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parser()