# Tigrinya-Parallel-Corpus

"EN_all" and "TI_all" contain the enitre data set, untokenised and not randomised.
Of the 63465 strings, 58191 or 91% are from biblical sources (strings in lines 4322 - 62513).

Folders "v1", "v2", etc refer to versions one, two, etc.

In these folders, all files starting with "EN" contain English sentences, files starting with "TI" contain the corrsponding sentences in Tigrinya. One line is equal to one sentence, line `i` in "EN" corresponds to line `i` in "TI" with the same name.

 * v1: Untokenised, one file per language.
 * v2: Untokenised. Each language split in three files: training, validation, evaluation. Order random, lines still correspond between "EN" and "TI". 
 * v3: Files from v2 encoded using 10000-item subword models from sentencepiece. 
