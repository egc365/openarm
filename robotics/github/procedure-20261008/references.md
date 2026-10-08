# References

Textbook survey first. The local extractions of *The ASQ Certified Six Sigma Black Belt Handbook* and *The Lean Six Sigma Black Belt Handbook* are in the corpus as historical-working, owner-unaccepted editions. `corpus_search` refused the ASQ edition with HTTP 400 because verified retrieval inputs are not complete. No sentence in this folder is a quotation from those books.

Training knowledge, kept separate from the sources below. I already knew the five DMAIC names before this search. That memory is not a page citation. The wording used for decisions comes from the ASQ page that was opened.

More training knowledge, still not a citation. I already knew the names flexion, extension, radial deviation, and ulnar deviation. I did not know which OpenArm joint Anvil assigns to each motion, and I did not know the degree table. Those facts come from the Anvil page below.

## Sources opened this turn

American Society for Quality. (n.d.-a). *DMAIC*. https://asq.org/quality-resources/dmaic

American Society for Quality. (n.d.-b). *Six Sigma*. https://asq.org/quality-resources/six-sigma

GitHub. (n.d.). *About releases*. GitHub Docs. https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases

The same page was opened again on 2026-10-08. It says each file included in a release must be under 2 GiB. That sentence is the limit used for path D. The local STEP is 577954123 bytes, which is under 2 GiB. The file was not uploaded.

Pololu Corporation. (2024, April 3). *Micro metal gearmotors with carbon brushes (HPCB), no encoder* [Drawing 0J949]. https://www.pololu.com/file/0j949/micro-metal-gearmotor-dimensions.pdf

CaptainObvious. (2019, December 8). *N20 geared motor continuous rotation servo with AS5600 magnetic sensor*. Thingiverse. https://www.thingiverse.com/thing:4030416

Revolio_ClockbergJr. (2023, December 21). Comment on "Why are the gears on this SG90 servo not moving?" *Reddit*. https://www.reddit.com/r/arduino/comments/18nxluq/why_are_the_gears_on_this_sg90_servo_not_moving/

NZRVA. (2023, January 3). Comment on "My first and second attempt at a gear train." *Reddit*. https://www.reddit.com/r/3Dprinting/comments/102mk1y/my_first_and_second_attempt_at_a_gear_train/

IvorTheEngine. (2023, January 3). My first and second attempt at a gear train. Broken teeth and melted gears. *Reddit*. https://www.reddit.com/r/3Dprinting/comments/102mk1y/my_first_and_second_attempt_at_a_gear_train/

## Data read this turn, not a publication

`gh repo list egc365` on 2026-10-08. No repository name or description matched servo, joy, or a printed actuator. `print-cell-1m` was created 2026-10-08 and is a printer park.

`curl` on 2026-10-08. `https://github.com/egc365/openarm` returned HTTP 200. `https://github.com/egc365/openarm_hardware` returned HTTP 404.

`run2/cad/motion-contract.json` field `positive_clip` is `FAIL_UNIMPLEMENTED_SHOULDER_ONLY`.

`engineering/cad/modular-six-axis/motion-contract.json` field `positive_clip` is `IMPLEMENTED_POSITIVE_SHOULDER_CLIP`.

OpenArm STEP size 577,954,123 bytes. sha256 `b2b5c751c709797d7bacc6f7bb0c128adab408a70c16278d4fa53e6af2fa7e0b`.

Gantry directory time 2026-10-02 09:22:49 -0400. Unchanged.

## Sources opened for the fork correction

Anvil. (n.d.). *OpenARM 2.0*. https://docs.anvil.bot/introduction/openarm-2.0

The markdown twin of that page was fetched on 2026-10-08 from https://docs-origin.anvil.bot/introduction/openarm-2.0.md. The degree table is an image. The numbers in the source record were read from the screenshots, not from the markdown text. The screenshot footer says "Last updated 2 months ago". The page does not print a calendar date. The word LSCPCB is in the markdown prose about cables. It is not in the photo labels.

GitHub API on 2026-10-08. `repos/egc365/openarm` returned fork true and parent `enactic/openarm`. Compare `enactic:main...egc365:main` returned ahead 0, behind 10, status behind. `repos/egc365/openarm_hardware` returned HTTP 404. `repos/enactic/openarm_hardware/releases/tags/2.0.0` returned tag 2.0.0, published 2026-09-09T02:06:46Z, asset `openarm-hardware-2.0.0.tar.gz` of 163124751 bytes.

The fork file `website/docs/hardware/openarm-2.0/general.mdx` says each joint has a mechanical limit. That sentence does not print the Anvil degree table. The fork file `website/docs/overview/whats-new-in-2.0.mdx` does not state the wrist swap. Both files were read while the fork was 10 commits behind `enactic/openarm`. The 10 commit subjects are website dependency bumps, an in-hand camera note, FAQ entries, a cache change, and a Discord link change.
