import os
import json


path = r"../data/source_images3"
# f= open("../data_proc/raw_skeletons/skeletons_info.txt", 'w+')

count = 0
couldRename = 0


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



FullList = []
imagecount = 1
for subdir, dirs, files in os.walk(path,topdown=True):
    dirs.sort()
    for dir in dirs:
        try:
            FullList = []
            if str(dir).endswith('.json'):
                continue
            count += 1    
            print("proccessing file#" + str(count)) 
            print(dir) 
            pathtofile =  os.path.join(subdir,dir)
            command = "python3 /home/mina_atef0/Desktop/AlphaPose/demo.py --indir {} --outdir {} --detbatch 4 ".format(pathtofile,subdir)
            os.system(command)
            
            with open('data_proc/alphapose-results.json') as f:
                items = json.load(f)
                for item in items:
                    itemList = []
                    class_name = dir.split('_')[0]
                    itemList.append(Classes[class_name])
                    itemList.append(count)
                    itemList.append(int(item['image_id'][:5]) + 1)
                    itemList.append(class_name)
                    itemList.append(dir + '/' + item['image_id'])
                    itemList = itemList + item['keypoints']
                    FullList.append(itemList)
                FullList = sorted(FullList, key= lambda x: x[2])
                with open('../data_proc/raw_skeletons/skeletons_info/'+dir + '.txt', 'w+') as outfile:
                    json.dump(FullList, outfile)
        except:
            pass


    print("couldn't rename  " +str(couldRename) )

    print("made  " +str(count) )