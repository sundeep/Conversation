# File: conversation.py
# Function: Model a conversation 

class Conversation:
    """ A simple conversation modeller"""

    # Private Variable
    participants = []   # Conversation participants
    name = ""           # Conversation identifier
    summary = ""        # Conversation summary (for later)

    def __init__(self,conversation_string,name=''):
        self.conversation_stream = conversation_list
        self.name = name
        self.__assignParticipants__()


    def showConvo(self):
        """ Display conversation """
        for convo in self.conversation_stream:
            print " ".join(convo)

    def __assignParticipants__(self):
        """ Get the participants in the conversation from stream"""
       
        #Find location of ':' and words before is participant. 
        
        for line in self.conversation_stream:
            colon_index = line.index(':')
            participant = " ".join(line[0:colon_index])
            if not participant in self.participants:
                self.participants.append(participant)


        



        
        

