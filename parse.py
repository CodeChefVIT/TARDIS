import nltk
sentence=input()#Taking user problem health problem
chunkGram = r"""Chunk: {<.*>+}}<VB.?|IN|DT|TO|PRP>+{""" #Chunk description for RegexParser
chunkParser = nltk.RegexpParser(chunkGram)#Creating Chunk parse
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))#Part of Speech tagging the sentence
tree=chunkParser.parse(tagged)#Creating tree after parsing POS
list=[]
for subtree in tree.subtrees():#Getting Subtrees from Tree
     if subtree.label() == 'Chunk':#Identify chunks and extracting leaves of Noun(singular or mass), adjective defining noun
            a=subtree.leaves()
            for i in a:
                if(i[1]=='NN'):
                    noun=i[0]
                if(i[1]=='JJ'):
                    list.append(i[0])
tree.draw()
dict={}
dict[noun]=list#Dictionary for health problem
print(dict)
