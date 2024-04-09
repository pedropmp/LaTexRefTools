import re
import tkinter as tk
from tkinter import filedialog
from time import sleep

counter = 0
def extract_refkeys(log_line):
    global counter
    regex = r"\\cite\{([ a-zA-Z0-9\,?]+ ?)\}"
    results = re.findall(regex, log_line)
    if len(results) == 0:
        return None
    # print(results)
    result = [r.split(',') for r in results]
    return result


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[('TeX files', '*.tex')])
unique_keys = []

if file_path:
    with open(file_path) as f:
        for line in f:
            refkeys = extract_refkeys(line)
            if refkeys:
                for ref in refkeys:
                    if isinstance(ref, list):
                        for r in ref:
                            if r not in unique_keys:
                                print(r)
                                unique_keys.append(r.replace(' ', ''))
                    else:
                        if ref not in unique_keys:
                            print(ref)
                            unique_keys.append(ref.replace(' ', ''))
unique_keys.sort()
for key in unique_keys:
    print(key)
print(len(unique_keys))
