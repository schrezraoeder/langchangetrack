#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from argparse import ArgumentParser
import sys
from io import open
from os import path
from time import time
from langchangetrack.corpusreaders.plainngramscorpus import PlainNGRAMSCorpus
from corpustoembeddings import CorpusToEmbeddings

import logging
logger = logging.getLogger("langchangetrack")

__author__ = "Vivek Kulkarni"
__email__ = "viveksck@gmail.com"

LOGFORMAT = "%(asctime).19s %(levelname)s %(filename)s: %(lineno)s %(message)s"

def run(filename, output_dir, file_prefix, window_size, embedding_type):
    corpus_reader = PlainNGRAMSCorpus(args.filename)
    model_config = {}
    model_config['window'] = window_size
    model_file = path.join(output_dir, '_'. join([file_prefix, 'embeddings.model']))
    c = CorpusToEmbeddings(corpus_reader, embedding_type, model_config = model_config, save_model_file = model_file)
    c.build()

def main(args):
    filename = args.filename
    output_dir = args.output_dir
    file_prefix = args.file_prefix
    window_size = int(args.window_size)
    embedding_type = args.embedding_type
    run(filename, output_dir, file_prefix, window_size, embedding_type)

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-f", "--file", dest="filename", help="Input file for ngrams")
  parser.add_argument("-o", "--output_dir", dest="output_dir", help="Output directory")
  parser.add_argument("-p", "--file-prefix", dest="file_prefix", default = 'exp', help="File prefix")
  parser.add_argument("-w", "--window_size", dest="window_size", default = 5,  help="Window size for word2vec")
  parser.add_argument("-e", "--embedding_type", dest="embedding_type", default = 'skipgram',  help="Embedding type")
  logging.basicConfig(level=logging.INFO, format=LOGFORMAT)
  args = parser.parse_args()
  main(args)
