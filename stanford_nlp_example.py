#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:10:28 2020

@author: gizem
"""

# Simple usage
#https://github.com/smilli/py-corenlp

from pycorenlp import StanfordCoreNLP

# Before this, cd to directory and run java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer

nlp_wrapper = StanfordCoreNLP('http://localhost:9000')

text = ('Share your success with a friend.')

output = nlp_wrapper.annotate(text, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })

print(output['sentences'][0]['parse'])
