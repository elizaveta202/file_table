import sys, os, HTML, argparse, re

def table(path_, exc):
    
    main_table = []

    for root, dirs, files in os.walk(path_):
        for name in files:
            fullname = name.split(".")
            path = os.path.join(root, name)
            size = os.path.getsize(os.path.join(root, name))

            if exc and not re.search(exc, name) or not exc:
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

    
parser = argparse.ArgumentParser()
parser.add_argument("dir", help = "create html-table with information about the files in target directory")
parser.add_argument("--exclude", action="store", help="exclude files with pointed directory")
args = parser.parse_args()

if args.exclude:
    table(args.dir, args.exclude)
    
else:
    print (args.exclude)
    table(args.dir, args.exclude)


