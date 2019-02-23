import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

import geocoder
myloc = geocoder.ip('me')
print(myloc.latlng)
#getting the location of the device

import feedparser
from nltk.corpus import wordnet 
synonyms = [] 
#using nltk to form a word set for synonyms for word outbreak and spread
#using wordnet inside nltk library to get the required words
for syn in wordnet.synsets("spread"): 
    for l in syn.lemmas(): 
        synonyms.append(l.name())  
  
spread = set(synonyms) 
from nltk.corpus import wordnet 
synonyms = [] 
  
for syn in wordnet.synsets("outbreak"): 
    for l in syn.lemmas(): 
        synonyms.append(l.name())  
#taking a union of the word synonym set formed
out = set(synonyms)
out = out.union(spread)
probable = []
d = feedparser.parse('long,lat')#parsing the required titles from a cerating location, that contains the news regarding the disease outbreak
for post in d.entries:
    for i in out:
        if(i in post.title):
            probable.append(post.title)

print(probable)

cd = ['HIV/AIDS', 'Chickenpox', 'Chronic Fatigue Syndrome', 'Common Cold', 'Diphtheria', 'E. coli', 'Giardiasis', 'Infectious Mononucleosis', 'Flu', 'Lyme Disease', 'Malaria', 'Measles', 'Meningitis','Mumps', 'Polio', 'Pneumonia','Rocky Mountain Spotted Fever', 'Salmonella Infections','Severe Acute Respiratory Syndrome','Sexually Transmitted Diseases','Shingles', 'Zoster', 'Tetanus', 'Toxic Shock Syndrome', 'Tuberculosis', 'Viral Hepatitis', 'West Nile Virus','Whooping Cough']
prob = [x.split(" ") for x in probable]

cd = [x.lower() for x in cd]
for x in range(len(prob)):
    if(set(prob[x]).intersection(cd)):
        print(str(set(prob[x]).intersection(cd))[2:5]+" Alert")