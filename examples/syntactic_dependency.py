#!/usr/bin/env python

from gurunudi import AI,api

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("Larry Page was doing his Phd at Stanford University in 1996.")

#The AI attribute "syntax_tree" returns a list containing the dependency parse tree for each sentence in the given text
print(ai.syntax_tree)

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.syntax_tree returns None i.e. if syntactic dependency API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for German text.
ai = AI("Emmanuel Macron est le président de la France.",gurunudi.FRENCH)

#For the latest updated list of languages supported by Gurunudi for syntactic dependency visit https://gurulaghu.com/languages/