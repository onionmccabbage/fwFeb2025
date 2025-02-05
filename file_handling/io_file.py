# working with byte files

def writebytes(b):
    '''write some bytes'''
    # we have a file access object - this is NOT the file itself
    # the operating system does the actual file handling om our behalf
    # NB usually wrap this is try-except
    # fout = open('mybytes' , 'wb') # 'wb' will (over)write bytes
    # fout.write(b)
    # fout.close() # tidy up when done
    # or more briefly
    with(open('mybytes', 'ab')) as fout:
        # fout.writelines() # iterate a collection and wtie its lines
        fout.write(b) # when 'with' is done, it closes fout
        fout.write(f'\n\n'.encode())

def readBytes():
    '''read and show the byte file'''
    with(open('mybytes', 'rb')) as fin: # 'rb' will read bytes
        s = fin.readlines() # read all the content into a list object with each line as a member
        r = fin.read() # read in the entire content
    return r

if __name__ == '__main__':
    b = bytes('this is plain text'.encode('utf-8'))
    writebytes(b)
    r = readBytes()
    print(f'Retrieved {r.decode()}')
