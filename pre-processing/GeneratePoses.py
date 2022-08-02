# for fname in range(9999):
#     with open(f'posi{fname}.txt', 'w') as outfile:
#             with open(f'{fname}.txt') as infile:
#                 outfile.write(infile.read())
T0 = [[ 1., 0., 0., 0.],[ 0., 0., 1., 0.],[ 0., -1., 0., 0.],[ 0., 0., 0., 1.]]
T1 = [[ 1., 0., 0., 0.],[ 0., -1., 0., 0.],[ 0., 0., -1., 0.],[ 0., 0., 0., 1.]]
from numpy import loadtxt
from yaml import load
result = ''
def readPose(i):
    lines = loadtxt(f'{i}.txt', comments="#", delimiter=" ", unpack=False)
    return lines
for i in range(9999):
    try:
        data = readPose(i)
        data = T0@data@T1
        data = str(data).replace('[','').replace(']','')
        with open(f'posi{i}.txt', 'w') as out:
            out.write(data)
        data = ''
        with open(f'posi{i}.txt', 'r') as lines:
            for line in lines:
                data += line.strip()+'\n'
        result += data
    except:
        break
with open(f'trainval_poses.txt', 'w') as out:
    out.write(result)