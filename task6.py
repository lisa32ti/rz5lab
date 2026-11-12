import sys

def parse_args(args):
    params = {}
    sort_needed = False
    
    for arg in args:
        if arg == '--sort':
            sort_needed = True
        elif '=' in arg:
            key, value = arg.split('=', 1)
            params[key] = value
            
    if sort_needed:
        for key in sorted(params.keys()):
            print(f"Key: {key} Value: {params[key]}")
    else:
        for key, value in params.items():
            print(f"Key: {key} Value: {value}")

if __name__ == "__main__":
    parse_args(sys.argv[1:])