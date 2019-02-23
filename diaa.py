import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

import geocoder
myloc = geocoder.ip('me')
loc = myloc.latlng
min = []
#getting the location of the device
longlat = {'Mumbai': [19.075983, 72.877655], 'Delhi': [28.704060, 77.102493], 'Bangalore':[12.971599, 77.594566], 'Hyderabad':[17.385044, 78.486671], 'Chennai':[13.082680, 80.270721], 'Ahemdabad':[23.022505, 72.571365]}
# assigning longitude and latitude for cities

mint=[]
for i in longlat:
        min.append(np.array(longlat[i])-np.array(loc))
for i in range(len(min)):
        mint.append(round(min[i][0]+min[i][1]))
#Extracting your location from the mininum distance between longitude and latitude
city = list(dict.keys(longlat))[mint.index(0)]
rssfeed = {'Mumbai': -2128838597, 'Delhi': -2128839596, 'Bangalore': -2128833038, 'Hyderabad': -2128816011, 'Chennai': 2950623, 'Ahemdabad': -2128821153}
#storing the rss number for the cities from times of india rss feeder
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
d = feedparser.parse('https://timesofindia.indiatimes.com/rssfeeds/'+str(rssfeed[city])+'.cms')#parsing the required titles from a cerating location, that contains the news regarding the disease outbreak
for post in d.entries:
    for i in out:
        if(i in post.title):
            probable.append(post.title)

if(probable):
        print(probable)
else:
        print("No current outbreaks ")

cd = ['HIV/AIDS', 'Chickenpox', 'Chronic Fatigue Syndrome', 'Common Cold', 'Diphtheria', 'E. coli', 'Giardiasis', 'Infectious Mononucleosis', 'Flu', 'Lyme Disease', 'Malaria', 'Measles', 'Meningitis','Mumps', 'Polio', 'Pneumonia','Rocky Mountain Spotted Fever', 'Salmonella Infections','Severe Acute Respiratory Syndrome','Sexually Transmitted Diseases','Shingles', 'Zoster', 'Tetanus', 'Toxic Shock Syndrome', 'Tuberculosis', 'Viral Hepatitis', 'West Nile Virus','Whooping Cough']
prob = [x.split(" ") for x in probable]

cd = [x.lower() for x in cd]
for x in range(len(prob)):
    if(set(prob[x]).intersection(cd)):
        print(str(set(prob[x]).intersection(cd))[2:5]+" Alert")
