import os

folders = [folder for folder in os.listdir('.') if folder[0] != '.']
amt = len(folders)
n = 4
qrtr = amt // n
# print('chunk size:', qrtr)
remainder = amt % n
if remainder > 20: raise Exception

chunks = []
for f in range(n): chunks.append(folders[qrtr*f:qrtr*(f+1)])
chunks.append(folders[qrtr*4:])

for i,chunk in enumerate(chunks):
    for ln in chunk:
        print(ln)
        os.system('git add "{}"'.format(ln))
    os.system('git commit -m "chunk #{}, updating the following: {}'.format(i,chunk))
    os.system('git push')
    inp = input('Continue? Y/N ').strip().split()[0].lower()
    if inp == 'n': break

