Analog Inputs - Hardware
========================

An analog sensor reports a measurement as a changing voltage. Potentiometers
and some distance or acceleration sensors use analog outputs.

Check the Electrical Range
--------------------------

Check both the sensor supply and its possible signal-voltage range. The
sensor's output must match the controller input's limits, including at the
ends of the sensor's measurement range. The supply rating and signal range
are not necessarily the same thing.

A multi-axis sensor may have a separate analog signal for each axis. Record
which input reads each signal. Use :doc:`analog-potentiometers-hardware` and
:doc:`accelerometers-hardware` for examples of the measurements involved.

Systemcore Connections
----------------------

Use `Systemcore wiring in WPILib <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html#sensor-connections>`_
for controller connections. Check the sensor's electrical interface and the
controller hardware revision before wiring.

For code, use the `WPILib sensor guide
<{{ wpilib_docs_url }}docs/software/hardware-apis/sensors/analog-inputs-software.html>`_.
