# Neural RGBD
PyTorch implementation of [Neural RGB-D Surface Reconstruction](https://dazinovic.github.io/neural-rgbd-surface-reconstruction/static/pdf/neural_rgbd_surface_reconstruction.pdf), 

## Setup

```
pip install -r requirements.txt
```

Install Marching cube algo

```
pip install --upgrade PyMCubes
```
  ## Dataset

ScanNet: Attached in submission files.
The ICL data(not used in demo): [webpage](https://www.doc.ic.ac.uk/~ahanda/VaFRIC/iclnuim.html)

## Run

```
runner.bat
or
python optimize.py --config configs/<scene_config_name>
```

Output would be stored in logs/\*/\*.ply
