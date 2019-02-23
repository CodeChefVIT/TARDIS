import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from autocorrect import spell

sentence=input()#Taking user problem health problem

chunkGram = r"""Chunk: {<.*>+}
}<IN|DT|TO|PRP>+{""" #Chunk description for RegexParser
chunkParser = nltk.RegexpParser(chunkGram)#Creating Chunk parse

crct = [spell(w) for w in nltk.word_tokenize(sentence)] # Correct the spelling for the words in the sentence

tagged = nltk.pos_tag(crct)#Part of Speech tagging the sentence
tree=chunkParser.parse(tagged)#Creating tree after parsing POS
list=[]
for subtree in tree.subtrees():#Getting Subtrees from Tree
     if subtree.label() == 'Chunk':#Identify chunks and extracting leaves of Noun(singular or mass), adjective defining noun
            a=subtree.leaves()
            for i in a:
                if(i[1]=='NN'):
                    noun=i[0]
                if(i[1]=='JJ' or i[1]=='VBZ' or i[1]=='VBG' or i[1]=='VBN'or i[1]=='NN'):
                    list.append(i[0])
#tree.draw()
dict={}
ps=PorterStemmer()
stopwords=set(stopwords.words('english')) 
filter_list = [ps.stem(w) for w in list if not w in stopwords] ## Find stem of the word

new_list = [spell(w) for w in filter_list] #Complete the stem of the porter stemmer


dict[noun]=new_list #Dictionary for health problem
print(dict)
