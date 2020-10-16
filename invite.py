#!/usr/bin/env python3
import amino
import os
import getpass
def Tass2(data):
    listusers=[]
    for userId ,status in zip(data.userId,data.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers
def Tass(data):
    listusers=[]
    for userId ,status in zip(data.profile.userId,data.profile.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers
os.system('clear')
print("\033[1;32m ______                      __    __               ")
print("\033[1;32m|      \                    |  \  |  \              ")
print("\033[1;32m \$$$$$$ _______  __     __  \$$ _| $$_     ______  ")
print("\033[1;32m  | $$  |       \|  \   /  \|  \|   $$ \   /      \ ")
print("\033[1;32m  | $$  | $$$$$$$\\$$\ /  $$| $$ \$$$$$$  |  $$$$$$\ ")
print("\033[1;32m  | $$  | $$  | $$ \$$\  $$ | $$  | $$ __ | $$    $$")
print("\033[1;32m _| $$_ | $$  | $$  \$$ $$  | $$  | $$|  \| $$$$$$$$")
print("\033[1;32m|   $$ \| $$  | $$   \$$$   | $$   \$$  $$ \$$     \ ")
print("\033[1;32m \$$$$$$ \$$   \$$    \$     \$$    \$$$$   \$$$$$$$")
print("\033[1;32m                                                    ")
print("\033[1;32m                                                    ")
print("\033[1;31m                                                    ")
print("\033[1;31m __                   __                           ") 
print("\033[1;31m|  \                 |  \                         ")  
print("\033[1;31m| $$____    ______  _| $$_                         ") 
print("\033[1;31m| $$    \  /      \|   $$ \                       ")  
print("\033[1;31m| $$$$$$$\|  $$$$$$\\$$$$$$                      ")   
print("\033[1;31m| $$  | $$| $$  | $$ | $$ __                        ")
print("\033[1;31m| $$__/ $$| $$__/ $$ | $$|  \                     ")  
print("\033[1;31m| $$    $$ \$$    $$  \$$  $$                     ")  
print("\033[1;31m \$$$$$$$   \$$$$$$    \$$$$    \033[1;32m script by \033[1;36mkira_xc  ")  
print('\n\033[0m')              
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
    try:
        email=input("\033[1;93m# your email : \033[0m")
        password=getpass.getpass("\033[1;93m# your password : \033[0m")
        client.login(email=email,password=password)
        tst=True
    except:
        tst=False
        print("\033[1;93m# verify email or password\033[0m")
        exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")
        if exx=='n' or exx=='N' or exx=='no':
            os._exit(1)
            
tst=False
while tst==False:
    try:
        infoos=input("\033[1;93m#give me url of group : \033[0m")
        infoo=client.get_from_code(infoos)
        tst=True
        if infoo.objectType!=12:
            print ("\033[1;93m#not chat url !\033[0m")
            tst=False
    except:
        tst=False
        print("\033[1;93m# verify your url \033[0m")
    if tst==False:
        exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")
        if exx=='n' or exx=='N' or exx=='no':
            os._exit(1)
            
chatId=infoo.objectId
comId=infoo.path[1:infoo.path.index("/")]
sub_client=amino.SubClient(comId=comId,profile=client.profile)
swich=0
tst=False
while tst==False:
    try:
        tst=True
        
        swich=int(input("\033[1;93mchoose : \n\033[1;92m1 \033[1;93m- online members \n\033[1;92m2\033[1;93m - followers of user \n\033[1;92m3 \033[1;93m- new members \n\033[1;92mwhich one \033[1;93m: \033[0m"))
        if swich<0 or swich>3:
            print("\033[1;93mplease ... choose 1 or 2 or 3 \033[0m")
            tst=False
    except :
        print("\n\033[1;93mchoose a number\033[0m ")
        tst=False
tst=False
while tst==False:
    try:
        tst=True
        maxo=int(input("\n\033[1;93m# what maximum member ? : \033[0m"))   
    except:
        tst=False
        print("\033[1;93mno  .... \n type a number exmple :\033[1;92m 400 \033[0m")
    if tst==False:
        tobb=input("to be continue ? y/n : ")
        if tobb=="n" or tobb=="N":
            os._exit(1)
cpt=0
if swich==1:
    nemmm=0
    cpt=0
    while maxo>nemmm and len(sub_client.get_online_users(start=nemmm,size=25).profile.userId)!=0:
        lista=sub_client.get_online_users(start= nemmm,size= 25)
        
        for userId in Tass(lista):
            try:
                sub_client.invite_to_chat(userId=userId,chatId=chatId)
                cpt=cpt+1
                print(cpt , "\033[1;93m ) \033[1;92m- \033[1;93muser id\033[1;92m =\033[0m ",userId)
            except:
                ffffff=True
        nemmm=nemmm+25
elif swich==2:
    tst=False
    while tst==False:
      try:
         link=input("\033[1;93m# give me link of profile \033[1;92m: \033[0m")
         linko=client.get_from_code(link)
         tst=True
         if linko.objectType!=0:
             print (" \033[1;93mnot profile url !\033[0m")
             tst=False
         fchg=linko.path[1:infoo.path.index("/")]
         if fchg!=comId:
             tst=False
             print ("\033[1;93mis not profile of this community !\033[0m")
      except:
          tst=False
          print("\033[1;93m# verify your url \033[0m")
          
      if tst==False:
          exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")
          if exx=='n' or exx=='N' or exx=='no':
              os._exit(1)
    userIdf=linko.objectId
    nemmm=0
    cpt=0
    while maxo>nemmm and len(sub_client.get_user_followers(userId=userIdf,start=nemmm,size=25).userId)!=0:
        listf=sub_client.get_user_followers(userId=userIdf,start= nemmm,size= 25)
        
        for userId in Tass2(listf):
            try:
                sub_client.invite_to_chat(userId=userId, chatId=chatId)
                cpt=cpt+1
                print(cpt , "\033[1;93m ) \033[1;92m- \033[1;93muser id \033[1;92m= \033[0m",userId)
            except:
                ffffff=True
        nemmm=nemmm+25
elif swich==3:
    nemmm=0
    cpt=0
    while maxo>nemmm and len(sub_client.get_all_users(start=nemmm,size=25).profile.userId)!=0:
        listn=sub_client.get_all_users(start=0,size=25)
        
        for userId in Tass(listn):
            try:
                sub_client.invite_to_chat(userId=userId,chatId=chatId)
                cpt=cpt+1
                print(cpt , "\033[1;93m ) \033[1;92m-\033[1;93m user id \033[1;92m= \033[0m",userId)
            except:
                ffffff=True
                
        nemmm=nemmm+25
    
print("\033[1;92mall done !\033[0m")
    
os._exit(1)