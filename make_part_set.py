from functions import make_new_part_set


file_path = r"C:\Users\ved.thakare\OneDrive - University of Virginia\vanilla_blower_newdummy\atd-m350-d00.05_11_mas_mm_kg_ms.key"
new_file_path = r"C:\Users\ved.thakare\OneDrive - University of Virginia\vanilla_blower_newdummy\Dummy_partset.k"
sid = 2000

newfile_text = make_new_part_set(file_path, new_file_path, sid=sid, name='All_AB')

print(newfile_text)
