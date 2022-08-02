from pymeshfix import _meshfix
tin = _meshfix.PyTMesh()
tin.LoadFile('mesh_002000.ply')
tin.clean(max_iters=10, inner_loops=3)
tin.save_file('cleanned.ply')
