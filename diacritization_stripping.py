#!/usr/bin/env python3
from __future__ import division
from __future__ import print_function
import sys

import argparse
import pandas as pd

import diacritization_stripping_data

parser = argparse.ArgumentParser()
parser.add_argument("--uninorms", action="store_true",
                    help="Use diacritization stripping based on Unicode Normalization")
parser.add_argument("--verbose", "-v", action="store_true",
                    help="Also compute statistics of the stripping")
args = parser.parse_args()

# Sample DataFrame creation, replace with actual DataFrame loading or definition
# df = pd.DataFrame({'text': ['your', 'data', 'here']})

maps = []
if not args.uninorms:
    maps.append(diacritization_stripping_data.strip_diacritization_uninames)
else:
    maps.append(diacritization_stripping_data.strip_diacritization_uninorms)

# Processing each row in the DataFrame
total, stripped, stripped_map = 0, 0, {}
processed_texts = []

df = pd.read_csv("./data/cleaned.csv")

for line in df['standardized_text']:
    output = ""
    for c in line:
        for m in maps:
            if c in m:
                stripped += 1
                stripped_map[c] = stripped_map.get(c, 0) + 1
                output += m[c]
                break
        else:
            output += c

        if not c.isspace():
            total += 1
    processed_texts.append(output)

df['source_text'] = processed_texts

if args.verbose:
    histogram = sorted(stripped_map.items(), key=lambda key_value: key_value[1], reverse=True)[:10]
    histogram = " ".join(map(lambda key_value: "{}:{:.2f}%".format(key_value[0], 100 * key_value[1] / stripped), histogram))
    print("Total: {}, stripped: {:.2f}%, histogram: {}".format(total, 100 * stripped / total, histogram),
          file=sys.stderr)

df_src = df['source_text']
df_src.to_csv("./data/source.csv", index=False)

