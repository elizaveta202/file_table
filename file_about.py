import os, HTML

main_table = []

for filename in os.listdir("D:\\file_table\\file_table"):
    info = os.stat(filename)
    size = info.st_size
    path = os.path.realpath(filename)
    fullname = os.path.basename(path)
    fullname = fullname.split(".")
    file_inf = []
    file_inf.append(fullname[0])
    file_inf.append(fullname[1])
    file_inf.append(size)
    file_inf.append(path)


    main_table.append(file_inf)

print (main_table)

htmlcode = HTML.table(main_table)
print (htmlcode)
