2027 Robot Overview
===================

The main change for 2027 is the move to Systemcore. Start there when planning
your electronics layout and updating an existing robot.

Systemcore
----------

*FIRST* has confirmed that Systemcore is required for the 2027 season. Each
team will receive a 4 GB unit in the season-specific box of the Kickoff Kit.

The production hardware has changes from the original alpha units, including
power and CAN connectors. Systemcore ships with power input cables. FIRST's
`November 17 availability update
<https://www.firstinspires.org/community-blog/2026-systemcore-on-sale-date-update>`_
says the Black Tote will contain the cables needed to wire the Kitbot,
including RSL and CAN adapters, plus components for making Molex SL cables.
The previously announced complete Molex SL cable kits will not be included;
a crimper is not supplied with the component kit. Check which hardware you
have before following an older diagram or video.

See `FIRST's Systemcore update
<https://community.firstinspires.org/2026-systemcore-pricing-and-availability>`_
for the announcement and `WPILib's Systemcore introduction
<{{ wpilib_docs_url }}docs/software/systemcore-info/systemcore-introduction.html>`_
for the controller overview.

Hardware Preview Updates
------------------------

FIRST's `2027 rule preview, Part 2
<https://www.firstinspires.org/community-blog/2026-event-robot-rule-preview-for-2027-season-part-2>`_
names new component options. See the
:doc:`hardware component overview </docs/controls-overviews/control-system-hardware>`
for the device entries and manufacturer links.

The preview also removes relays from the approved power-regulating devices,
adds servo-power options because Systemcore does not power servos directly,
and calls for COTS connectors on motor circuits. These are preview changes;
use the season manual for the final requirements.

Preparing your robot
--------------------

* Plan mounting and access for the controller, power distribution, radio,
  motor controllers, and wiring.
* Record the components and connections you intend to use.
* Check the manufacturer's instructions for each device and cable.
* Follow :doc:`../zero-to-robot/returning` for the software and controller
  update sequence.

Use the `Systemcore wiring guide in WPILib
<{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_ for controller
connections, then continue with Robot to Motion for software setup.

Kitbot and competition resources
--------------------------------

Use :doc:`../zero-to-robot/step-1/kitbot-starterbot-assembly` for official
assembly resources. Check :doc:`../competition/index` for season documents
before preparing for inspection.

Software updates
----------------

The 2027 software is still being developed. Use a matching WPILib release,
Driver Station, and Systemcore image. Check the
`2027 changelog
<{{ wpilib_docs_url }}docs/yearly-overview/yearly-changelog.html>`_
and `known issues
<{{ wpilib_docs_url }}docs/yearly-overview/known-issues.html>`_
for the release you are using.

Cable-kit information updated November 17, 2026. Other season information
was last reviewed October 14, 2026, using the linked FIRST and WPILib documentation.
