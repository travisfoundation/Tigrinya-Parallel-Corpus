# The TravisFoundation English-Tigrinya Parallel Corpus

A corpus of parallel English-Tigrinya phrases, compiled by Travis Foundation. This parallel corpus' main goal is of course to help progress the path towards English-Tigrinya machine translation. 

Its secondary aim is to increase (if only by a little) the amount of digital, publicly available samples of the Tigrinya language, spoken by at least 9 million people. 

## Basic Properties

This parallel corpus uses the simplest possible format, namely a line-by-line format in which line `i` in `some_file_EN` corresponds to line `i` in `some_file_TI`. All files are UTF-8 encoded (Unix line-breaking), which includes the Ge'ez alphabet, the alphabet in which Tigrinya is written.

The corpus is left unchanged from its original sources (see section below) which entails partly inconsistent style, e.g. with respect to punctuation, and some linguistic noise. This repository includes simple scripts to normalise the corpus linguistically and regarding punctuation, which may be less useful for the English parts of this corpus but more so for the Tigrinya parts.

Some cornerstone statistics of the Travis Foundation corpus:

 - number of phrases: 
 - number of words: EN, TI
 - 
 
 
## Provenance

The majority of this collection of parallel sentences is actually scraped from the Jehova's Witnesses' website, to our knowledge the largest findable collection of texts with both English and Tigrinya version. The X parallel sentences obtained from this source account for Y% of our corpus. (Please note that we do not claim or wish to infringe upon the ownership of these texts; we include them here merely for scientific pruposes, namely for training and testing machine learning models. Please be aware of that when using this corpus.)

The remainder of this corpus, that is the remaining A sentence pairs or B%, is however crowd-sourced by ourselves. With tremendous efforts, Eritrean volunteers helped digitise their own language and created these sentence pairs by translating English sentences into their mother tongue. All of these English source sentences were obtained from open-source sites, almost all from Wikipedia and a small number from other sources. Hence, over this part of the corpus we claim complete ownership and publish it here for open-source use under the [provided license](./LICENSE.txt).


## Scripts

This corpus comes with a few Python scripts to parse and process the corpus. While very basic scripts in terms of natural language processing, they are mainly included to exemplify doing linguistic pre-processing for Tignrinya, such as dealing with the Ge'ez UTF-8 code points and punctuation.
Specifically, these scripts include:

  - `script_a.py`: Some contents.







 - Tigrinya-English parallel corpus
 
 - properties:
   - UTF-8 encoded
   - line-by-line formatting, i.e. line `i` in `some_file_EN` corresponds to line `i` in `some_file_TI`
 
 - provenance information:
   - large part is scraped from the Jehova's Witnesses web-site (without permission) 
     -> don't know the process and hence no grip on accuracy/appropriateness of translations
     -> language is highly biased towards religious topics ('Jesus' being the 4th most common word); 
        more problematically, the language represents the views of JW, some of which very opinionated or even intolerant
   - rest is crowd-sourced by ourselves (with the tremendous efforts from Eritrean volunteers), by translating snippets of articles from the English Wikipedia
