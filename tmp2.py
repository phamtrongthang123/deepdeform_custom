import pymeshlab as ml
from pathlib import Path 
import os 
import multiprocessing as mp 
from multiprocessing import Pool 

with open('log.txt', 'w') as f: 
    pass 
root = Path('./unzip_root')
saved_root = Path('./unzip_root_s')
os.makedirs(saved_root, exist_ok=True)

def proc_run(posixpath):
    ms = ml.MeshSet()
    ms.load_new_mesh(str(posixpath))
    m = ms.current_mesh()
    print('input mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')

    #Target number of vertex
    TARGET=55000

    #Estimate number of faces to have 100+10000 vertex using Euler
    numFaces = 100 + 2*TARGET

    #Simplify the mesh. Only first simplification will be agressive
    while (ms.current_mesh().vertex_number() > TARGET):
        ms.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=numFaces, preservenormal=True)
        print("Decimated to", numFaces, "faces mesh has", ms.current_mesh().vertex_number(), "vertex")
        #Refine our estimation to slowly converge to TARGET vertex number
        numFaces = numFaces - (ms.current_mesh().vertex_number() - TARGET)

    m = ms.current_mesh()
    print('output mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')
    # ms.apply_filter('point_cloud_simplification',samplenum=10000)
    # ms.apply_filter('compute_normals_for_point_sets')
    # ms.apply_filter('surface_reconstruction_ball_pivoting')
    # ms.apply_filter('parametrization_trivial_per_triangle',textdim=2048)
    # ms.save_current_mesh('third.obj')
    ms.save_current_mesh(str(saved_root/posixpath.name))
    # break
    with open('log.txt', 'a') as f:
        f.write(f'{posixpath} - {m.vertex_number()} vertices - {m.face_number()} faces\n')
allp = sorted(list(root.glob("*.ply")))
p = Pool()
p.map(proc_run, allp)
    