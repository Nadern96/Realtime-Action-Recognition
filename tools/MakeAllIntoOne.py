import os
import json


path = r"../data_proc/raw_skeletons/numbered/"
f= open("../data_proc/raw_skeletons/skeletons_info.txt", 'w+')

Classes = {'clap':1,
          'hit':2, 
          'jump':3,
          'kick':4,
          'punch':5,
          'push':6,
          'run':7,
          'shake':8,
          'sit':9,
          'situp':10,
          'stand':11,
          'turn':12,
          'walk':13,
          'wave':14,
}

count = 0 
full = []
ImageCount = 0
itemCount = 0
for subdir, dirs, files in os.walk(path,topdown=True):
    files.sort()
    for file in files:
        count += 1    
        print("proccessing file#" + file) 

        pathtofile =  os.path.join(subdir,file)
        
        with open(pathtofile) as f:
            items = json.load(f)
            for item in items:
                item[3] += item[3] + ImageCount
                itemCount += 1
                full.append(item)
            


  with open('../data_proc/raw_skeletons/skeletons_info.txt', 'w+') as outfile:
                    json.dump(items, outfile)

