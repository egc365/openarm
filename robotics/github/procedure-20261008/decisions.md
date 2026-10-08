# Decision board, 2026-10-08

The trail is `decisions.tsv` in this folder. One row is one decision.

## What is solved

The owner's fork is `https://github.com/egc365/openarm`. Parent is `enactic/openarm`. Ahead 0. Behind 10. The root is the website. It has no STEP tree.

`https://github.com/egc365/openarm_hardware` is a 404 because that repository was never created. It is not the fork.

The Anvil page `https://docs.anvil.bot/introduction/openarm-2.0` is a vendor page. It is not the fork. The degree table is filed with three named columns. The Damiao motor table was not changed.

The local STEP stays at its path and sha256. It was not put in git.

## Recommendation

Use path A.

A. Use the fork that exists. Read `egc365/openarm`. Follow its README to `enactic/openarm_hardware` release 2.0.0 and to the hashed local STEP. Do not create a new repository.

## The other three paths

B. Fork `enactic/openarm_hardware` into the `egc365` account and date that fork. Do not call the upstream repository the owner's fork before that fork exists.

C. Pull the 10 commits onto `egc365/openarm`. Those commits do not add STEP files.

D. Upload the 577954123 byte local STEP as a GitHub release asset. A release asset must be under 2 GiB. Do not put the STEP in git.

Four paths exist. Not three, and not five. B, C, and D were not done.

## Control

A later reader can evaluate this session with four checks.

1. The record names `egc365/openarm` as the fork of `enactic/openarm`.
2. The record says `egc365/openarm_hardware` was never created.
3. The wrist table names the column for each degree.
4. The STEP sha256 is on disk and the file is not in git.

This control is the check above. It is not a quotation from a Six Sigma handbook. The local handbook extraction was not quoted.

## Still open

The tiny printed-servo repository name is unknown. Search N20, micro metal gearmotor, printed servo, AS5600, and Pololu 0J949. Do not rate 5 lb. Do not claim melt.

The run2 shoulder is still `FAIL_UNIMPLEMENTED_SHOULDER_ONLY`. The engineering copy still says the clip is implemented. Those files were not edited. The five modular-arm choices are still unanswered.

Whether to do path B, C, or D is still the owner's choice. The recommendation remains A.

## Rationale

Stopping at the guessed hardware URL hid a fork that the API already names. The README in that fork already points at the upstream hardware release. Creating a second repository, pulling website bumps, or uploading the local STEP does not identify the fork.

## Block

The block was a wrong repository name, not a missing fork. The name is corrected in the source record. The hardware repository under `egc365` still does not exist. That remaining gap is path B, and it is not required to name the fork.
