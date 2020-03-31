# JSON reader

import os, json

import nltk_example

# Dictionary of articles: title -> steps
steps = {}

# Dictionary of descriptions: title -> descriptions
descriptions = {}

data_path = '../new_wikihow_1000'
for filename in os.listdir(data_path):
    with open(data_path + '/' + filename, "r") as f:
        data_json = json.load(f)
        # For each JSON file fill the dictionaries
        title = data_json['title']
        # Skip articles with no title
        if title == None:
            continue
        # Get the steps
        step_list = []
        description_list = []
        if len(data_json['method/part']) > 0:
            methods = data_json['method/part']
            for method in methods:
                sub_steps = method['steps']
                step_titles = [step[0] for step in sub_steps]
                step_descriptions = [step[1] for step in sub_steps]
                step_list += step_titles
                description_list += step_descriptions
        else:
            step_list = [step[0] for step in data_json['steps']]
            description_list = [step[1] for step in data_json['steps']]
        steps[title] = step_list
        descriptions[title] = description_list

            


