Sensing and Sensors
===================

Sensors let your robot measure what its mechanisms are doing and detect
objects around it.

Sensor Examples
---------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Sensor
     - What it measures
     - Example use
   * - :doc:`Limit switch </docs/hardware/sensors/proximity-switches>`
     - Whether a mechanism has reached a set position.
     - Detect when an elevator reaches its lower stop.
   * - :doc:`Beam-break sensor </docs/hardware/sensors/proximity-switches>`
     - Whether an object blocks a light beam.
     - Detect a game piece entering the intake.
   * - :doc:`Encoder </docs/hardware/sensors/encoders-hardware>`
     - Shaft position or movement.
     - Track drive-wheel rotation or elevator movement.
   * - :doc:`Potentiometer </docs/hardware/sensors/analog-potentiometers-hardware>`
     - Position over a limited range of rotation.
     - Measure the angle of an arm.
   * - :doc:`Gyro / IMU </docs/hardware/sensors/gyros-hardware>`
     - Rotation rate; an IMU also includes acceleration measurements.
     - Help the drivetrain track its heading.
   * - :doc:`Distance sensor </docs/hardware/sensors/lidar>`
     - Distance to a target.
     - Measure the robot's distance from an object.

Check the sensor's range, mounting, electrical interface, and software support
before choosing a model. Use the
:doc:`sensor hardware guides </docs/hardware/sensors/sensor-overview-hardware>`
for more detail and the status of Systemcore wiring instructions.

Videos
------

WPI Professor Craig Putnam explains different sensor types, how they work,
and how to choose them for a robot.

.. youtube:: 1KiFLdFx1c8

.. youtube:: qLYN6mqbBNs

.. youtube:: taoa8UWRHa0

.. youtube:: J6sgEZ5eJW8

.. youtube:: ukYHeqeSCNM
