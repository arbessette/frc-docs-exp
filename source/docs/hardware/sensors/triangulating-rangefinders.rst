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

.. note::

   Systemcore connection diagrams for these sensors are still being completed.
   Check the sensor supply, signal levels, pinout, and interface against the
   controller documentation before wiring.

For code, use the `WPILib sensor guide
<https://docs.wpilib.org/en/latest/docs/software/hardware-apis/sensors/sensor-overview-software.html>`_.
