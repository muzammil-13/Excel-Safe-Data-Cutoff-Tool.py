import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
parser.add_argument("--sheet", required=True)
parser.add_argument("--column", required=True)
parser.add_argument("--condition", required=True)
parser.add_argument("--value", required=True)
parser.add_argument("--max_row", type=int)

args = parser.parse_args()

safe_data_cutoff(
    args.file,
    args.sheet,
    args.column,
    args.condition,
    args.value,
    args.max_row
)