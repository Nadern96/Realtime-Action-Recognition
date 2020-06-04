import os
import json


path = r"/home/mina_atef0/Desktop/AlphaPose/chossen"
f= open("data_proc/raw_skeletons/skeletons_info.txt", 'w+')

count = 0
couldRename = 0
Classes = {'1':1,'2':2,'3':3}

for subdir, dirs, files in os.walk(path,topdown=True):
    for dir in dirs:
        if str(dir).endswith('.json'):
            continue
        count += 1    
        print("proccessing file#" + str(count)) 
        print(dir) 
        pathtofile =  os.path.join(subdir,dir)
        command = "python3 demo.py --indir {} --outdir {}".format(pathtofile,subdir)
        os.system(command)

        with open('data_proc/alphapose-results.json') as f:
            items = json.load(f)
            for item in items:
                class_name = dir.split('_')[0]
                itemList.append(Classes[class_name])
                itemList.append(count)
                itemList.append(int(item['image_id'][:5]))
                itemList.append(class_name)
                itemList.append(dir + '/' + item['image_id'])
                itemList = itemList + item['keypoints']
                print(itemList)
                break




print("couldn't rename  " +str(couldRename) )

print("made  " +str(count) )