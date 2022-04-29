import os

num_chunks = 4

folders = [folder for folder in os.listdir('.') if folder[0] != '.']
qrtr = len(folders) // num_chunks
if qrtr > 20: raise Exception

chunks = []
for f in range(num_chunks): chunks.append(folders[qrtr*f:qrtr*(f+1)])
chunks.append(folders[qrtr*4:])

for i,chunk in enumerate(chunks):
    for ln in chunk:
        os.system('git add "{}"'.format(ln))
    os.system('git commit -m "chunk #{}, updating the following: {}'.format(i,chunk))
    os.system('git push origin master')
    inp = input('Continue? Y/N ').strip()[0].lower()
    if inp == 'n': break

