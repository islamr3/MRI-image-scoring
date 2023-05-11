from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import os
import numpy as np
import warnings;warnings.filterwarnings('ignore')
import pprint
import shutil

type = ["X","Y","eigen_val","eigen_bec","elect_crd","elect_fig_0","elect_fig_1","tpr","score"]

level_1 = ["task_classification/"]

level_2 = ["listen_image/","listen_voice/","image_voice/",
           "listen_01/","image_01/","voice_01/"]

level_4 = ["","label_","eigen_val_","eigen_bec_","elect_crd_","elect_fig_0_","elect_fig_1_","tpr_","score_"]

level_3 = ["listen_01/","image_01/","voice_01/"]

level_5 = ["pow_01_250","pow_01_50","pow_01_50_con","csp_01_250","csp_01_50","csp_01_50_con",
           "pow_02_250","pow_02_50","pow_02_50_con","csp_02_250","csp_02_50","csp_02_50_con",
           "pow_12_250","pow_12_50","pow_12_50_con","csp_12_250","csp_12_50","csp_12_50_con",
           "pow_l01_250","pow_l01_50","pow_l01_50_con","csp_l01_250","csp_l01_50","csp_l01_50_con",
           "pow_i01_250","pow_i01_50","pow_i01_50_con","csp_i01_250","csp_i01_50","csp_i01_50_con",
           "pow_v01_250","pow_v01_50","pow_v01_50_con","csp_v01_250","csp_v01_50","csp_v01_50_con"]

last = [".npy",".png"]


for i in range(3):
    path = []
    for j in range(len(level_2)):
        name_1 = level_1[0]
        name_2 = name_1 + level_2[j] + level_4[i+2]
        for l in range(2):
            name_5 = name_2 + level_5[l+3+j*6] + last[0]
            path.append(name_5)
    exec("{}_path = {}".format(type[i+2],path))


for i in range(2):
    path = []
    for j in range(len(level_2)):
        name_1 = level_1[0]
        name_2 = name_1 + level_2[j] + level_4[i+5]
        for l in range(2):
            name_5 = name_2 + level_5[l+3+j*6] + last[1]
            path.append(name_5)
    exec("{}_path = {}".format(type[i+5],path))


ch=60
#
#n_features = 6

print("Do you want to create coordinate data? y or n")
ans = input()
#ans = "n"
if ans=="y":
    #im = Image.open("elect_fig_js8.png")
    im = Image.open("UP1_192.png")
    im_list = np.asarray(im)
    plt.imshow(im_list)
    crd = np.array(plt.ginput(n=ch,timeout=0))
    #crd = Coordinate of scatter
    for i in range(len(elect_crd_path)):
        np.save(elect_crd_path[i],crd)
if ans=="n":

    crd_copy =  np.load("task_classification/listen_image/elect_crd_csp_01_250.npy" )
    for i in range(len(elect_crd_path)):
        np.save(elect_crd_path[i],crd_copy)

for i in range(len(elect_fig_0_path)):
    #shutil.copy('elect_fig_js8.png', elect_fig_0_path[i])
    #shutil.copy('elect_fig_js8.png', elect_fig_1_path[i])
    shutil.copy('UP1_192.png', elect_fig_0_path[i])
    shutil.copy('UP1_192.png', elect_fig_1_path[i])



#b=np.load('P2_T.npy')
#c=b.transpose()
#im=Image.open("task_classification/listen_image/elect_fig_0_csp_01_250.png")
##colors = np.random.rand(50)
#colors = c*100;
#im_list=np.asarray(im) 
#fig, ax = plt.subplots()
##fig, ax = plt.subplots()
#for i in range(len(c)):
#    #fig, ax = plt.subplots()
#    plt.imshow(im_list)
#    s=ax.scatter(crd[i,0], crd[i,1],colors[i],c[i]*500,alpha=0.5)


im=Image.open("task_classification/listen_image/elect_fig_0_csp_01_250.png")
im_list=np.asarray(im) 

b=np.load('P1_T.npy')
c=b.transpose()
c = c*100 #area
s=b.transpose()   #Color
fig, ax = plt.subplots()
plt.imshow(im_list)
##s=ax.scatter(crd[:,0], crd[:,1],c,s,cmap=cm.jet,alpha=0.5)
#s=ax.scatter(crd[:,0], crd[:,1],200,s,cmap=cm.jet,alpha=0.5) #robi previous
s=ax.scatter(crd[:,0], crd[:,1],150,s,cmap=plt.cm.OrRd,alpha=0.6)
fig.colorbar(s,ax=ax)
plt.show()
plt.savefig(elect_fig__path[0])
#fig, ax = plt.subplots()

    