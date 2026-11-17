Sensor Communication Buses
==========================

A communication bus carries measurements and configuration data between
devices. Some sensors use CAN, I2C, or USB instead of separate analog or
digital measurement signals.

Choose the Interface
--------------------

Check that the sensor and controller support the same electrical interface
and protocol. Record the connector pinout, supply, device address or ID,
and software needed to read the measurements.

CAN
---

Devices on a CAN bus need the correct wiring and bus termination. See
:doc:`/docs/hardware/hardware-basics/can-wiring-basics` for the Systemcore
wiring documentation status. CAN IDs do not identify power distribution
channels.

I2C and USB
-----------

Check device addresses and electrical requirements for I2C sensors. For USB,
check the required host connection, power, driver, and software support.
A matching connector alone does not establish compatibility.

For CAN programming, use `Using CAN Devices in WPILib
<{{ wpilib_docs_url }}docs/software/can-devices/using-can-devices.html>`_.

Systemcore Connections
----------------------

Use `Systemcore wiring in WPILib <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html#sensor-connections>`_
for controller connections. Check the sensor's electrical interface and the
controller hardware revision before wiring.

For code, use the `WPILib sensor guide
<{{ wpilib_docs_url }}docs/software/hardware-apis/sensors/sensor-overview-software.html>`_.
