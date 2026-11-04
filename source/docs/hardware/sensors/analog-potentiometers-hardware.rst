Analog Potentiometers - Hardware
================================

A potentiometer is a variable resistor. Used as a voltage divider, it produces
an analog voltage that changes as its shaft turns. A robot can use that
measurement to track a mechanism's position.

Mounting
--------

Many potentiometers have a limited mechanical travel. Arrange the coupling
so the mechanism cannot drive the sensor beyond that travel. Check the shaft
alignment and support so the sensor does not carry unintended loads.

Reading Position
----------------

The wiper provides the changing signal. Check the manufacturer's terminal
identification, supply requirements, and output range before wiring. The
signal must stay within the controller input's allowed range throughout the
mechanism's travel. See :doc:`analog-inputs-hardware`.

Check which direction makes the reading increase before calibrating position
in the robot program.

Systemcore Connections
----------------------

.. note::

   Systemcore connection diagrams for these sensors are still being completed.
   Check the sensor supply, signal levels, pinout, and interface against the
   controller documentation before wiring.

For code, use the `WPILib sensor guide
<https://docs.wpilib.org/en/latest/docs/software/hardware-apis/sensors/analog-potentiometers-software.html>`_.
