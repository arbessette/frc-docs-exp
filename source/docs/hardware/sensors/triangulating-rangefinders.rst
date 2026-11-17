Triangulating Rangefinders
==========================

Triangulating rangefinders estimate distance from the position of reflected
light on a detector. Many use infrared light. This differs from measuring the
travel time of a light pulse.

.. figure:: images/triangulating-rangefinders/infrared-proximity-sensor.png
   :alt: Sharp infrared triangulating rangefinder with its connector visible.
   :width: 350

   Infrared triangulating rangefinder.

Using the Measurement
---------------------

Check the sensor's working range and output curve. An analog output should
not be assumed to change linearly with distance. Use the manufacturer's curve
or a measured calibration when converting a reading into distance.

Test the sensor with the target material, angle, and lighting expected on the
robot. Keep the emitter and receiver unobstructed. See
:doc:`analog-inputs-hardware` for analog interface planning.

Systemcore Connections
----------------------

Use `Systemcore wiring in WPILib <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html#sensor-connections>`_
for controller connections. Check the sensor's electrical interface and the
controller hardware revision before wiring.

For code, use the `WPILib sensor guide
<{{ wpilib_docs_url }}docs/software/hardware-apis/sensors/sensor-overview-software.html>`_.
