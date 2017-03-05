import test_structure_file_table, pytest
from file_about import table 

def test_file_table():
    p = "D:/test_dir/"
    table1 = test_structure_file_table.file_table(p, 0)
    table2 = table(p, None)

    assert table1==table2
