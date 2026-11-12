import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true')
args, unknown = parser.parse_known_args()

params = {}
for arg in unknown:
    if '=' in arg:
        key, value = arg.split('=', 1)
        params[key] = value

if args.sort:
    for key in sorted(params.keys()):
        print(f"Key: {key} Value: {params[key]}")
else:
    for key, value in params.items():
        print(f"Key: {key} Value: {value}")