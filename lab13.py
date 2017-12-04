#!/usr/bin/python

#CST205 Lab 13 Pair Programming Project Problem 1 Madlib
#
# December 4, 2017
#
# Team 5, Hopper
#
#  Jose Garcia Ledesma
#  Gabriel Loring

# Problem Step 1 & 2 instruct us to locate a news story and to remove some of the words.
# We have inserted tags for every romved word to indicate the type of word it was and
# should therefore be replaced with, verbs with verbs, nouns with nouns nd so on
newsStory = '''
<Pronoun> has <verb> a brand new <noun>, which experts said shows a <adjactive> advance in technology and threat.
Photos of the <noun> released Thursday by <pronoun> showed a large, tall missile that appears to be significantly <adjactive> than the Hwasong-14, previously Pyongyang's most-advanced missile, which was launched over Japan twice in July.
\"They wanted (to be able) to hit all of the US and they wanted something big to hit it with," said David Schmerler, a research associate at the James Martin Center for Nonproliferation Studies (CNS). \"This seems on the surface level to be that missile.\"
The US military has begun referring to the missile as a <noun> -- a new designation signaling that the US is increasingly seeing the recent launch as involving a new type of ICBM, according to two US defense officials.
The two launches in July were categorized as KN-20s.
Experts have been analyzing and studying the images since their release, so what can we learn from them about North Korea's new weapon?

'''
  
def scanStoryStream(storyText):
  '''
  A news story is just a long string of charachters. 
  We removed the words replacing them
  with tags that indicate the type of word that was removed.  We now 
  scan the string with a simple state machine to locate and replace 
  the tags 
  '''
  inTag = False
  newStory = ""
  for letter in storyText:
    if inTag == False and letter == '<':
      inTag = True
      keyWord = ""
    elif inTag == True and letter == '>':
      inTag = False
      userWord = promptUserForWordByType(keyWord)
      newStory = newStory + userWord
    elif inTag == True:
      keyWord = keyWord + letter
    else:
      newStory = newStory + letter
      
  return newStory


def getWordTypesFromStream(storyText):
  '''
  A news story is just a long string of charachters. 
  We removed the words replacing them
  with tags that indicate the type of word that was removed.  We now 
  scan the string with a simple state machine to locate the words we 
  need to get the operator to supply
  '''
  words = {}
  inTag = False
  for letter in storyText:
    if inTag == False and letter == '<':
      inTag = True
      keyWord = ""
    elif inTag == True and letter == '>':
      inTag = False
      if keyWord in words:
        words[keyWord] = words[keyWord] + 1
      else:
        words[keyWord] = 1
    elif inTag == True:
      keyWord = keyWord + letter
     
  return words

def getUserWord(wordTypeCount):
  '''
  Problem Step 3 instructs us to prompt the user for words and store those words
  We will store the words in place.
  '''
  completeWordList = {}
  for wordType in wordTypeCount:
    wordList = [''] * wordTypeCount[wordType]
    for x in range(wordTypeCount[wordType]):
      prompt = ("Please enter a %s:\t"%(wordType))
      wordList[x] = input(prompt)
    completeWordList[wordType]=wordList
  return completeWordList
 
def printNewsStory(storyText):
  print(storyText)
  
def updateStoryStream(storyText, wordTypeCount, wordlist):
  '''
  A news story is just a long string of charachters. 
  We removed the words replacing them
  with tags that indicate the type of word that was removed.  We now 
  scan the string with a simple state machine to locate and replace 
  the tags using the words entered by the operator and assigned the correct
  word type
  '''
  inTag = False
  newStory = ""
  for letter in storyText:
    if inTag == False and letter == '<':
      inTag = True
      keyWord = ""
    elif inTag == True and letter == '>':
      inTag = False
      wordTypeCount[keyWord] = wordTypeCount[keyWord] -1
      newStory = newStory + wordlist[keyWord][wordTypeCount[keyWord]]
    elif inTag == True:
      keyWord = keyWord + letter
    else:
      newStory = newStory + letter
      
  return newStory


    
def main():
  '''
  Dynamicaly assemble a dictionary wordTypeCount that counts the types and count of
  words that will need to be replaced in the news article.
  Using our dictionary of word types, build a dictionary or lists to hold the operator
  supplied words of each type
  Finally replace the user supplied words in place of the word tags in the story.
  The story can now be print to the consol
  
  '''
  wordTypeCount = getWordTypesFromStream(newsStory)
  wordlist = getUserWord(wordTypeCount)
  madLibStory = updateStoryStream(newsStory, wordTypeCount, wordlist)
  printNewsStory(madLibStory)

main()