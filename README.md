# Mini-Proyect-IR
 
 
 ## Pig Latin
 - Pig Latin is a language game where English words are altered in a set of rules:     
        1. If word does not start with a letter, it will not be changed.     
        2. Every word that starts with a consonant, all consonants before the first vocal will be moved to the end, and 'ay' is added.     
        3. Words that start with a vocal, 'yay' will be added at the end.
  - Examples;   
  mess ⇒ essmay     
  father ⇒ atherfay     
  Rwanda ⇒ Andarway     
  choir ⇒ oirchay    
  ant ⇒ antyay     
  4G ⇒ 4G      
  - This scrip translates from Pig Latin to English. If no argument is given, it will promp you to enter the phrases. If a text file is given, it will generate a text file with the traduction.    
  - Example:    
ENGLISH: Spam, SPAM, Spam, Egg and Spam;    
PIG LATIN: Amspay, AMSPAY, Amspay, Eggyay andyay Amspay;    
ENGLISH: brandy and a fried egg on top and Spam     
PIG LATIN: andybray andyay ayay iedfray eggyay onyay    
optay andyay Amspay      
ENGLISH: 4G and spam    
PIG LATIN: 4G andyay amspay     

  ## Count Words
- Script that analysis a given text file, and gives a complete evaoluation of the text in terms of nº of lines, nº of words with/without stopwords, dictionary of the file...  

usage: count_words.py [-h] [-s STOPWORDS] [-l] [-b] [-f] file [file ...]        
- positional arguments:    
file text file.     
- optional arguments:      
-h, --help show this help message and exit     
-s STOPWORDS, --stop STOPWORDS    
filename with the stopwords.   
-l, --lower lowercase all words before computing stats.   
-b, --bigram compute bigram stats.   
-f, --full show full stats.  
![image](https://user-images.githubusercontent.com/99536660/172832764-364535cf-47ca-458f-ac96-1d92fbed165e.png)
![image](https://user-images.githubusercontent.com/99536660/172832798-b9a3bfd0-a610-403b-871a-3a0493ddaaf6.png)

 ## Infinite Monkey
  - Infinite Monkey Theorem; States that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text.   
  -  This script tries to do something like that, the objective is creating phrases by chosing random words form a dictionary of bigrmas/trigrams. The resaults are surprisingly good, as some phrases generated do make sense.    
  monkey_indexer.py -> Creates an index from the textfile. Default bigrams, however if in prompt tri is typed trigram indexer will be generated.         
  monkey_info.py -> Generates information from an index.    
  monkey_evolved.py -> Generates phrases from the index.    
  monkey_lib -> Library for all the methods used.
  
  Index:       
  ![image](https://user-images.githubusercontent.com/99536660/172835157-48d608ef-bf7a-484d-b18a-740025ce774e.png)        
  Info:      
  ![image](https://user-images.githubusercontent.com/99536660/172835218-7abbd918-de7c-4ff8-a5cd-99fc5b879036.png)

  
