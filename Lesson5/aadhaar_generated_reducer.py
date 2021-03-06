import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    aadhaar_generated = 0
    last_key = None
    
    for line in sys.stdin:
        #your code here
        #reducer function will consume the key value pairs emitted by mapper
        #so create and array data for every single line which will essentially be length of two containing the 
        #key and the value. Note that we split on the tab, which we input into the output of our mapper.
        data = line.strip().split("\t")
        
        #If for some reason data is less than or greater than length two, we continue on.
        #There's something wrong with this key value pair and we shouldn't process it.
        if len(data) != 2:
            continue
          
        this_key, count = data
        
        
        ########### CODE 1 ##############
        
        #So if this is a new key, let's submit the final key value pair.
        if last_key and last_key != this_key:
            print "{0}\t{1}".format(last_key, aadhaar_generated)
            aadhaar_generated = 0 #Set aadhaar_generated value = 0 for new key
        
        last_key = this_key #Set this key as a old key
        #Otherwise, let's add the number of aadhaar_generated in this particular key value pair to
        #the total number of aadhaar_generated for this key and let's continue onto the next value.
        aadhaar_generated += float(count)
        
        #We include this last if clause for the last key in our data. Because there's no next key after the
        #last key.If we didn't have this, we could not admit a key value pair for the final key in our intermediate
        #data. So here after we've done all this other processing up here, we just say for the last key, let's make sure
        #we emit the key value pair.
        if last_key != None:
            print "{0}\t{1}".format(last_key, aadhaar_generated)
            
            
        ########### CODE 2 ##############
        # if this is the first iteration
        if not last_key:
            last_key = this_key

        # if they're the same, log it
        if this_key == last_key:
            aadhaar_generated += float(count)
        else:
            # state change (previous line was k=x, this line is k=y)
            result = [last_key, aadhaar_generated]
            #print("\t".join(str(v) for v in result))
            print "{0}\t{1}".format(last_key, aadhaar_generated)
            last_key = this_key
            aadhaar_generated = float(count)

    # this is to catch the final counts after all records have been received.
    print "{0}\t{1}".format(last_key, aadhaar_generated)        
    #print("\t".join(str(v) for v in [last_turf, turf_count]))
reducer()
