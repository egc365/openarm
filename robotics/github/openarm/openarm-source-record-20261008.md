# OpenArm source record, 2026-10-08

## Owner fork

`https://github.com/egc365/openarm` opens. HTTP status is 200. The page title is `GitHub - egc365/openarm: A fully open-source humanoid arm for physical AI research and deployment in contact-rich environments. · GitHub`.

The root listing is the website repo. The folders are `.claude`, `.github`, and `website`. The files are `.editorconfig`, `.gitignore`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE`, and `README.md`. That root has no STEP tree and no STL tree.

`https://github.com/egc365/openarm_hardware` is a 404. HTTP status is 404. The page title is `Page not found · GitHub · GitHub`.

`https://github.com/enactic/openarm` is not the owner's fork. `https://github.com/enactic/openarm_hardware` is not the owner's fork. The README in `egc365/openarm` names `https://github.com/enactic/openarm_hardware` as the upstream CAD location. That upstream URL is not the owner's fork.

## On-disk CAD

These two files exist:

- `/home/egc365/Documents/cannabis-sample-prep-cell/torso/build_openarm/openarm_orca.step`
- `/home/egc365/Documents/cannabis-sample-prep-cell/torso/openarm-bom/OpenArm 2.0 BOM-BOＭ.csv`

The modular six-axis arm is not this OpenArm CAD.

## Published OpenArm motors

Source: `https://huggingface.co/docs/lerobot/en/openarm`. This is the only servo list in this record.

CAN FD nominal bitrate is 1 Mbps. CAN FD data bitrate is 5 Mbps. Payload is 6.0 kg peak and 4.1 kg nominal.

| Joint | Motor | Send CAN ID | Recv CAN ID |
| --- | --- | --- | --- |
| joint_1 | DM8009 | 0x01 | 0x11 |
| joint_2 | DM8009 | 0x02 | 0x12 |
| joint_3 | DM4340 | 0x03 | 0x13 |
| joint_4 | DM4340 | 0x04 | 0x14 |
| joint_5 | DM4310 | 0x05 | 0x15 |
| joint_6 | DM4310 | 0x06 | 0x16 |
| joint_7 | DM4310 | 0x07 | 0x17 |
| gripper | DM4310 | 0x08 | 0x18 |

## Tiny printed servo

The tiny printed-servo repository name is unknown. The owner said that repository was pushed on 2026-10-08. This record does not identify that repository. This record gives no dimensions for that servo. This record gives no 5 lb rating for that servo. This record gives no melt conclusion for that servo.

## Gantry

`/home/egc365/Documents/cannabis-sample-prep-cell/.scratch/gantry-three-pairs-20261002` is already released. This goal did not modify it.
