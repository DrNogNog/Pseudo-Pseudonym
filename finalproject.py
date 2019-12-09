#
# finalproject.py  (Milestone)
#
# Cuckcoo's Calling book checker  
#

def clean_text(txt):
    """ returns a list containing the words in txt after it has been “cleaned”"""
    listofwords = ''
    txt = txt.lower()
    for word in txt:
        if word.isspace() or word.isalpha():
            listofwords += word
    return listofwords.split(' ') #creates list of words
def sample_file_write(filename):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.
        
def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)

def sentencesplitter(txt):
    """returns a list containing sentences"""
    listofsentences = ""
    txt = txt.replace('Mr. ', '')
    txt = txt.replace('Mrs. ', '')
    txt = txt.replace('Dr. ', '')
    txt = txt.replace('A.', ''),txt = txt.replace('B.', ''),txt = txt.replace('C.', ''),txt = txt.replace('D.', ''),txt = txt.replace('J.', ''),txt = txt.replace('K.', ''),txt = txt.replace('R.', ''),txt = txt.replace('G.', '')
    txt = txt.replace('  ',' ')
    txt = txt.lower()
    txt = txt.replace('!', '**').replace('?','**').replace('.','**').split('**')
    txt = txt[:-1]

def stem(s):
    """returns the historical stem of s"""
    if s[-3:] == 'ing':
        if len(s) < 6:
            s = s
        elif s[-4] == s[-5]:
            s = s[:-4]
        else:
            s = s[:-3]
    elif s[-2:] == 'er':
        if len(s) < 4:
            s = s
        elif s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-3:] == 'ies':
        s = s[:-2]
    elif s[-1:] == 'e':
        s = s[:-1]
    elif s[-2:] == 'ed':
        if len(s) < 4:
            s = s
        elif s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-4:] == 'tion':
        s = s[:3] + 'e'
    elif s[-1:] == 'y':
        s = s[:-1] + 'i'
    return s
class TextModel:
    def __init__(self, model_name):
        """contructs new TextModel object by accepting a string model_name"""
        self.name = str(model_name) #the name
        self.words = {} #all the types of words
        self.word_lengths = {} #lengths and top length count
        self.stems = {} #all the stems
        self.sentence_lengths = int #sentence lengths and all their counts
        self.word_vowel_count = {} # sorts vowel occurrence of each word and counts occurance ex:{5 vowels: in 24 words}
    def __repr__(self):
        """returns a string that includes the name of the model as well as the sizes of dictionaries"""
    
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += "number of word lengths: " + str(len(self.word_lengths)) + '\n'
        return s
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!
        sentencelength = #CONTINUE HERE
            
            
        word_list = clean_text(s)
    
        # Template for updating the words dictionary.
        for w in word_list:
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1
            length = len(w)
            # Add code to update other feature dictionaries.
            if length in self.word_lengths:
                self.word_lengths[length] += 1
            else:
                self.word_lengths[length] = 1
            eachstem = stem(s)
            if eachstem in self.stems:
                self.stems[eachstem] += 1
            else:
                self.stems[eachstem] = 1
            #self.sentence_lengths self.num_vowel_count
            
            
            
            
            
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model. It should not explicitly return a value."""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
    def save_model(self):
        """writing its various feature dictionaries to files"""
        file1 = open((self.name + '_' + 'words'), 'w')
        f2 = open((self.name + '_' + 'word_lengths'), 'w')
        f3 = open((self.name + '_' + 'stems'), 'w')
        f4 = open((self.name + '_' + 'sentence_lengths'), 'w')
        f5 = open((self.name + '_' + 'word_vowel_count'), 'w')

        file1.write(str(self.words))
        f2.write(str(self.word_lengths))
        f3.write(str(self.stems))
        f4.write(str(self.sentence_lengths))
        f5.write(str(self.word_vowel_count))

        file1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
    def read_model(self):
        """reads stored dictionaries """
        file1 = open((self.name + '_' + 'words'), 'r')
        f2 = open((self.name + '_' + 'word_lengths'), 'r')
        f3 = open((self.name + '_' + 'stems'), 'r')
        f4 = open((self.name + '_' + 'sentence_lengths'), 'r')
        f5 = open((self.name + '_' + 'word_vowel_count'), 'r')

        dict_str1 = file1.read()
        dict_str2 = f2.read()
        dict_str3 = f3.read()
        dict_str4 = f4.read()
        dict_str5 = f5.read()

        file1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
                
        self.words = eval(dict_str1)
        self.word_lengths = eval(dict_str2)
        self.stems = eval(dict_str3)
        self.sentence_lengths = eval(dict_str4)
        self.word_vowel_count = eval(dict_str5)
