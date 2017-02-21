import sys, os, HTML, argparse, re
from path import Path

def table(path_, exc):
    
    main_table = []

    target_dir = Path(path_)
    

    for f in target_dir.walkfiles():
    	fname = f.basename()
  
    	ext = fname.split(".")[-1]
    	fname = fname.split(".")[0:-1]
    	name ="".join(fname)
    	
    	size = f.getsize()
    	path = os.path.join(path_, f.basename())
    	

    	if exc and not re.search(exc, name) or not exc:
                file_inf = []
            
                file_inf.append(name)
                file_inf.append(ext)
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
parser.add_argument("--exclude", action="store", help="exclude files with pointed pattern")
args = parser.parse_args()

table(args.dir, args.exclude)


