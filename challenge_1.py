import util
import json # this is part of the Python standard library


# we need to load in some external data
def grabJSON():
    '''Load some JSON data for us to work with
    Here we load weather dat for Athens'''
    with open('tools.json', 'r') as fin:
        tools = fin.read() # read inall the content
    # function do not need a 'return' statement
    # if we choose to return something, that is the end of the function
    return tools

# then we need to grab the bits we're intersted in
def handleData():
    '''Take the loaded data and start analysing it'''
    result = grabJSON()
    # we can convert this into a Pyuthon structure
    results_obj = json.loads(result)
    print(results_obj) # the entire loaded data structure
    # we have a LIST containing a DICT so we will need [0]
    # we parse the structure, we walk-the-tree
    print(results_obj[0]['name'])
    print(results_obj[0]['description'])
    print(results_obj[0]['input_schema'])
    print(results_obj[0]['input_schema']['properties'])
    print(results_obj[0]['input_schema']['properties']['data'])
    print(results_obj[0]['input_schema']['properties']['data']['items']['required'])


if __name__ == '__main__':
    handleData()