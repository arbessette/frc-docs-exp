# Component indicators and Systemcore source review

Reviewed November 17, 2026. This records the sources checked and the changes
supported by them; it is not a hardware test or an exhaustive web inventory.

## Completed in FRC Docs

- Replaced PDP and PCM review placeholders with component diagnostic summaries.
  Named the CTRE manual revision/date and original PDP scope. Enabled/disabled
  communication patterns remain explicitly unverified with Systemcore software.
- Restored PDH diagnostic patterns for firmware 21.1.7 and later. REV still
  describes its green communication state using the previous controller, so
  that state is not presented as verified Systemcore behavior.
- Corrected the PH hardware-fault pattern to orange/cyan and the orange/green
  description to compressor overcurrent. Removed the unsupported orange/red
  entry and linked the current REV reference.
- Updated the 2027 overview's cable-kit information using FIRST's November 17
  announcement: complete Molex SL cable kits will not be in the Black Tote;
  Kitbot cables, including RSL/CAN adapters, and cable-making components remain
  included. The component kit excludes a crimper.

## Sources checked

- [CTRE PDP manual](https://ctre.download/files/user-manual/PDP%20User%27s%20Guide.pdf),
  revision 1.6, March 28, 2018, page 16. Downloaded and visually checked the LED
  table because the web text extraction omitted it.
- [CTRE PCM manual](https://ctre.download/files/user-manual/PCM%20User%27s%20Guide.pdf),
  revision 1.4, March 30, 2018, pages 12–15.
- [REV PDH indicators](https://docs.revrobotics.com/ion-control/pdh/status-led).
- [REV PH indicators](https://docs.revrobotics.com/ion-control/ph/status-led).
- [SystemcoreTesting](https://github.com/wpilibsuite/SystemcoreTesting), including
  beta power guidance and its linked controller specification.
- [Linked controller specification](https://downloads.limelightvision.io/documents/systemcore_specifications_june15_2025_alpha.pdf).
  It still labels the hardware alpha. Its connector, termination, I/O, and
  indicator details do not establish beta-and-later installation requirements.
- [FIRST November 17 availability update](https://www.firstinspires.org/community-blog/2026-systemcore-on-sale-date-update).

## Still open after this review

The reviewed sources did not establish beta-and-later Systemcore distribution
protection ratings, controller CAN termination, a complete radio installation,
signal-light wiring/behavior, or the full Smart I/O electrical specification.
The existing beta Micro-Fit power guidance and cable drawings remain useful,
but do not by themselves close those gaps. No alpha ratings were transferred
into beta instructions.

The component indicator summaries establish manufacturer definitions, not
Systemcore software compatibility or current-season eligibility. No WPILib
source files were changed in this review.
