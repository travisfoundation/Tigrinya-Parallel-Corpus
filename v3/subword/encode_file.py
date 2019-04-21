# -*- coding: utf-8 -*-

import os
import sentencepiece as spm

from argparse import ArgumentParser


def read_sents(file_name):
    with open(file_name) as handle:
        for line in handle:
            yield line.strip()


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--source_file", type=str, 
                            help="The source file to encode. Assumes one string per line.")
    arg_parser.add_argument("--spm_model", type=str,
                            help="File name of the saved model.")
    
    
    args = arg_parser.parse_args()
    prefix, *extensions = args.source_file.split(".")
    model_name = args.spm_model
    
    encoded_file_name = prefix + "_encoded" + ("." if extensions else "") + ".".join(extensions)


    lines = list(read_sents(args.source_file))
    
    print("LOADED FILE CONTENTS...")

    sp = spm.SentencePieceProcessor()
    sp.Load(model_name)
    
    print("LOADED SPM MODEL...\nWriting encoded lines to", encoded_file_name)
        
    # ▁ = 'LOWER ONE EIGHTH BLOCK' (U+2581)
    with open(encoded_file_name, "w") as handle:

        for i, s in enumerate(lines):
            piece_ls = sp.EncodeAsPieces(s)
            pieces_str = " ".join(piece_ls)
            
            handle.write(pieces_str)
            handle.write("\n")
            
            if i % int(len(lines)/10) == 0:
                print("=="*10, "LINE NUMBER", i, "=="*10)
                print(s)
                print("-->")
                print(pieces_str)
                print("\n")
            
            
    print("\nDONE!")
    
    


