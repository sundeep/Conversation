#File : script.py
#Function: utilize the Conversation model


import conversation
import nltk


def main():
    
    #create bits
    from nltk.corpus import webtext
    overheard_sents = webtext.sents('overheard.txt')

    convo1 = conversation.Conversation(overheard_sents[0:3],"white_and_asian")
    print "Participants:", convo1.participants


if __name__ == "__main__":
    main()
