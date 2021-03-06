#!/bin/env python3

import os
import sys

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.sam') or file.endswith('.tsv') or file.endswith('.fa') or file.endswith('.fq') or file.endswith('.fasta') or file.endswith('.fastq'):
            os.system(f"gzip {os.path.join(subdir, file)}")