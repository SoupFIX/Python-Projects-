from colorama import Fore,init,Back,Style
import os
import pandas as pd
#pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns',None)
init(autoreset=True)
count=0
print(Fore.WHITE+Style.BRIGHT+"--------------------------------------------------------------------------------------------------------------------------\n\n\n\n")
#analyzer function
def analyse(path):
    global count
    for root,direc,files in os.walk(path):
        print(Fore.RED + Style.BRIGHT+ f"Main Folder : {root}")
        print(Fore.BLUE + Style.BRIGHT+ f"Sub Folder(directory) : {direc}")
        print(Fore.GREEN + Style.BRIGHT+ f"Files : {files}","\n")
        print(Fore.WHITE+Style.BRIGHT+"------------------------------------------------------------------------------------------------------------------\n\n\n\n")
        count+=1
        for i in files:
            #for csv files
            if i.endswith('.csv'):
                d1 = pd.read_csv(i)
                d1.fillna(0)
                desc = d1.describe()
                inf = d1.info()
                hd = d1.head()
                print(Fore.GREEN + Style.BRIGHT + f"FILE NAME : {i}\n",Fore.YELLOW + Style.BRIGHT + f"{i}\n\n {d1}","\n")
                print(Fore.GREEN + Style.BRIGHT + f"DESCRIPTION OF : {i}\n {desc}")
                print(Fore.CYAN + Style.BRIGHT + f"\n HEADERS : \n\n {hd}")
                print(Fore.RED + Style.BRIGHT + f"INFO OF {i} : \n {inf}")
                print("----------------------------------------------------------------------------------------------------------------------------------\n\n\n\n")
            # for excel files
            if i.endswith('.xlsx') | i.endswith('.slx'):
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
                d2 = pd.read_excel(i)
                d2.fillna(0)
                desc = d2.describe()
                hd = d2.head()
                inf = d2.info()
                print(Fore.GREEN + Style.BRIGHT + f"FILE NAME : {i}\n",Fore.YELLOW + Style.BRIGHT + f"\n\n\t {d2}","\n")
                print(Fore.GREEN + Style.BRIGHT + f"DESCRIPTION OF : {i}\n {desc}")
                print(Fore.CYAN + Style.BRIGHT + f"\n HEADERS : \n\n {hd}")
                print(Fore.RED + Style.BRIGHT + f"INFO OF {i} : \n {inf}")
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
            # for json files
            if i.endswith('.json'):
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
                d3 = pd.read_json(i)
                d3.fillna(0)
                desc = d3.describe()
                hd = d3.head()
                inf = d3.info()
                print(Fore.GREEN + Style.BRIGHT + f"FILE NAME : {i}\n" , Fore.YELLOW + Style.BRIGHT + f"\n\n\t {d3}" , "\n")
                print(Fore.GREEN + Style.BRIGHT + f"DESCRIPTION OF : {i}\n {desc}")
                print(Fore.CYAN + Style.BRIGHT + f"\n HEADERS : \n\n {hd}")
                print(Fore.RED + Style.BRIGHT + f"INFO OF {i} : \n {inf}")
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
            # for html
            if i.endswith('.html'):
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
                d3 = pd.read_html(i)
                d3.fillna(0)
                desc = d3.describe()
                hd = d3.head()
                inf = d3.info()
                print(Fore.GREEN + Style.BRIGHT + f"FILE NAME : {i}\n" , Fore.YELLOW + Style.BRIGHT + f"\n\n\t {d3}" , "\n")
                print(Fore.GREEN + Style.BRIGHT + f"DESCRIPTION OF : {i}\n {desc}")
                print(Fore.CYAN + Style.BRIGHT + f"\n HEADERS : \n\n {hd}")
                print(Fore.RED + Style.BRIGHT + f"INFO OF {i} : \n {inf}")
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
            #for text files
            if i.endswith('.txt'):
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
                d4 = pd.read_csv(i)
                desc = d4.describe()
                hd = d4.head()
                inf = d4.info()
                d4.fillna(0)
                print(Fore.GREEN + Style.BRIGHT + f"FILE NAME : {i}\n",Fore.YELLOW + Style.BRIGHT+f"\n\n {d4}","\n")
                print(Fore.GREEN + Style.BRIGHT + f"DESCRIPTION OF : {i}\n {desc}")
                print(Fore.CYAN + Style.BRIGHT + f"\n HEADERS : \n\n {hd}")
                print(Fore.RED + Style.BRIGHT + f"INFO OF {i} : \n {inf}")
                print(Fore.WHITE+Style.BRIGHT+"----------------------------------------------------------------------------------------------------------\n\n\n\n")
    print("The totalnumber of files and folder are : ",count)
print(Fore.CYAN + Style.BRIGHT + "\t\t\t\t\tWELCOME TO THE AUTOMATIC FILES GENERATOR AND READER!\t\t\t\t\t")
#input the path
pth = input(Fore.GREEN+Style.BRIGHT+"Enter the folder path in which all your files are present for analysis ")
#function call
analyse(pth)
        

        