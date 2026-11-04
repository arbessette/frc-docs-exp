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

.. note::

   Systemcore connection diagrams for these sensors are still being completed.
   Check the sensor supply, signal levels, pinout, and interface against the
   controller documentation before wiring.

For code, use the `WPILib sensor guide
<https://docs.wpilib.org/en/latest/docs/software/hardware-apis/sensors/analog-inputs-software.html>`_.
