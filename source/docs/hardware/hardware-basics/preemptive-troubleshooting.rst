Robot Preemptive Troubleshooting
================================

Inspect the robot before practice and competition, and repeat the checks after
repairs or significant impacts. Record problems and repairs so the next person
working on the robot knows what changed.

These checks cover physical connections and mounting on Systemcore robots.
Use the manufacturer's instructions for the controller hardware revision and
power distribution device installed on your robot.

Prepare for Inspection
----------------------

Disable the robot and disconnect the battery before adjusting electrical
connections or working near moving mechanisms. Support mechanisms that could
move when power is removed. Use the component manufacturer's procedures for
fastener torque, connector assembly, and maintenance.

For wiring layout, strain relief, and labeling, see
:doc:`wiring-best-practices`. For battery handling and testing, see
:doc:`robot-battery`.

Keep Inspection Tools Handy
---------------------------

A flashlight helps you see inside the robot and check cable routes. Use the
connector manufacturer's recommended tool when opening spring terminals.

.. figure:: images/preemptive-troubleshooting/tools.png
   :alt: WAGO terminal tool and a handheld flashlight.
   :width: 450

   WAGO terminal tool and flashlight.

Battery and Main Power Connections
----------------------------------

* Check that the battery is secured to the chassis and cannot move into wiring
  or mechanisms.
* Inspect the battery case, cables, insulation, crimps, and connector housings
  for damage. Follow the battery guide when deciding whether to remove a
  battery from service.
* Check that terminal covers and insulation are in place. Exposed terminals in
  inspection photographs are for illustration, not the operating condition.
* Check that the robot-side battery connector and main power leads have strain
  relief so battery changes do not pull on breaker or distribution terminals.
* Inspect the main breaker mounting and terminals for damage or movement.
  Follow the manufacturer's tightening procedure; do not twist terminals or
  apply force to molded studs as a test.

Power Distribution and Branch Wiring
------------------------------------

* Check that the power distribution device and connected components are
  securely mounted.
* Inspect connections for exposed strands, damaged insulation, loose terminals,
  discoloration, and cables rubbing against sharp edges or moving parts.
* Check connector seating and wire retention using the manufacturer's
  inspection procedure. Correct a loose connection before applying power.
* Confirm that installed fuses and breakers match the wiring design and the
  applicable component instructions. Fuse positions and ratings differ between
  distribution devices; do not apply a PDP layout to another model.
* Have another team member check repaired connections before returning the
  robot to service.

Controller, Radio, and Signal Cables
------------------------------------

* Inspect Ethernet plugs for damaged latches and check that cables are supported
  near their connectors.
* Check controller and radio power connectors, CAN connections, and sensor
  cables for secure seating and strain relief.
* Keep metal chips and debris out of electronics when drilling or cutting near
  installed components. Inspect the area before reconnecting power.
* Confirm that cables remain clear through the intended mechanism travel.

For LED indications, see :doc:`status-lights-ref`. For CAN wiring, see
:doc:`can-wiring-basics` and check its hardware scope before using a diagram.

Controlled Functional Check
---------------------------

After completing the unpowered inspection, clear the work area and follow the
team's normal procedures for a controlled functional test. Keep people clear
of moving mechanisms and stop the test if a connection becomes intermittent
or a component behaves unexpectedly.

Record the conditions that reproduce a fault. Do not drop the robot or shake
powered electrical connections to simulate match impacts. Use WPILib's
`troubleshooting guide
<https://docs.wpilib.org/en/stable/docs/software/support/troubleshooting.html>`_
for software and connection diagnostics.

Driver Station and Event Checks
-------------------------------

* Bring the Driver Station laptop power supply and inspect frequently used USB
  and Ethernet cables for damage.
* Confirm that the team has completed the applicable WPILib setup and software
  update procedures before the event.
* Review Driver Station logs after testing or a match and record unexpected
  disconnects or voltage changes for investigation.
* Recheck mounting and electrical connections after significant impacts and
  repairs. Assign responsibility for the inspection and record its completion.

Use :doc:`../../competition/index` to prepare the team's event checklist.

Continue to Software Setup
--------------------------

For a newly assembled Systemcore robot, complete the unpowered physical checks
above before moving to software setup and controlled powered tests. Resolve
inspection problems before enabling the robot.

Use `Robot to Motion in WPILib Docs
<{{ wpilib_docs_url }}docs/zero-to-robot/introduction.html>`_
to set up your environment, configure Systemcore, and deploy your first program.
After testing, use the Driver Station and event checks above to prepare for
practice and competition.

.. button-link:: {{ wpilib_docs_url }}docs/zero-to-robot/introduction.html
   :color: primary
   :outline:

   Continue to Robot to Motion →

:doc:`← Zero to Robot </docs/zero-to-robot/index>`
