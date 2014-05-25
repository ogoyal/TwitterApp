# Count hashtags

def main():
    
    fileName = input("filename: ")

    try:
        # open file for reading, using more liberal character set
        inFile = open(fileName,"r",encoding="utf-8")
    except:
        print("bad file name")
        return # stop program if not a good file name

    # make an empty dictionary
    hashDict = {}
    # file reading loop

    while True:
        line = inFile.readline() #read a new line
        if line == "": # "" indicates file is over
            break
        line = line.strip() # removes newline at end
        
        # line is a string
        fields = line.split('"') # break into list of fields
        for tweet in fields: # treat each field as if
            # it was a tweet; can't hurt
            tweet = tweet.replace("#"," #") # make sure
            # each hash tag is in its own word
            wList = tweet.split()  # break into words
            # wList is a list
            for w in wList:
                w = w.lower() # make sure it is all lower case
                if w[0] == "#":
                    # possible hash tag!
                    # remove punctuation at the end
                    while w != "":
                        last = w[-1]
                        if not last.isalpha():
                            w = w[0:-1]
                        else:
                            break
                    # if there is anything still there...
                    if w != "":
                        # update the count in dictionary
                        if w in hashDict:
                            # hash tag is already there
                            count = hashDict[w]
                            count = count+1
                        else:
                            # tag is not in dictionary
                            count = 1
                        # store new count back in dictionary
                        hashDict[w] = count
    # finally, sort and copy to output               
    outList = []
    # copy dictionary items into a list
    for key in hashDict:
        item = [hashDict[key],key] # each dictionary item becomes
        # a list with two elements
        outList.append(item) # store these pairs in the big list
    # sort the list
    outList.sort(reverse=True) # from high to low counts
    # first item is hashtag used to select file; skip it
    for i in range(1,11):
        print(outList[i][0], outList[i][1])
            
main()
input("Press enter to exit.")
        
