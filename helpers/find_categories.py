#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:33:44 2020

@author: gizem
"""
import os, json
import shutil

#category_list = {}
sub_categories = ['Studying', 'Drinks', 'Job Attendance', 'Relationship Issues', 'Fashion', 'Celebrities',
                  'Dogs', 'College University and Postgraduate', 'Games', 'Dating', 'Youth Dating', 'Youth Culture',
                  'Social Interactions for Youth', 'Friends', 'Youth and Family', 'Social Events for Youth',
                  'Looking Good', 'School Stuff', 'Fandom', 'Parties', 'Social Interactions', 'Cats', 'Parenting',
                  'Birds', 'Traveling with Companions', 'Fun Activities', 'Parents', 'Single Life', 'Toys', 
                  'Weddings', 'Neighbors', 'Halloween', 'Socializing at Work', 'Nicknames', 'Music']

# fill dictionary with keys
category_sublist = dict(zip(sub_categories, [[] for i in range(len(sub_categories))]))

data_path = 'wikihow_dataset'
print(len(os.listdir(data_path)))
for f_name in os.listdir(data_path):
    if f_name == '991780.json':
        continue
    with open(data_path + '/' + f_name, "r") as f:
        data_json = json.load(f)
        if data_json['category_hierarchy']:
            category = data_json['category_hierarchy']
            if len(category) > 1:
                if category[1] in category_sublist:
                    category_sublist[category[1]].append(f_name)
#print('All categories:')
#print(list(category_list.keys()))
#print('All sub-categories:')
#for k,v in category_sublist.items():
#    print(k + ': ' + str(v))

# Copy all the files
#for k in category_sublist.keys():
#    files = category_sublist[k]
#    for f in files:
#        shutil.copy(('wikihow_dataset/' + f),'category_files')
