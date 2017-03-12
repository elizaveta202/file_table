import HTML, argparse, re


from pathlib import Path

main_table = []

def iter_dir (target_dir, exc):

    for x in target_dir.iterdir():
        if not x.is_dir():
			
            if exc and not re.search(exc, x.name) or not exc:
                file_inf = []

                file_inf.append(x.stem)
                file_inf.append(x.suffix)
                file_inf.append(x.stat().st_size)
                file_inf.append(target_dir/x.name)
    

                main_table.append(file_inf)
        else:
            iter_dir(x,exc)

def table(path_, exc):
    
    target_dir = Path(path_)
    iter_dir (target_dir, exc)
    
    htmlcode = str(HTML.table(main_table,header_row=['Name',   'Extension',   'Size (Bytes)', 'Path']))
    f = open("file's table.htm", "w")

    for i in htmlcode:
        f.write(i)
    f.close()
    
    print ("The table has been created. You can find it in the same directory as this script.")

    return main_table

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help = "create html-table with information about the files in target directory")
    parser.add_argument("--exclude", action="store", help="exclude files with pointed pattern")
    args = parser.parse_args()

    table(args.dir, args.exclude)


