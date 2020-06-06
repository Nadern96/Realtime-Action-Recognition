'''
python video2images.py \
        -i /media/nader/Local\ Disk/Nader\ 2014/CSE_2ndYear/Graduation\ Project/hmdb51_org/clap/'boom_snap_clap_(challenge)_HARDCORE_VERSION!_clap_u_nm_np1_fr_bad_0.avi' \
        -o /media/nader/Local\ Disk/Nader\ 2014/CSE_2ndYear/Graduation\ Project/hmdb51_org \
        --sample_interval 2 \
        --max_frames 30
'''

import os
path = r"../Biking"
image_folder = "../../Realtime-Action-Recognition/data/source_images3/"
#change dir to tools folder
#os.chdir("tools")

f= open("../../Realtime-Action-Recognition/data/source_images3/valid_images.txt", 'w+')

for subdir, dirs, files in os.walk(path,topdown=True):
    for file in files:   
        if str(file).endswith('.avi'):
          pathtofile =  os.path.join(subdir,file)
          classname = subdir[subdir.rfind('/')+1:] +'_'
          classname += file
          folderpath =  os.path.join(image_folder,classname)
          os.mkdir(folderpath)
          command = "python3 video2images.py -i {} -o {} --sample_interval 2 --max_frames 56".format(pathtofile,folderpath)
          os.system(command)
          list = os.listdir(folderpath) # dir is your directory path
          number_files = len(list)
          
          f.write(classname)
          f.write("\n")
          f.write("{} {}".format(0,number_files-1))
          f.write("\n \n")

f.close()