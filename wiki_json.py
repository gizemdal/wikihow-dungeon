#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, json

import nltk_example

# list of tuples (method_number, step text)
steps = []

# Description dictionary step text -> description
descriptions = {}

# Method names
method_names = []

# Imperative list
def get_article(filename):
    with open('../new_wikihow_1000/' + filename, "r") as f:
        #global steps, descriptions, method_names
        s = [] # steps
        d = [] # descriptions
        m = [] # methods
        data_json = json.load(f)
        title = data_json['title']
        if title != None:
        # Get the steps
            if len(data_json['method/part']) > 0:
                methods = data_json['method/part']
                for method in methods:
                    all_steps = [(method['name'], step[0]) for step in method['steps']]
                    s += all_steps
                    m += method['name']
                    all_descs = dict(zip([step[0] for step in method['steps']], [step[1] for step in method['steps']]))
                    d.update(all_descs)      
            else:
                s = [(None, step[0]) for step in data_json['steps']]
                d = dict(zip([step[0] for step in data_json['steps']], [step[1] for step in data_json['steps']]))
        else:
            print('Article has no title!')
        return s, d, m

def is_imperative(text):
    # First tokenize the step headline
    tokens = nltk_example.tokenize(text)
    # Get the POS-tags
    tags = nltk_example.nltk.pos_tag(tokens)
    # Check if imperative
    imperative = nltk_example.is_imperative(tags)
    
    return imperative
            

article_file = '1929699.json'
#article_file = '9689074.json'
steps, descriptions, method_names = get_article(article_file)

# Once the necessary fields are filled, find imperatives
imperatives = []

for step in steps:
    # First split the headline into sentences
    headline_sentences = step[1].split('.')
    for headline in headline_sentences:
        if len(headline) == 0:
            continue
        if is_imperative(headline):
            imperatives.append(headline)
            break
    description = descriptions[step[1]]
    # Split the description paragraph into sentences
    sentences = description.split('.')
    for sentence in sentences:
        if len(sentence) == 0:
            continue
        if is_imperative(sentence):
            imperatives.append(sentence)

print(imperatives)

