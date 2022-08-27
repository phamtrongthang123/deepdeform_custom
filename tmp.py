from pathlib import Path 
import os 
import sys 
root = Path('unzip_root')
seq = 'seq003'
path = root/seq
count_max = 0 
for pi in path.glob("*"):
    if not os.path.isdir(str(pi)):
        continue 
    count_max+=1
segment = list(range(100, count_max, 100))
frameids = list(range(0, count_max, 50))

for pi in path.glob("*"):
    if not os.path.isdir(str(pi)):
        continue 
    frameid = int(str(pi.name).split('_')[1]) -1 
    if frameid not in frameids:
        continue 
    segs = [x for x in segment if x >= frameid]
    obs = pi/'observation.ply'
    for seg in segs:
        saved_path = root/f'{seq}_{seg}_{str(frameid).zfill(6)}.ply'
        print(f'cp {obs} {saved_path}')
        os.system(f"cp {obs} {saved_path}")