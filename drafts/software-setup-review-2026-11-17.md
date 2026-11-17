# WPILib setup and first-drive review — November 17, 2026

Reviewed the sibling WPILib checkout's environment setup, installer, offline
preparation, Python setup, Driver Station installation, controller imaging,
configuration, and first-drive entry pages against official release sources.

## Corrections applied in WPILib Docs

- Replaced the 2025 installer card and ambiguous latest-stable link with the
  reviewed 2027 Alpha 8 release and explicit newer-release selection guidance.
- Matched the setup overview's macOS minimum to the Alpha 8 requirement (15+).
- Removed the overview's claim that macOS/Linux cannot image Systemcore; the
  documented web-update workflow and Hardware Manager downloads cover them.
- Linked compatibility checks for WPILib, OS images, Driver Station, and vendor
  libraries before updating and before the first deployment.
- Changed RobotPy installation commands to allow 2027 prereleases while
  excluding earlier-season packages. Project version selection still needs
  to match the installed software and the testing instructions.
- Replaced the blanket claim that Systemcore only provides Python 3.14 with
  release-specific runtime guidance. The OS history explicitly records a
  Python 3.13 transition; it does not establish 3.14 for every supported image.
- Corrected offline installer selection, linked versioned documentation
  downloads, and added OS/Driver Station/Python preparation requirements.
- Clarified prerelease FMS compatibility: confirm the combination with the
  event. The Driver Station README and Alpha 7/8 release notes differ in scope.
- Removed alpha-derived LED acceptance criteria from the configuration checklist.
- Updated first-power-on Wi-Fi defaults for image 17+ (per-unit SSID/password).

## Sources

- [WPILib Alpha 8](https://github.com/wpilibsuite/allwpilib/releases/tag/v2027.0.0-alpha-8)
- [Systemcore compatibility tables](https://github.com/wpilibsuite/SystemcoreTesting#software-compatibility)
- [Driver Station releases](https://github.com/wpilibsuite/FirstDriverStation-Public/releases)
- [Driver Station installation notes](https://github.com/wpilibsuite/FirstDriverStation-Public)
- [Systemcore OS history](https://github.com/LimelightVision/systemcore-os-public)
- [RobotPy testing instructions](https://github.com/wpilibsuite/SystemcoreTesting/blob/main/robotpy.md)
- [REV testing notes](https://github.com/wpilibsuite/SystemcoreTesting/blob/main/REV.md)

## Remaining validation

- Screenshots have not been recaptured or certified current.
- No installer, OS update, robot deployment, or motor test was performed.
- Blocks generated code and REV library compatibility still require runtime
  and hardware testing. OnBot, LabVIEW, and FTC walkthroughs remain incomplete.
- Exact desktop architecture support still needs a targeted review: some
  release assets include Windows Arm builds while local prerequisite text
  says unsupported. Asset presence alone does not establish supported use.
- The existing routine-update threshold of image 11 was retained: the OS
  history explicitly says image 11 can update to 12 through the web UI, even
  though the testing README conservatively describes image 12 onward.

Validation: the full WPILib HTML build passed with warnings treated as errors.
The 2027 Python package constraint was checked to admit the documented alpha
version and exclude the previous season. The final incremental build also
passed after the Wi-Fi/runtime wording changes. Checked the rendered Wi-Fi,
installer, Python, and vendor guidance and refreshed the local WPILib preview.
