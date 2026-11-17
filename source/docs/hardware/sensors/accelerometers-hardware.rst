Accelerometers - Hardware
=========================

Accelerometers measure acceleration along one or more axes. They can be
separate devices or part of an IMU with a :doc:`gyro <gyros-hardware>`.

Single-axis sensors measure along one direction. Multi-axis sensors provide
measurements along several axes, so their mounting orientation matters.
Record the sensor axes and keep the sensor fixed to the part being measured.

Choosing a Sensor
-----------------

Check the measurement range, noise, update rate, and interface. Do not assume
that integrating acceleration twice will give useful robot position: small
measurement errors accumulate. Match the sensor to the measurement you need.

Analog sensors may use one signal per measured axis. Other devices send
measurements over a bus. Check :doc:`analog-inputs-hardware` and
:doc:`serial-buses` before planning the connection.

Systemcore Connections
----------------------

Use `Systemcore wiring in WPILib <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html#sensor-connections>`_
for controller connections. Check the sensor's electrical interface and the
controller hardware revision before wiring.

For code, use the `WPILib sensor guide
<{{ wpilib_docs_url }}docs/software/hardware-apis/sensors/accelerometers-software.html>`_.
