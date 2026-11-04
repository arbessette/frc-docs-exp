Sensors on Systemcore
=====================

Sensors provide feedback about mechanism position, robot motion, and the
surrounding field. Choose the sensor and controller interface together,
checking the documentation for both devices before making a connection.

The `WPILib Systemcore introduction
<https://docs.wpilib.org/en/latest/docs/software/systemcore-info/systemcore-introduction.html>`_ describes the controller interfaces.

Choose What You Need to Measure
-------------------------------

Start with the measurement your mechanism or drivetrain needs, then check
how the sensor connects to your controller or motor controller.

.. list-table:: Common sensor choices
   :header-rows: 1
   :widths: 35 65

   * - Measurement
     - Sensor types to consider
   * - Mechanism at a stop or an object present
     - Mechanical, magnetic, inductive, or photoelectric proximity switches.
   * - Shaft position or speed
     - Encoders; potentiometers can measure position over a limited rotation.
   * - Distance to an object
     - Ultrasonic, infrared, or lidar rangefinders.
   * - Rotation or heading
     - Gyroscopes and inertial measurement units (IMUs).
   * - Acceleration
     - Accelerometers, either separate or included in an IMU.

Sensor function and electrical interface are separate choices. Two sensors
that measure the same thing can use different signal voltages or buses.
Check the sensor datasheet and Systemcore documentation before wiring.

Specific Systemcore-compatible examples and wiring diagrams are still needed.

Systemcore Sensor Wiring
------------------------

.. note::

   Smart I/O pinouts, electrical compatibility, switch wiring, encoder
   connections, and sensor bus diagrams are pending for the production
   hardware. Wiring examples from other controllers are not included.

Sensor Selection and Mounting
-----------------------------

.. note::

   Systemcore-compatible sensor examples and mounting illustrations are
   pending review.

Programming
-----------

Use the `WPILib sensor programming overview
<https://docs.wpilib.org/en/latest/docs/software/hardware-apis/sensors/sensor-overview-software.html>`_
for sensor classes and reading measurements in code.

.. toctree::
   :maxdepth: 1
   :caption: Sensor Types

   proximity-switches
   encoders-hardware
   analog-potentiometers-hardware
   gyros-hardware
   accelerometers-hardware
   lidar
   triangulating-rangefinders

.. toctree::
   :maxdepth: 1
   :caption: Electrical Interfaces

   analog-inputs-hardware
   digital-inputs-hardware
   serial-buses
