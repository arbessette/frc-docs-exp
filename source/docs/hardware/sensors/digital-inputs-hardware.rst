Digital Inputs - Hardware
=========================

A digital input reads discrete signal states. A simple switch, proximity
sensor, or encoder can provide digital signals.

Switches and Powered Sensors
----------------------------

A switch changes an electrical connection when activated. A powered sensor
may provide its output through a different circuit. Check whether the sensor
uses an open-collector, open-drain, or driven output and what the controller
input supports.

The input's pull resistor affects how an open switch is read. Use the
controller's documented input circuit when choosing the connections and
checking the code. Do not assume an open switch always means high or low.

See :doc:`proximity-switches` and :doc:`encoders-hardware` for sensor choices.

Systemcore Connections
----------------------

.. note::

   Systemcore connection diagrams for these sensors are still being completed.
   Check the sensor supply, signal levels, pinout, and interface against the
   controller documentation before wiring.

For code, use the `WPILib sensor guide
<https://docs.wpilib.org/en/latest/docs/software/hardware-apis/sensors/digital-inputs-software.html>`_.
