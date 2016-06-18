#!/usr/bin/env python3

# Psudo code
# 
# open files to copy
# Make new directory
# make new files with replaces strings
# add model to world file

import os
import errno
import sys
import fileinput
import shutil

numCopies = 3

templateDir = '/home/matt/Workspace/GazeboDev/quad_model_dev/modelDev/quad_2292_template'
copyDir = '/home/matt/Workspace/GazeboDev/quad_model_dev/Gen_Models'
#newpath = r'C:\Program Files\arbitrary' 
templateVar = '{$modelName}'
modelName = 'quad_2292' # append _1 to each model

runName = 'test1'
worldFile = '/home/matt/Workspace/GazeboDev/quad_model_dev/modelDev/quad_2292_template.world'



confFileName = 'model.config'
sdfFileName = 'model.sdf'

confFile = open(os.path.join(templateDir,confFileName),'r')
sdfFile = open(os.path.join(templateDir,sdfFileName),'r')


for i in range(1,numCopies+1):
	newModelName = modelName+'_'+str(i)
	newDir = os.path.join(copyDir,newModelName)
	os.makedirs(newDir)
	 
	newConfFile = open(os.path.join(newDir,confFileName),'w')
	for line in confFile:
		newConfFile.write(line.replace(templateVar,newModelName))
	newConfFile.close()
	confFile.seek(0,0)
	
	newSdfFile = open(os.path.join(newDir,sdfFileName),'w')
	for line in sdfFile:
		newSdfFile.write(line.replace(templateVar,newModelName))
	newSdfFile.close()
	sdfFile.seek(0,0)
	

confFile.close()
sdfFile.close()

#####
# dev code below

# os.makedirs(path, exist_ok=True)
#f1 = open('file1.txt', 'r')
#f2 = open('file2.txt', 'w')
#for line in f1:
#    f2.write(line.replace('old_text', 'new_text'))
#f1.close()
#f2.close()

#def copy(src, dest):
    #try:
        #shutil.copytree(src, dest)
    #except OSError as e:
        ## If the error was caused because the source wasn't a directory
        #if e.errno == errno.ENOTDIR:
            #shutil.copy(src, dest)
        #else:
            #print('Directory not copied. Error: %s' % e)


#from os import walk

#f = []
#for (dirpath, dirnames, filenames) in walk(mypath):
    #f.extend(filenames)
    #break
    
    
#from os import listdir
#from os.path import isfile, join
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
