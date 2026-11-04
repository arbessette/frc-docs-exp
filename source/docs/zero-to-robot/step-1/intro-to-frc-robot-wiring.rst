FRC Robot Wiring Reference
==========================

Use this guide for a basic four-motor drivetrain with two CIM motors on each
side and one SPARK MAX controller per motor. You can use this setup on a
Kitbot or another differential-drive chassis.

Systemcore runs the robot code and sends commands over CAN. Each SPARK MAX
has its own power connection and runs one motor.

.. note::

   This guide is still being completed. Systemcore power, CAN, and signal-light
   connections need to be checked against the hardware you have. The missing
   details are listed below.

Components
----------

* An assembled differential-drive chassis with four CIM motors, two per side.
* A Systemcore controller and the power cable for its hardware revision.
* Four REV SPARK MAX motor controllers.
* A robot battery, main breaker, and power distribution device, with wire
  and circuit protection that match your components and the current rules.
* A VH-109 radio and its power and Ethernet cables.
* CAN cables, appropriate connectors, mounting hardware, labels, and strain
  relief.

Check the manufacturer instructions for wire sizes, connectors, circuit
protection, and fastener torque. Check the current rules before choosing parts.

.. grid:: 1 3 3 3
   :gutter: 3

   .. grid-item::

      .. figure:: /docs/controls-overviews/images/control-system-hardware/systemcore.png
         :alt: Limelight Systemcore controller.
         :width: 200

         Systemcore. Photo courtesy of Limelight.

   .. grid-item::

      .. figure:: /docs/controls-overviews/images/control-system-hardware/spark-max-motor-controller.png
         :alt: REV SPARK MAX motor controller.
         :width: 200

         SPARK MAX. Photo courtesy of REV Robotics.

   .. grid-item::

      .. figure:: /docs/controls-overviews/images/control-system-hardware/robot-battery.png
         :alt: Robot battery with attached battery leads.
         :width: 200

         Robot battery. Photo courtesy of AndyMark.

See the :doc:`hardware component overview
</docs/controls-overviews/control-system-hardware>` for photos and descriptions
of power distribution, radios, breakers, and other components.

.. admonition:: Photo placeholder: Complete drivetrain
   :class: note

   Show the assembled four-CIM drivetrain from above, with the left and right
   sides, Systemcore, four SPARK MAX controllers, power distribution, battery,
   and radio labeled.

Plan the Connections
--------------------

Each motor controller gets power from the power distribution device:

.. code-block:: text

   Battery -> main breaker / power distribution
              |-> protected branch -> leftLeader   SPARK MAX -> left CIM motor
              |-> protected branch -> leftFollower SPARK MAX -> other left CIM
              |-> protected branch -> rightLeader  SPARK MAX -> right CIM motor
              |-> protected branch -> rightFollower SPARK MAX -> other right CIM
              |-> Systemcore supply connection [details pending]
              `-> radio supply connection [installation-specific]

This map shows where power goes. It does not show connector pins or how to
assemble the cables. Write down the power channel used by each controller.
Power channel numbers and CAN IDs are separate.

Mount the controllers where their power, motor, and CAN connections are
accessible. Keep wiring away from moving parts and provide strain relief.
See :doc:`/docs/hardware/hardware-basics/wiring-best-practices`.

.. admonition:: Photo placeholder: Electronics layout
   :class: note

   Show controller mounting, accessible connectors, cable routing, and strain
   relief. Include enough of the chassis to show where the electronics sit.

SPARK MAX Power and Motor Connections
-------------------------------------

Disconnect the battery before making connections. Check the labels on the
SPARK MAX before connecting wires. Both the power input and motor output
have red and black wires.

* Connect each controller's ``V+`` and ``V-`` power inputs to its protected
  power distribution circuit. Check positive and negative before connecting.
* Connect one brushed CIM motor to each controller's ``A`` and ``B`` motor
  outputs. Leave output ``C`` unused and insulated.
* Set each controller to brushed motor mode before testing.

REV documents these connections in its `SPARK MAX power and motor reference
<https://docs.revrobotics.com/brushless/spark-max/specs/power-and-motor-connections>`_.
Check that reference when identifying the leads. Reversing polarity or mixing
up power and motor connections can damage the controller.

.. admonition:: Photo placeholder: SPARK MAX power and CIM motor leads
   :class: note

   Show one controller with V+ and V- input labels and A and B motor outputs
   visible. Show the unused C lead insulated and the battery disconnected.

CAN Controller Assignments
--------------------------

Use these example assignments to match the WPILib Blocks drivetrain guide.
Label each controller with its side, motor, and CAN ID.

.. list-table:: Example drivetrain assignments
   :header-rows: 1
   :widths: 25 15 30 30

   * - Program name
     - CAN ID
     - Motor
     - Power channel
   * - ``leftLeader``
     - 1
     - Left motor 1
     - Write in your channel
   * - ``leftFollower``
     - 2
     - Left motor 2
     - Write in your channel
   * - ``rightLeader``
     - 3
     - Right motor 1
     - Write in your channel
   * - ``rightFollower``
     - 4
     - Right motor 2
     - Write in your channel

Connect all four controllers to the same Systemcore CAN bus. The Blocks
example uses bus 0 and CAN IDs 1–4. If your robot uses different IDs, update
the code to match.

The code sets one controller on each side to follow the other. Each still
needs its own power, motor, and CAN connections. Do not connect one
controller's motor output to another controller.

Use REV's `SPARK MAX control connection reference
<https://docs.revrobotics.com/brushless/spark-max/specs/control-connections>`_
to identify the CAN connector. Cable order does not set CAN IDs or follower
relationships.

.. admonition:: Photo placeholder: CAN wiring and controller labels
   :class: note

   Show the four controllers with CAN IDs 1–4 and motor-side labels. Make the
   CAN cable routing visible. Capture the Systemcore connector and termination
   once the connections have been checked for this Systemcore revision.

Systemcore Details Still Needed
-------------------------------

.. list-table:: Wiring details to add
   :header-rows: 1
   :widths: 30 70

   * - Connection
     - Required information
   * - Systemcore supply
     - Input connector, polarity, cable assembly, and protected distribution
       connection for the installed controller revision.
   * - CAN bus
     - Systemcore connector pinout, connection to the controller chain, and
       termination at the ends of the bus. See
       :doc:`/docs/hardware/hardware-basics/can-wiring-basics` for its status.
   * - Radio
     - Power connection and Ethernet port/cable assignment for the chosen
       Systemcore and VH-109 installation.
   * - Signal light
     - Systemcore connection diagram and indicator behavior for the installed
       hardware and firmware.

For more about the controller, see the `WPILib Systemcore introduction
<https://docs.wpilib.org/en/latest/docs/software/systemcore-info/systemcore-introduction.html>`_.
Use WPILib's Robot to Motion guide to update Systemcore and configure the
radio.

.. admonition:: Photo placeholder: Systemcore power connection
   :class: note

   Show the controller hardware revision, connector orientation, polarity
   markings, and power cable route to the protected distribution connection.
   Take the photo once the power connection has been checked.

.. admonition:: Photo placeholder: Radio installation
   :class: note

   Show the VH-109 mounting, labeled power connection, and Ethernet cable route
   to Systemcore. Use the same hardware configuration as the wiring reference.

.. admonition:: Photo placeholder: Signal-light connection
   :class: note

   Show the signal light mounting and its labeled Systemcore connection.
   Take the photo once the connector and wiring have been checked.

Inspect, Then Program
---------------------

Record power channels, CAN IDs, hardware revisions, and cable assignments.
Before applying power, complete the
:doc:`physical inspection checklist
</docs/hardware/hardware-basics/preemptive-troubleshooting>`.

Once the hardware is ready, continue to `Robot to Motion
<https://docs.wpilib.org/en/latest/docs/zero-to-robot/introduction.html>`_.
The `Blocks drivetrain example
<https://docs.wpilib.org/en/latest/docs/software/blocks/first-project.html>`_
uses the controller names and CAN IDs above. Follow it to set up the
followers, check motor direction, and test the drivetrain.

:doc:`Wiring walkthrough <basic-robot-wiring>` ·
:doc:`← Zero to Robot <../index>`
