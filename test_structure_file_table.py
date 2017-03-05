import os, random
from pathlib import Path

main_table = []

def file_table(new_path, lvl):
    
    if not os.path.exists(new_path):    
        os.makedirs(new_path)
        p = random.randint(1,10)
        i = 0
        while i < p:
            
            f = open (new_path+str(i)+".txt","w")
            l = "w" * random.randint(10,500)
            for index in l:
                f.write(index + '\n')
            f.close()
            
            list_inf = []
            list_inf.append(str(i))
            list_inf.append(".txt")
            list_inf.append(os.path.getsize(new_path+str(i)+".txt"))
            list_inf.append(new_path+str(i)+".txt")
            main_table.append(list_inf)
            
            i+=1
            
        if lvl < 4:
            file_table(new_path+"subdir/", lvl+1)

    return main_table
    
if __name__=="__main__":
    new_path = "D:/test_dir/"
    file_table(new_path, 0)
    print (main_table)
