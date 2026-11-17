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

Use `Systemcore wiring in WPILib <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html#sensor-connections>`_
for controller connections. Check the sensor's electrical interface and the
controller hardware revision before wiring.

For code, use the `WPILib sensor guide
<{{ wpilib_docs_url }}docs/software/hardware-apis/sensors/digital-inputs-software.html>`_.
