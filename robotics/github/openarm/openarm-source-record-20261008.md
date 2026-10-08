# OpenArm source record, 2026-10-08

## Owner fork

The owner's fork is `https://github.com/egc365/openarm`.

On 2026-10-08 the GitHub API for `repos/egc365/openarm` returned `fork` true and parent `enactic/openarm`. The page HTTP status is 200. The page title is `GitHub - egc365/openarm: A fully open-source humanoid arm for physical AI research and deployment in contact-rich environments. · GitHub`.

Compare `enactic:main...egc365:main` returned ahead 0, behind 10, status behind. The 10 commits are website dependency bumps, an in-hand camera note, FAQ entries, a cache change, and a Discord link change. Those commits do not add a STEP tree.

The root listing is the website repo. The folders are `.claude`, `.github`, and `website`. The files are `.editorconfig`, `.gitignore`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE`, and `README.md`. That root has no STEP tree and no STL tree.

`https://github.com/egc365/openarm_hardware` returns HTTP 404. The saved API response is `fork-status.txt` in this folder. A 404 does not say whether the name was never created, renamed, or deleted. The forks list for `enactic/openarm_hardware` has no repository owned by `egc365`. This URL is not the owner's fork. The page title is `Page not found · GitHub · GitHub`.

`https://github.com/enactic/openarm` is the parent of the fork. It is not the owner's fork.

`https://github.com/enactic/openarm_hardware` is the CAD location named by the fork README. It is not the owner's fork. Release tag `2.0.0`, name `OpenArm Hardware 2.0.0`, was published `2026-09-09T02:06:46Z`. The asset `openarm-hardware-2.0.0.tar.gz` is 163124751 bytes. The `.sha256` asset is 96 bytes. The `.sha512` asset is 160 bytes.

`egc365/openarm_description` does not resolve to a repository. That name was guessed. It is not a second fork.

## On-disk CAD

These two files exist:

- `/home/egc365/Documents/cannabis-sample-prep-cell/torso/build_openarm/openarm_orca.step`
- `/home/egc365/Documents/cannabis-sample-prep-cell/torso/openarm-bom/OpenArm 2.0 BOM-BOＭ.csv`

The STEP file is 577954123 bytes. sha256 `b2b5c751c709797d7bacc6f7bb0c128adab408a70c16278d4fa53e6af2fa7e0b`. Git rejects a file over 100 MB. This file was not uploaded. This record does not compare those bytes with `openarm-hardware-2.0.0.tar.gz`. The modular six-axis arm is not this OpenArm CAD.

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

Do not copy Anvil joint degrees or Anvil payload numbers into this table.

## Anvil wrist page

Anvil is a vendor documentation page. Anvil is not the owner's fork. `enactic/openarm` is not the owner's fork.

Page: `https://docs.anvil.bot/introduction/openarm-2.0`

Markdown twin fetched on 2026-10-08: `https://docs-origin.anvil.bot/introduction/openarm-2.0.md`

The screenshot footer says `Last updated 2 months ago`. The page does not print a calendar date.

The page says that with OpenARM 1.0, normal teleoperation wrist motions often hit joint limits because the human kinematic and the robot kinematic do not match. The arm and the elbow then made large corrective moves. The page calls that motion jerky.

The page says humans have a much larger range of motion in flexion and extension than in radial and ulnar deviation. The diagram labels are EXTENSION (+) in purple, FLEXION (-) in purple, RADIAL DEVIATION in green, and ULNAR DEVIATION in green. The diagram does not print degree numbers.

The page says OpenArm 1.0 used J6 for extension and flexion, and used J7 for radial and ulnar deviation. The page calls J7 the joint with the wider range. The page says OpenArm 2.0 swapped those joints so extension and flexion get the larger range. The page says the new J6 was updated to support a slightly wider radial and ulnar deviation range. The CAD callout on the Anvil wrist says `Extra range in J6`.

The drawing on the page shows this assignment:

- OpenArm 1.0: J6 is extension and flexion. J7 is radial and ulnar deviation.
- OpenArm 2.0, both the Standard wrist and the Anvil wrist: J6 is radial and ulnar deviation. J7 is extension and flexion.

The degree table is an image on the page. The markdown text does not print the numbers. The numbers below were read from the screenshots on 2026-10-08. The unit is degrees. The screenshot pages in this folder are `pictures/07-anvil-jerky-motion.png` through `pictures/13-anvil-cables.png`. The readable copy of the table is `pictures/05-anvil-range-table.png`. The reading of the table is `pictures/06-how-to-read-the-table.png`.

| Joint | Anvil OpenARM 1.0 | Standard OpenARM 2.0 | Anvil OpenARM 2.0 |
| --- | --- | --- | --- |
| J1 | -135 to +135 | -200 to +80 | -135 to +135 |
| J2 | -190 to +10 | -190 to +10 | -190 to +10 |
| J3 | -90 to +90 | -90 to +90 | -90 to +90 |
| J4 | 0 to 140 | 0 to 140 | 0 to 140 |
| J5 | -90 to +90 | -90 to +90 | -90 to +90 |
| J6 | -45 to +45 | -45 to +45 | -45 to +70 |
| J7 | -90 to +90 | -90 to +90 | -90 to +90 |
| Gripper | -45 to 0 | -45 to 0 | -45 to 0 |

The J6 cells for Standard OpenARM 2.0 and Anvil OpenARM 2.0 are boxed in red. The Anvil OpenARM 1.0 J6 cell is purple and is not in that red box. J7 is purple in all three columns.

How to read the table:

The swap is which joint does flexion. After the swap, flexion is J7 at -90 to +90. Before the swap, flexion was J6 at -45 to +45. That comparison uses the drawing and the table together. The J6 row by itself does not show a larger flexion number. Standard OpenARM 2.0 J6 stays -45 to +45.

Anvil OpenARM 2.0 J6 is -45 to +70. It is not -70 to +70. That cell is the page's slightly wider radial and ulnar range, and it matches the callout `Extra range in J6`.

J1 is not the same across columns. Standard OpenARM 2.0 J1 is -200 to +80. Both Anvil columns keep J1 at -135 to +135.

No degree on this page is a measured stop on the local STEP. The fork page `website/docs/hardware/openarm-2.0/general.mdx` says each joint has a mechanical limit. That sentence does not print this table. The fork page `website/docs/overview/whats-new-in-2.0.mdx` does not state this wrist swap. Both pages were read from the fork while it was 10 commits behind `enactic/openarm`.

The page names these tasks: fasten 4 zip ties in 1 min, disassemble complex Legos, easily align and insert cables, and pack raw eggs. The page says the gain is close-to-body work on both arms, with a well tuned IK solver.

The wiring photo labels are Original OpenARM, Anvil OpenARM 1.0, and Anvil OpenARM 2.0. The photo shows a loose red and black multi-wire cable, then a sleeved cable with a rectangular multi-pin plug, then a flat hard-case cable with a right-angle connector. The page prose says the design moved from LSCPCB cables to custom hard-case cables and added a harness, so motors stop dropping off the control bus during continuous data collection. The word LSCPCB is in that prose. It is not in the photo labels.

The closing lines say the change is small and mechanical, plus the cables. Anvil OpenARM 2.0 keeps OpenARM easy to build, modify, and repair, and the page says the wrist now moves the way a person does. Full specs point at the Anvil docs.

## Hardware-name paths

Four paths exist. The recommendation is A. B, C, and D were not done.

A. Use the fork that exists. Read `egc365/openarm`. Follow its README to `enactic/openarm_hardware` release 2.0.0 and to the hashed local STEP. Do not create a new repository.

B. Fork `enactic/openarm_hardware` into the `egc365` account and date that fork. Do not call the upstream repository the owner's fork before that fork exists.

C. Pull the 10 commits onto `egc365/openarm`. Those commits do not add STEP files.

D. Upload the local STEP as a GitHub release asset. A release asset must be under 2 GiB. Do not put the STEP in git.

## Tiny printed servo

The tiny printed-servo repository name is unknown. The owner said that repository was pushed on 2026-10-08. This record does not identify that repository. This record gives no dimensions for that servo. This record gives no 5 lb rating for that servo. This record gives no melt conclusion for that servo.

Search terms if the name stays missing: N20, micro metal gearmotor, printed servo, AS5600, Pololu 0J949.

## Gantry

`/home/egc365/Documents/cannabis-sample-prep-cell/.scratch/gantry-three-pairs-20261002` is already released. This goal did not modify it.
