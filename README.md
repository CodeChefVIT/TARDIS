# TARDIS
# Alleviate
A simple chat based interface where people can share their medical queries to get relevant answers.
The implementations done in the first commit are:
* Use of Google Places API to collect reviews of hospitals
* Perfroming sentiment analysis of the reviews of the hospitals to find the overall sentiment value for the hospital
* Parsing the user query to find the noun (subject) in the string and the chunks associated with it
* Creating a database with the sentiment values and reviews for future use
* Using Times of India News Articles and RSS feeds to find Disease in Area (DIA) Alert to alter users about contigious diseases that might happen near them

The following are in pipeline for the second part of the hack:
* Completion of the RASA based Context-Driven Bot
* UI/UX Design
* Integrating Medicine and Doctor reviews along with hospitals
* Using ChatBot data to understand symptoms of disease and recommend medecine
* Use of Medical Triage (if found)
