Lidar - Hardware
================

Lidar uses emitted light and its return to measure distance. The measurement
can help detect objects or map the area around a robot.

Single-direction Sensors
------------------------

.. figure:: images/lidar/1-dimentional-lidar.png
   :alt: Garmin LIDAR-Lite sensor and attached cable.
   :width: 300

   Single-direction lidar sensor.

A single-direction sensor measures along its beam. Check its minimum and
maximum range, field of view, update rate, and communication interface.

Scanning Sensors
----------------

.. figure:: images/lidar/2-dimentional-lidar.png
   :alt: RPLIDAR scanning sensor.
   :width: 300

   Scanning lidar sensor.

A scanning sensor collects measurements across a plane. The program must
handle a set of range readings rather than one distance. Check the scan rate,
angular resolution, and available software support.

Choosing a Target
-----------------

Reflectivity, transparent surfaces, target angle, and distance can affect the
reading. Test with the actual objects you want to detect. More distant targets
also have wider spacing between samples at a fixed angular resolution.

See :doc:`serial-buses` for communication choices.

Systemcore Connections
----------------------

Use `Systemcore wiring in WPILib <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html#sensor-connections>`_
for controller connections. Check the sensor's electrical interface and the
controller hardware revision before wiring.

For code, use the `WPILib sensor guide
<{{ wpilib_docs_url }}docs/software/hardware-apis/sensors/sensor-overview-software.html>`_.
