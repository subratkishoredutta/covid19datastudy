import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

new = pd.read_csv("new.csv") 
covid= new.copy()

covid=covid.drop(labels=["Last Update"],axis=1)

## drawing graphs
## dividing the dataset based on the different places

india=covid.loc[covid['Country/Region']=='India']
china=covid.loc[covid['Country/Region']=='Mainland China']
italy=covid.loc[covid['Country/Region']=='Italy']
germany=covid.loc[covid['Country/Region']=='Germany']


##china
Anhui = covid.loc[covid['Province/State']=='Anhui']
Beijing = covid.loc[covid['Province/State']=='Beijing']
Chongqing = covid.loc[covid['Province/State']=='Chongqing']
Fujian = covid.loc[covid['Province/State']=='Fujian']
Gansu = covid.loc[covid['Province/State']=='Gansu ']
Guangdong = covid.loc[covid['Province/State']=='Guangdong']
Guangxi = covid.loc[covid['Province/State']=='Guangxi']
Guizhou = covid.loc[covid['Province/State']=='Guizhou']
Hainan = covid.loc[covid['Province/State']=='Hainan']
Hebei = covid.loc[covid['Province/State']=='Hebei']
Heilongjiang = covid.loc[covid['Province/State']=='Heilongjiang']
Henan = covid.loc[covid['Province/State']=='Henan']
Hong_Kong = covid.loc[covid['Province/State']=='Hong Kong']
Hubei = covid.loc[covid['Province/State']=='Hubei']
Hunan = covid.loc[covid['Province/State']=='Hunan']
Inner_Mongolia = covid.loc[covid['Province/State']=='Inner Mongolia']
Jiangsu = covid.loc[covid['Province/State']=='Jiangsu']
Jiangxi = covid.loc[covid['Province/State']=='Jiangxi ']
Jilin = covid.loc[covid['Province/State']=='Jilin']
Liaoning = covid.loc[covid['Province/State']=='Liaoning']
Ningxia = covid.loc[covid['Province/State']=='Ningxia']
Qinghai = covid.loc[covid['Province/State']=='Qinghai']
Shaanxi = covid.loc[covid['Province/State']=='Shaanxi ']
Shandong = covid.loc[covid['Province/State']=='Shandong']
Shanghai = covid.loc[covid['Province/State']=='Shanghai']
Shanxi = covid.loc[covid['Province/State']=='Shanxi']
Sichuan = covid.loc[covid['Province/State']=='Sichuan']
Taiwan = covid.loc[covid['Province/State']=='Taiwan']
Tianjin = covid.loc[covid['Province/State']=='Tianjin']
Tibet = covid.loc[covid['Province/State']=='Tibet']
Xinjiang = covid.loc[covid['Province/State']=='Xinjiang']
Yunnan = covid.loc[covid['Province/State']=='Yunnan']
Zhejiang = covid.loc[covid['Province/State']=='Zhejiang']

names = {"Anhui":Anhui,"Beijing":Beijing,"Chongqing":Chongqing,"Fujian":Fujian,"Gansu" : Gansu,"Guangdong": Guangdong,"Guangxi" : Guangxi,"Guizhou" : Guizhou,
         "Hainan":Hainan,"Hebei":Hebei,"Heilongjiang":Heilongjiang,"Henan":Henan, "Hong Kong" :Hong_Kong,"Hunan":Hunan,"Inner Mongolia":Inner_Mongolia,"Jiangsu":Jiangsu,
         "Jiangxi":Jiangxi,"Jilin":Jilin,"Liaoning":Liaoning,"Ningxia":Ningxia,"Qinghai":Qinghai,"Shaanxi":Shaanxi,"Shandong":Shandong,"Shanghai":Shanghai,"Shanxi" : Shanxi,"Sichuan" : Sichuan,
         "Taiwan":Taiwan,"Tianjin" : Tianjin,"Tibet" : Tibet,"Xinjiang":Xinjiang,"Yunnan":Yunnan,"Zhejiang":Zhejiang}

new = ['Anhui','Beijing','Chongqing','Fujian','Gansu','Guangdong','Guangxi','Guizhou','Hainan','Hebei','Heilongjiang','Henan','Hong Kong',
'Hunan','Inner Mongolia','Jiangsu','Jiangxi','Jilin','Liaoning','Ningxia','Qinghai','Shaanxi','Shandong','Shanghai','Shanxi','Sichuan','Taiwan','Tianjin',
'Tibet','Xinjiang','Yunnan','Zhejiang']

fig1 = plt.figure(figsize=(20,10))
ax1=plt.subplot2grid((1,1),(0,0))
ax1.grid(True)
ax1.plot(germany['ObservationDate'],germany['Confirmed'],color = 'blue',label="Germany")
ax1.plot(italy['ObservationDate'],italy['Confirmed'],color = '#dbb704',label="Italy")
ax1.plot(india['ObservationDate'],india['Confirmed'],color = 'red',label="India")
ax1.scatter(germany['ObservationDate'],germany['Confirmed'],color = 'blue')
ax1.scatter(italy['ObservationDate'],italy['Confirmed'],color = '#dbb704')
ax1.scatter(india['ObservationDate'],india['Confirmed'],color = 'red')
for label1 in ax1.xaxis.get_ticklabels():
    label1.set_rotation(90)
    label1.set_color('#a19dd9')
for label1 in ax1.yaxis.get_ticklabels():
    label1.set_color('#a19dd9')
ax1.xaxis.label.set_color('#4c3ab0')
ax1.yaxis.label.set_color('#4c3ab0')
ax1.spines["left"].set_color('#4c3ab0')
ax1.spines["bottom"].set_color('#4c3ab0')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_linewidth(2)
ax1.spines['bottom'].set_linewidth(2)
plt.title('Confirmed cases vs dates\nin various countries',color="#4c3ab0",fontsize=25)
plt.xlabel("Dates",fontsize=20)
plt.ylabel("Confirmed cases",fontsize=20)
plt.legend()
fig1.savefig('various.jpg')
plt.show()


fig2 = plt.figure(figsize=(20,20))
ax2=plt.subplot2grid((1,1),(0,0))
ax2.grid(True)
for name in new:
    m=names[name]
    ax2.plot(m['ObservationDate'],m['Confirmed'],label=name)
    for label2 in ax2.xaxis.get_ticklabels():
        label2.set_rotation(90)
        label2.set_color('#a19dd9')
    for label2 in ax2.yaxis.get_ticklabels():
        label2.set_color('#a19dd9')
ax2.xaxis.label.set_color('#4c3ab0')
ax2.yaxis.label.set_color('#4c3ab0')
ax2.spines["left"].set_color('#4c3ab0')
ax2.spines["bottom"].set_color('#4c3ab0')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_linewidth(2)
ax2.spines['bottom'].set_linewidth(2)
plt.title('Confirmed cases vs dates\nin various provinces of China',color='#4c3ab0',fontsize=25)
plt.xlabel("Dates",fontsize=20)
plt.ylabel("Confirmed cases",fontsize=20)
plt.legend()
#ax2.grid(True,color='c',linestyle='-')
fig2.savefig('within_China.jpg')
plt.show()


fig3 = plt.figure(figsize=(20,10))
ax3=plt.subplot2grid((1,1),(0,0))
ax3.grid(True)
ax3.plot(Hubei['ObservationDate'],Hubei['Confirmed'],color="blue",label="confimed")
ax3.plot(Hubei['ObservationDate'],Hubei['Deaths'],color="red",label="Deaths")
ax3.scatter(Hubei['ObservationDate'],Hubei['Confirmed'],color="blue")
ax3.scatter(Hubei['ObservationDate'],Hubei['Deaths'],color="red")
for label3 in ax3.xaxis.get_ticklabels():
    label3.set_rotation(90)
    label3.set_color('#a19dd9')
for label3 in ax3.yaxis.get_ticklabels():
    label3.set_color('#a19dd9')
ax3.text('01/23/2020',35000,' Lockdown in wuhan and\n   other cities in Hubei\n        (01/23/2020)',fontsize=15,color='#4c3ab0')
ax3.axvline('01/23/2020',color='#dbb704',linestyle='--',linewidth=3)
ax3.xaxis.label.set_color('#4c3ab0')
ax3.yaxis.label.set_color('#4c3ab0')
ax3.spines["left"].set_color('#4c3ab0')
ax3.spines["bottom"].set_color('#4c3ab0')
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['left'].set_linewidth(2)
ax3.spines['bottom'].set_linewidth(2)
plt.xlabel("Dates",fontsize=20)
plt.ylabel("Cases",fontsize=20)
plt.title("Cases in Hubei Province of China",color='#4c3ab0',fontsize=25)
plt.legend()
fig3.savefig('china.jpg')
plt.show()
#3bc7ff

fig4 = plt.figure(figsize=(20,10))
ax4=plt.subplot2grid((1,1),(0,0))
ax4.grid(True)
ax4.plot(india['ObservationDate'],india['Confirmed'],color="blue",label="Confimed")
ax4.plot(india['ObservationDate'],india['Deaths'],color="red",label="Deaths")
ax4.scatter(india['ObservationDate'],india['Confirmed'],color="blue")
ax4.scatter(india['ObservationDate'],india['Deaths'],color="red")
for label4 in ax4.xaxis.get_ticklabels():
    label4.set_rotation(90)
    label4.set_color('#a19dd9')
for label4 in ax4.yaxis.get_ticklabels():
    label4.set_color('#a19dd9')
ax4.text('01/22/2020',35,' Janata Curfew\n   (03/23/2020)',color='#4c3ab0',fontsize=15)
ax4.axvline('01/22/2020',color='#dbb704',linestyle='--',linewidth = 3)
ax4.xaxis.label.set_color('#4c3ab0')
ax4.yaxis.label.set_color('#4c3ab0')
ax4.spines["left"].set_color('#4c3ab0')
ax4.spines["bottom"].set_color('#4c3ab0')
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
ax4.spines['left'].set_linewidth(2)
ax4.spines['bottom'].set_linewidth(2)
leg = ax4.legend()
leg.get_frame().set_alpha(0.8)
plt.xlabel("Dates",fontsize=20)
plt.ylabel("Cases",fontsize=20)
plt.title("Cases in India",color='#4c3ab0',fontsize=25,fontstyle='normal')
fig4.savefig('india.jpg')
plt.show()


fig5 = plt.figure(figsize=(20,10))
ax5=plt.subplot2grid((1,1),(0,0))
ax5.grid(True)
ax5.plot(italy['ObservationDate'],italy['Confirmed'],color="blue",label="Confimed")
ax5.plot(italy['ObservationDate'],italy['Deaths'],color="red",label="Deaths")
ax5.scatter(italy['ObservationDate'],italy['Confirmed'],color="blue")
ax5.scatter(italy['ObservationDate'],italy['Deaths'],color="red")
for label5 in ax5.xaxis.get_ticklabels():
    label5.set_rotation(90)
    label5.set_color('#a19dd9')
for label5 in ax5.yaxis.get_ticklabels():
    label5.set_color('#a19dd9')
ax5.text('03-09-2020',35000,' total lockdown\n   (03/09/2020)',color='#4c3ab0',fontsize=15)
ax5.axvline('03-09-2020',color='#dbb704',linestyle='--',linewidth = 3)
ax5.xaxis.label.set_color('#4c3ab0')
ax5.yaxis.label.set_color('#4c3ab0')
ax5.spines["left"].set_color('#4c3ab0')
ax5.spines["bottom"].set_color('#4c3ab0')
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
ax5.spines['left'].set_linewidth(2)
ax5.spines['bottom'].set_linewidth(2)
leg = ax5.legend()
leg.get_frame().set_alpha(0.8)
plt.xlabel("Dates",fontsize=20)
plt.ylabel("Cases",fontsize=20)
plt.title("Cases in Italy",color='#4c3ab0',fontsize=25,fontstyle='normal')
fig5.savefig('italy.jpg')
plt.show()

def date_con(X_con_mod):
    for i in range(len(X_con_mod)):
        u=X_con_mod[i][0]
        n=int(u[0:2])
        m=int(u[3:5])
        x=int(u[6:10])
        X_con_mod[i][3]=((x*365.25)+m+(n*30.4375))/100000
    return X_con_mod

ind = india.copy()

ind= ind.drop(labels=["Province/State","Country/Region"],axis=1)
a=np.zeros((len(ind),1))

#model 1
X_con_mod = np.array(ind.drop(labels=['Confirmed'],axis=1))
X_con_mod = np.append(X_con_mod,a,axis=1)
X_con_mod = date_con(X_con_mod)
X_con_mod = np.delete(X_con_mod,0,1)
Y_con_mod = np.array(ind["Confirmed"])
X_con_mod = np.transpose(X_con_mod)
Y_con_mod = Y_con_mod.reshape(1,Y_con_mod.shape[0])
#model 2
X_dea_mod = np.array(ind.drop(labels="Deaths" ,axis = 1))
X_dea_mod = np.append(X_dea_mod,a,axis=1)
X_dea_mod = date_con(X_dea_mod)
X_dea_mod = np.delete(X_dea_mod,0,1)
Y_dea_mod = np.array(ind["Deaths"])
X_dea_mod = np.transpose(X_dea_mod)
Y_dea_mod = Y_dea_mod.reshape(1,Y_dea_mod.shape[0])

#model 3
X_rec_mod = np.array(ind.drop(labels="Recovered" , axis = 1))
X_rec_mod = np.append(X_rec_mod,a,axis=1)
X_rec_mod = date_con(X_rec_mod)
X_rec_mod = np.delete(X_rec_mod,0,1)
Y_rec_mod = np.array(ind["Recovered"])
X_rec_mod = np.transpose(X_rec_mod)
Y_rec_mod = Y_rec_mod.reshape(1,Y_rec_mod.shape[0])

def normalise(X_ori):
    i,j=X_ori.shape
    meanO=np.zeros((X_ori.shape[0],1))
    stanDev=np.zeros((X_ori.shape[0],1))
    for m in range(i):
        meanO[m][0]=X_ori[m].mean()
    X_ori = X_ori - meanO
    stanDev = np.sum(np.square(X_ori),axis=1)/X_ori.shape[1]
    for k in range(i):
        stanDev[k]=np.sqrt(stanDev[k])
    for o in range(i):
        X_ori[o]=(X_ori[o] - mean[o])/stanDev[o]
    return X_ori
def predict_count(X_ori,W,b):
    date = input ("enter the date in the form mm/dd/yyyy:")
    u=date
    n=int(u[0:2])
    m=int(u[3:5])
    x=int(u[6:10])
    X = np.zeros((3,1))
    X[0][0]=X_ori[0][-1] + X_ori[0][-1] - X_ori[0][-2]
    X[1][0]=X_ori[1][-1] + X_ori[1][-1] - X_ori[1][-2]
    X[2][0]=((x*365.25)+m+(n*30.4375))/1000000
    Y= np.dot(W,X) + b
    print("the predicted count is :", Y)

n_y=1
n_x=3
W1 = np.random.randn( n_y, n_x)*np.sqrt(2/3)
b1 = np.zeros(( n_y, 1))
m=73
learning_rate=0.0000055 ###0.0000055
cost=[]
for i in range(len(X_con_mod[0])):
    X_con_mod[0][i]=float(X_con_mod[0][i])

for i in range(1815): ###1815

    Z=np.dot(W1,X_con_mod)+ b1

    J = (1/m)*np.sum((Y_con_mod-Z)+(Y_con_mod-Z))
    print("cost after "+str(i)+" iterations :",J)
    cost.append(J)
    dZ=(-2/m)*(Y_con_mod-Z)
    dW = (1/m)*np.dot(dZ,np.transpose(X_con_mod))
    db = (1/m)*np.sum(dZ,axis=1,keepdims=True)
    
    W1 = W1 - learning_rate*dW
    b1 = b1 - learning_rate*db
plt.plot(range(1815),cost)  

Y_check  = np.dot(W1,X_con_mod)+ b1

Y = pd.DataFrame(np.transpose(Y_check))
X = pd.DataFrame(np.array(india["ObservationDate"]).reshape(india.shape[0],1))
Y_con = pd.DataFrame(np.array(Y_con_mod).reshape(india.shape[0],1))
###plot of the results

fig6 = plt.figure(figsize=(20,10))
ax6=plt.subplot2grid((1,1),(0,0))
ax6.grid(True)
ax6.plot(X[0],Y[0],color="blue",label="Predicted")
ax6.plot(X[0],Y_con[0],color="red",label="actual")
ax6.scatter(X[0],Y[0],color="blue")
ax6.scatter(X[0],Y_con[0],color="red")
for label6 in ax6.xaxis.get_ticklabels():
    label6.set_rotation(90)
    label6.set_color('#a19dd9')
for label6 in ax6.yaxis.get_ticklabels():
    label6.set_color('#a19dd9')

ax6.xaxis.label.set_color('#4c3ab0')
ax6.yaxis.label.set_color('#4c3ab0')
ax6.spines["left"].set_color('#4c3ab0')
ax6.spines["bottom"].set_color('#4c3ab0')
ax6.spines['right'].set_visible(False)
ax6.spines['top'].set_visible(False)
ax6.spines['left'].set_linewidth(2)
ax6.spines['bottom'].set_linewidth(2)
leg = ax5.legend()
leg.get_frame().set_alpha(0.8)
plt.xlabel("Dates",fontsize=20)
plt.ylabel("Cases",fontsize=20)
plt.legend()
plt.title("Predicting confirm cases in India",color='#4c3ab0',fontsize=25,fontstyle='normal')
fig6.savefig('indiapred.jpg')
plt.show()
