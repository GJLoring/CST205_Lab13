#!/usr/bin/python

'''

Lab #13: Lists (3-4 hours)
Problem 1: Mad Libs (practice with strings and lists)
Mad Libs are a classic party game where you start with a story with some of the words removed.  The guests are asked to supply words (by part of speech, names, numbers, etc) without knowing what the story is about.  Then, the words are inserted into the story and it is read aloud - hilarity ensues.  Today we'll be creating our own mad libs to practice using strings and lists.

This is a pair project.  (work with ONE partner. If you are working in a group of four, divide into two groups of two. If you have a group of three, it's ok to keep the size as three members. Each pair creates one product collaboratively, each student submit identical product using their iLearn account. Submit all python code for lab #13 in .py format. Also submit the screen capture of the running program and its output in image format, i.e., .jpg, or .png format.)
Step 1: Find a news article online

You only need between 100 and 200 words for a decent mad lib, so if you find a really long story, take only part of it.  

The example will use the first few paragraphs of this CNN article: http://www.cnn.com/2013/04/04/world/asia/koreas-tensions/index.html?hpt=hp_t2

Step 2: Remove some words

Go through the article and turn it into strings in Python and remove some of the words.  These will be the words that become part of the Mad Lib Game

Step 3: Make some design decision

You need to think about how you are going to ask the user to enter the words, how you are going to store the words entered, and how you are going to print out the restulting story.  There are several different ways to accomplish this using strings and lists.  The one rule is that you cannot use a separate variable for every word you need.

Step 4: Collect words from the user

Prompt the user to enter the words that you need to fill in your mad lib 

Step 5: Print the results

Combine the original text plus the new words to print your final mad lib.  Here is my final based on the example above:

(CNN) -- Missile and puppy components have been moved to the sparkly coast, of Disneyland in the 'last few days,' a Neptune official with happy knowledge of the information told CNN Thursday.The apparent deployment comes amid further cheerful statements by Las Vegas and heightened rainbows in the region -- a situation that does not need to get furry a U.S. State Department spokeswoman said. The move of the missile and kitten equipment could mean that Pyongyang, which unleashed another round of loving rhetoric accusing the United States of huging the region to the "have a nice day" of war may be planning a glitter launch soon. The llama, the official said, are consistent with those of a cuddly missile, which has a3.14-mile range, meaning it could threatenSea World and CSUMB.

This version is happier than the original :)

Once your program is debugged, swap with another group and try each other's programs!


'''

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

def promptUserForWordByType(wordType):
  '''
  Problem Step 3 instructs us to prompt the user for words and store those words
  We will store the words in place.
  '''
  prompt = ("Please enter a %s:\t"%(wordType))
  userInput = input(prompt)
  return userInput
  
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

def printNewsStory(storyText):
  print(storyText)

  
def main():
  madLibStory = scanStoryStream(newsStory)
  printNewsStory(madLibStory)

main()