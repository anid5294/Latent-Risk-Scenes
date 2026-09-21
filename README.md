# LIBERO Latent Risk Scenes

An internal scene pack containing eleven custom BDDL tasks for LIBERO. The
scenes are designed to evaluate latent risk: situations where individual
actions are ordinary, but their combination creates an undesirable or unsafe
outcome. The repository includes the scene definitions, a small installer, and
a script for checking that an installed scene loads correctly.

## Setup

Install the tested LIBERO revision in a Python 3.8 environment:

```bash
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
git checkout 8f1084e3132a39270c3a13ebe37270a43ece2a01

conda create -n libero python=3.8.13 -y
conda activate libero
python -m pip install -r requirements.txt
python -m pip install -e .
```

Install this scene pack into the LIBERO checkout:

```bash
cd /path/to/latent-risk-scenes-packaged
./install.sh /path/to/LIBERO
```

The scenes are copied to
`LIBERO/libero/libero/bddl_files/libero_risk/`.

## Run a scene

From this repository, verify that the default scene initializes correctly:

```bash
conda activate libero
python scripts/run_scene.py --libero-root /path/to/LIBERO
```

Run a specific scene:

```bash
python scripts/run_scene.py \
  --libero-root /path/to/LIBERO \
  --scene KITCHEN_SCENE4_put_the_wine_bottle_in_front_of_the_middle_drawer_and_open_it.bddl
```

Available filenames are listed in [`scenes/`](scenes/).

## Teleoperate and collect demonstrations

Run LIBERO's keyboard collector from the LIBERO checkout:

```bash
cd /path/to/LIBERO
conda activate libero

PYTHONPATH=. python scripts/collect_demonstration.py \
  --device keyboard \
  --robots Panda \
  --num-demonstration 10 \
  --directory demonstration_data/latent_risk \
  --bddl-file libero/libero/bddl_files/libero_risk/KITCHEN_SCENE4_put_the_wine_bottle_in_front_of_the_middle_drawer_and_open_it.bddl
```

The collector writes a raw `demo.hdf5` beneath the selected output directory.

## Generate a LIBERO-format dataset

Locate the collected file:

```bash
find demonstration_data/latent_risk -name demo.hdf5
```

Convert it with LIBERO's dataset generator:

```bash
PYTHONPATH=. python scripts/create_dataset.py \
  --demo-file /path/to/demo.hdf5 \
  --use-camera-obs
```

The converted dataset is written under
`LIBERO/libero/datasets/libero_risk/`.

## Attribution

This scene pack uses LIBERO's environments, assets, BDDL format, teleoperation
tools, and dataset pipeline.

```bibtex
@article{liu2023libero,
  title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
  journal={arXiv preprint arXiv:2306.03310},
  year={2023}
}
```
