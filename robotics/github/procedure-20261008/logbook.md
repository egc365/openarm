# Logbook, 2026-10-08

The autoresearch master card, the debug graph, and the Spinellis, Zeller, and Agans note are missing. Each path is a broken link under `/wiki/outputs/`. This log uses the skill text that is still on disk. It does not invent the missing cards.

## Statement of the problem

Three checks block a build. The tiny printed-servo repository has no name. The run2 shoulder is a pad, while the engineering copy says the clip is implemented. `egc365/openarm_hardware` returns HTTP 404, and the local STEP is too large for a git file.

## Hypotheses and falsifiers

1. A repository under `egc365` created on 2026-10-08 is the tiny servo. Falsifier: `gh repo list` returns a name or description that says servo, joy, or printed actuator. Result: no such repository. `print-cell-1m` is a printer park. The hypothesis fails.
2. The hardware URL now opens. Falsifier: HTTP status is 200. Result: HTTP 404. The hypothesis fails.
3. The run2 contract now says the clip is implemented. Falsifier: `positive_clip` is not `FAIL_UNIMPLEMENTED_SHOULDER_ONLY`. Result: the string is still `FAIL_UNIMPLEMENTED_SHOULDER_ONLY`. The hypothesis fails.
4. The engineering copy agrees with run2. Falsifier: its `positive_clip` matches run2. Result: the engineering file says `IMPLEMENTED_POSITIVE_SHOULDER_CLIP`. The files disagree.

## Prediction

Another name search will not create a rating. A rename of the pad will not create a lock.

## Experiment

The account list, both HTTP checks, both contract strings, and the gantry directory time were read again on this turn. The gantry time is still 2026-10-02 09:22:49 -0400. The directory was not modified.

## Observed results

The search problem is closed. The name is not in the `egc365` account. The clip and the 404 remain human gates. No CAD file was edited.

## Conclusions

Do not rate the servo. Do not call the pad a lock. Do not upload the 578 MB STEP into git. The control record is this folder.

## Correction, same day

The hardware URL is still HTTP 404. That sentence was used as if the owner had no fork. That reading is wrong.

`egc365/openarm` is a fork. The API returned fork true and parent `enactic/openarm`. Compare returned ahead 0 and behind 10. The 10 commits do not add STEP files.

`egc365/openarm_hardware` was never created. It is not the fork. `enactic/openarm_hardware` release 2.0.0 remains upstream CAD. It is not the owner's fork.

The Anvil wrist page was filed from the screenshots and from the markdown twin. Anvil is not the fork. The Damiao motor table was not changed.

The gantry directory time is still 2026-10-02 09:22:49 -0400. The directory was not modified.
