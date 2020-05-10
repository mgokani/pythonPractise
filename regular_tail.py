'''
implement tail

tail <filename> prints only the last 10 lines of the File
tail -n 20 <filename> reads last 20 lines from filename and writes to stdout 
tail -f <filename> prints the last 10 lines and doesn't exit. It keeps reading lines as they are written to the file.
'''

count = 20

with open('file1.txt', 'r') as f:
  f_contents = f.readlines()
  
total_len = len(f_contents)

for i in range(total_len - count, total_len):
  print(f_contents[i].strip())
