import os
import shutil

queue_dir = '.queue/'
for file in os.listdir(queue_dir):
    punct = r'.-/~,{}[];:'
    filename = "".join(["".join([f for f in fpart if f not in punct])+" " for fpart in file[:file.index('pdf')-1].lower().split()[:4]]).strip()
    if not os.path.isdir(filename): os.mkdir(filename)
    src = '{}{}'.format(queue_dir, file)
    dest = '{}/'.format(filename)
    if not os.path.exists('.{}/{}'.format(filename, file)): shutil.copy(src, dest)
    os.remove('{}{}'.format(queue_dir, file))