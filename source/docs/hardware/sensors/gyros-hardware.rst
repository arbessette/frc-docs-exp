Gyroscopes - Hardware
=====================

A gyroscope measures rotation rate. The robot program can use that measurement
to help track heading or stabilize driving. An inertial measurement unit (IMU)
combines a gyro with an accelerometer and may include other sensors.

Mounting and Axes
-----------------

Mount the sensor securely and record its orientation on the robot. Check which
axis the manufacturer calls yaw, pitch, or roll, and how positive rotation is
defined. Those conventions must match the assumptions in the robot program.

Use the `WPILib axis conventions
<https://docs.wpilib.org/en/latest/docs/software/hardware-apis/motors/wpi-drive-classes.html#axis-conventions>`_
when connecting the hardware measurements to drive code.

Choosing an Interface
---------------------

Gyros and IMUs use different interfaces depending on the model. Check the
sensor documentation for power, communication, and software support. An
integrated controller sensor and an external IMU can require different APIs.
See :doc:`accelerometers-hardware` for the other part of an IMU.

Systemcore Connections
----------------------

.. note::

   Systemcore connection diagrams for these sensors are still being completed.
   Check the sensor supply, signal levels, pinout, and interface against the
   controller documentation before wiring.

For code, use the `WPILib sensor guide
<https://docs.wpilib.org/en/latest/docs/software/hardware-apis/sensors/gyros-software.html>`_.
