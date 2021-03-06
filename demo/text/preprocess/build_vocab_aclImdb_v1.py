"""
Copyright 2018 Lambda Labs. All Rights Reserved.
Licensed under
==========================================================================



"""
import argparse
import os
import sys
from collections import Counter
import operator
import pickle

def buildVocab(sentences):
  list_words = [w for l in sentences for w in l.split(" ")]
  counter = Counter(list_words)
  word_cnt = sorted(counter.items(),
                    key=operator.itemgetter(1), reverse=True)
  vocab = [x[0] for x in word_cnt]
  return vocab

def main():

  sys.path.append('.')
  from demo.text.preprocess import data_loader

  parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument("--input_file",
                      help="Path for input text file",
                      default="")
  parser.add_argument("--output_vocab",
                      help="Path for output vocabulary file",
                      default="")
  parser.add_argument("--unit",
                      help="Type of basic units",
                      choices=["char", "word"],
                      type=str,
                      default="word_basic")
  parser.add_argument("--loader",
                      help="name of data loader",
                      default="word_basic",
                      type=str,
                      choices=["char_basic", "word_basic", "imdb_loader"])

  args = parser.parse_args()


  args.input_file = os.path.expanduser(args.input_file)
  args.output_vocab = os.path.expanduser(args.output_vocab)
  
  loader = getattr(data_loader, args.loader)
  data = loader(args.input_file)
  
  vocab = buildVocab(data['sentence'])

  with open(args.output_vocab, 'w') as f:
    pickle.dump(vocab, f)

if __name__ == "__main__":
  main()