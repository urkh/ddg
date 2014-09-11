import sys
import urllib2
import json
import ipdb as pdb


def get_results(ddg):
    
    results = []
    
    for ret in ddg.get("RelatedTopics"):

        if ret.has_key("Topics"):
            for rett in ret.get("Topics"):
                result_inf = {"description":rett["Text"], "url":rett["FirstURL"]}

        else:
            result_inf = {"description":ret["Text"], "url":ret["FirstURL"]}

        results.append(result_inf)

    for result in results:
        print HEADER+" ["+str(results.index(result))+"]: "+BLUE+result.get("description")
        print HEADER+" ["+str(results.index(result))+"]: "+GREEN+result.get("url")
        print "\n"


#pdb.set_trace()
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


param = sys.argv[1]



if param == "-s":

    #params = 'hola'
    
    for arg in sys.argv:
        params+=arg+"+"

    #pdb.set_trace()

    ddg = urllib2.urlopen("http://api.duckduckgo.com/?q=hola%2Bmundo&format=json&no_html=1")
    #pdb.set_trace()
    get_results(json.load(ddg))

