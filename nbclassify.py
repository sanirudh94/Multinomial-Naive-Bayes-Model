import sys
import os
import string


def readFileData(hash1):
    fileop = open("nbmodel.txt","r")
    filewr = open("abc.txt","w")
    for line in fileop:
        parts = line.split()
        hash1[parts[0]] = {}
        hash1[parts[0]][parts[1]] = {}
        hash1[parts[0]][parts[3]] = {}
        hash1[parts[0]][parts[5]] = {}
        hash1[parts[0]][parts[7]] = {}
        hash1[parts[0]][parts[1]] = parts[2]
        hash1[parts[0]][parts[3]] = parts[4]
        hash1[parts[0]][parts[5]] = parts[6]
        hash1[parts[0]][parts[7]] = parts[8]
        
def determinefile(probabPT, probabPD, probabNT, probabND):
    if((probabPT > probabPD)and(probabPT > probabNT)and(probabPT > probabND)):
        PT = "PT"
        return PT
    elif((probabPD > probabPT) and (probabPD > probabNT) and (probabPD > probabND)):
        PD = "PD"
        return PD
    elif((probabNT > probabPT) and (probabNT > probabPD) and (probabNT > probabND)):
        NT = "NT"
        return "NT"
    else:
        ND = "ND"
        return ND

def writeprobableclass(probableclass,w):
    if(probableclass == "PT"):
        labela = "truthful"
        labelb = "positive"
        path = w

    elif(probableclass == "PD"):
        labela = "deceptive"
        labelb = "positive"
        path = w

    elif(probableclass == "NT"):
        labela = "truthful"
        labelb = "negative"
        path = w

    else:
        labela = "deceptive"
        labelb = "negative"
        path = w

    stringifier = labela+" "+labelb+" "+path
    filewriter.write(stringifier+"\n")

        

def classifyFile(fileptr,hash1,w):
    probabPT =0.0
    probabPD =0.0
    probabNT =0.0
    probabND =0.0
    stopwords = "a about above after again against all am an and any are aren't as at be because been before being below between both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself know nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves"
    stopwordslist = stopwords.split()
    exclude = set(string.punctuation)
    fileptr = ''.join(ch for ch in fileptr if ch not in exclude)
    parts = fileptr.split()
    for words in parts:
        words = words.lower()
        if words in stopwordslist:
            continue
        elif words in hash1:
            probabPT = probabPT + float(hash1[words]['PT'])
            probabPD = probabPD + float(hash1[words]['PD'])
            probabNT = probabNT + float(hash1[words]['NT'])
            probabND = probabND + float(hash1[words]['ND'])
    probableclass = determinefile(probabPT,probabPD, probabNT, probabND)
    writeprobableclass(probableclass,w)
    
      
def read_development_file(filename):
    hash1 ={}
    readFileData(hash1)
    positivedirs = next(os.walk(filename))[1]
    for positivedirectory in positivedirs:
        if(positivedirectory.startswith("positive")):
            isPositive = True
        else:
            isPositive = False
        if(positivedirectory.startswith("negative")):
            isNegative = True
        else:
            isNegative = False
        x = os.path.join(filename,positivedirectory)
        truthordecep = next( os.walk(x))[1]
        for truthordecepdir in truthordecep:
            if(truthordecepdir.startswith("deceptive")):
                isDeceptive = True
            else:
                isDeceptive = False
            if(truthordecepdir.startswith("truthful")):
                isTruthful = True
            else:
                isTruthful = False
            y = os.path.join(x,truthordecepdir)
            folder = next(os.walk(y))[1]
            for fold in folder:
                z = os.path.join(y,fold)
                files = next(os.walk(z))[2]
                for fileRead in files:
                    w = os.path.join(z,fileRead)
                    fileop = open(w,"r")
                    classifyFile(fileop.read(),hash1,w) 
                        
                    


filename = sys.argv[1]
filewriter = open("nboutput.txt","w")
read_development_file(filename)

