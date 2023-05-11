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

#eigienパス,ele_cd(画像の座標)パス作成
for i in range(3):
    path = []
    for j in range(len(level_2)):
        name_1 = level_1[0]
        name_2 = name_1 + level_2[j] + level_4[i+2]
        for l in range(2):
            name_5 = name_2 + level_5[l+3+j*6] + last[0]
            path.append(name_5)
    exec("{}_path = {}".format(type[i+2],path))#pathに溜め込んだアドレスをここで指定した名前の変数として保存

#elect_figパス作成
for i in range(2):
    path = []
    for j in range(len(level_2)):
        name_1 = level_1[0]
        name_2 = name_1 + level_2[j] + level_4[i+5]
        for l in range(2):
            name_5 = name_2 + level_5[l+3+j*6] + last[1]
            path.append(name_5)
    exec("{}_path = {}".format(type[i+5],path))#pathに溜め込んだアドレスをここで指定した名前の変数として保存

#電極数
ch=60
#
#n_features = 6
#電極の座標データ作成，画像保存
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
#画像の初期化
for i in range(len(elect_fig_0_path)):
    #shutil.copy('elect_fig_js8.png', elect_fig_0_path[i])
    #shutil.copy('elect_fig_js8.png', elect_fig_1_path[i])
    shutil.copy('UP1_192.png', elect_fig_0_path[i])
    shutil.copy('UP1_192.png', elect_fig_1_path[i])

#固有値ベクトルを呼び出して脳画像にプロット

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

    
    
#plt.colorbar(s)
#for i in range(len(eigen_val_path)):
##for i in range(2):
#    #v=np.load(eigen_val_path[i])
#    #b=np.load(eigen_bec_path[i])   
#    crd=np.load(elect_crd_path[i])
#    v_filt = abs(np.concatenate((b[:, :n_features // 2], b[:, -n_features // 2:]),axis=1))
#    eigien_1 = v_filt[:,0]#A vs B のB
#    eigien_0 = v_filt[:,-1]#A vs B のA
#    #最大固有値空間のプロット（A vs B のA）
#    #im=Image.open(elect_fig_0_path[i])
#    im=Image.open("task_classification/listen_image/elect_fig_0_csp_01_250.png")
#    im_list=np.asarray(im)
#    plt.imshow(im_list)
#    # "c" is value of scatter
#    sc = plt.scatter(crd[:,0],crd[:,1],c=eigien_0,s=100,cmap=cm.jet,alpha=0.5)
#    plt.colorbar(sc)
#    plt.savefig(elect_fig_0_path[i])
#    plt.clf()
#    #最小固有値空間のプロット(A vs B のB)
#    im=Image.open(elect_fig_1_path[i])
#    im_list=np.asarray(im)
#    plt.imshow(im_list)
#    sc = plt.scatter(crd[:,0],crd[:,1],c=eigien_1,s=100,cmap=cm.jet,alpha=0.5)
#    plt.colorbar(sc)
#    plt.savefig(elect_fig_1_path[i])
#    plt.clf()
