""" create a lexicon hash of available commands in game
    create a scanner to take user input and check it against hash
    send scanned input to game engine
"""
lexicon = { # this should probably be a list of tuples rather than hash 
    'direction': 'north', 
    'direction': 'south',
    'direction': 'east', 
    'direction': 'west', 
    'direction': 'up', 
    'direction': 'down', 
    'direction': 'left', 
    'direction': 'right', 
    'direction':'back'
    'verb': 'go', 
    'verb': 'stop', 
    'verb': 'kill', 
    'verb': 'eat'
    'stop': 'the', 
    'stop': 'in', 
    'stop': 'of', 
    'stop': 'from',
    'stop': 'at', 
    'stop': 'it'
    'noun': 'door', 
    'noun': 'bear', 
    'noun': 'princess', 
    'noun': 'cabinet'
}

def convert_num(s):
    try:
        return int(s)
    except ValueError:
        return None
    
command = raw_input("> ")

def scan(command):
    words = command.split()
    #insert fn to search and return hashmap values
    for word in words:
        try: 
            for item in lexicon:
                assertEquals(word.lower(), item)
        except ValueError:
            return None
    for word in words:
        number = convert_num(word):

    return word
        
