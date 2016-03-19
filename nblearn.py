import sys
import os
import string
import math

    
def learnBayes(fileptr,hash1,isPositive,isNegative,isDeceptive,isTruthful):
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
            if(isPositive and isTruthful):
                if(hash1[words]['PT'] == {}):
                    hash1[words]['PT'] = 1
                else:
                    hash1[words]['PT'] = hash1[words]['PT']+1
            elif(isPositive and isDeceptive):
                if(hash1[words]['PD'] == {}):
                    hash1[words]['PD'] = 1
                else:
                    hash1[words]['PD'] = hash1[words]['PD'] +1
            elif(isNegative and isDeceptive):
                if(hash1[words]['ND'] == {}):
                    hash1[words]['ND'] = 1
                else:
                    hash1[words]['ND'] = hash1[words]['ND']+1
            elif(isNegative and isTruthful):
                if(hash1[words]['NT'] == {}):
                    hash1[words]['NT'] = 1
                else:
                    hash1[words]['NT'] = hash1[words]['NT']+1
                    
                
        else:
            hash1[words]={}
            hash1[words]['PT']={}
            hash1[words]['PD'] = {}
            hash1[words]['ND'] = {}
            hash1[words]['NT'] = {}
            if(isPositive and isTruthful):
                hash1[words]['PT'] = 1
            elif(isPositive and isDeceptive):
                hash1[words]['PD'] = 1
            elif(isNegative and isDeceptive):
                hash1[words]['ND'] = 1
            elif(isNegative and isTruthful):
                hash1[words]['NT'] = 1


def calculateprobability(hash1,count,PTclasscount,PDclasscount,NTclasscount,NDclasscount):
    fileop = open("nbmodel.txt","w")
    for words in hash1:
        PTcount = count+PTclasscount
        PDcount = count+PDclasscount
        NTcount = count+NTclasscount
        NDcount = count+NDclasscount
        probabPTclass = math.log(hash1[words]['PT']+1)- math.log(PTcount)
        hash1[words]['PT'] = probabPTclass
        probabPDclass = math.log(hash1[words]['PD']+1)- math.log(PDcount)
        hash1[words]['PD'] = probabPDclass
        probabNTclass = math.log(hash1[words]['NT']+1)- math.log(NTcount)
        hash1[words]['NT'] = probabNTclass
        probabNDclass = math.log(hash1[words]['ND']+1)- math.log(NDcount)
        hash1[words]['ND'] = probabNDclass

    for key in hash1:
        stringprobability = key+' ' + 'PT '+ str(hash1[key]['PT']) + ' PD '+ str(hash1[key]['PD'])+ ' NT ' + str(hash1[key]['NT']) + ' ND ' +str( hash1[key]['ND']);
        fileop.write(stringprobability+"\n")
    fileop.close()
    

def probabilisticDetermination(hash1):
    count = 0
    PTclasscount =0
    PDclasscount =0
    NTclasscount =0
    NDclasscount =0
    for words in hash1:
        count = count+1
        if(hash1[words]['PT'] == {}):
            hash1[words]['PT'] = 0
        

        if(hash1[words]['PD'] == {}):
            hash1[words]['PD'] = 0

        if(hash1[words]['ND'] == {}):
            hash1[words]['ND'] = 0

        if(hash1[words]['NT'] == {}):
            hash1[words]['NT'] = 0
        PTclasscount += hash1[words]['PT']
        PDclasscount += hash1[words]['PD']
        NTclasscount += hash1[words]['NT']
        NDclasscount += hash1[words]['ND']
        
    calculateprobability(hash1,count,PTclasscount,PDclasscount,NTclasscount,NDclasscount)
    
    
def read_training_file(filename):
    hash1 ={}
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
                    fileop = open(os.path.join(z,fileRead),"r")
                    learnBayes(fileop.read(),hash1,isPositive,isNegative,isDeceptive,isTruthful)
    probabilisticDetermination(hash1)
        
            
training_file = sys.argv[1]
read_training_file(training_file)
