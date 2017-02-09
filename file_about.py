import sys, os, HTML

main_table = []

path_ = sys.argv[1]
                    
for filename in os.listdir(path_):
    
    path = path_+"\\"+filename
    #print ("fullpath " +path)
    size = os.path.getsize(path)
    
    fullname = os.path.basename(path)
    fullname = fullname.split(".")
    
    file_inf = []
    file_inf.append(fullname[0])
    file_inf.append(fullname[1])
    file_inf.append(size)
    file_inf.append(path)


    main_table.append(file_inf)



htmlcode = str(HTML.table(main_table,header_row=['Name',   'Extension',   'Size (Bytes)', 'Path']))


f = open("file's table.htm", "w")

for i in htmlcode:
    f.write(i)
f.close()
    
print ("The table has been created. You can find it in the same directory as this script.")

    

