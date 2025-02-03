import util
import json # this is part of the Python standard library


# we need to load in some external data
def grabJSON():
    '''Load some JSON data for us to work with
    Here we load weather dat for Athens'''
    with open('athens_w.json', 'r') as fin:
        ath = fin.read() # read inall the content
    # function do not need a 'return' statement
    # if we choose to return something, that is the end of the function
    return ath

# then we need to grab the bits we're intersted in
def handleData():
    '''Take the loaded data and start analysing it'''
    result = grabJSON()
    # we can convert this into a Pyuthon structure
    results_obj = json.loads(result)
    # challenge: print the 'coord' value of our dict
    print(results_obj['coord']) # we're not obliged to inject it into a formatted string...
    # challnge: print the 'visibility'
    print(results_obj['visibility'])
    # but often we do need to
    # print(f"{results_obj["coords"]}") # OOPS - do not use same quotes inside same quotes
    # print(f"{results_obj['coord']}") # FIXED!!
    # print(f'{results_obj["coord"]}') # FIXED!!
    # print(type(results_obj), results_obj)

# make them into a new pretty structure

if __name__ == '__main__':
    # print( grabJSON() )
    handleData()
    # print('It's you! Feathers McGraw')
