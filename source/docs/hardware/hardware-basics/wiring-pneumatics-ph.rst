Wiring Pneumatics - REV Pneumatic Hub
=====================================

This page describes the REV Pneumatic Hub component connections.

.. hint:: For pneumatics safety & mechanical requirements, consult this year's Robot Construction rules. For mechanical design guidelines, the FIRST Pneumatics Manual is located `here <https://www.firstinspires.org/sites/default/files/uploads/resource_library/frc/technical-resources/frc_pneumatics_manual.pdf>`__

.. seealso:: For Pneumatic Hub configuration, firmware updates, and detailed technical specifications, see the `REV Pneumatic Hub Documentation <https://docs.revrobotics.com/ion-control-system/ph>`__.

Systemcore Power and CAN Connections
------------------------------------

.. note::

   The Systemcore-to-Pneumatic-Hub wiring diagram is pending. It must identify
   the power distribution connection, CAN connector pinout, and termination
   for the installed hardware.

Use the `REV Pneumatic Hub documentation
<https://docs.revrobotics.com/ion-control-system/ph>`_ for module connections.
The component instructions below do not replace the pending Systemcore wiring
procedure.

Pneumatic Hub Component Connections
-----------------------------------

.. figure:: images/wiring-pneumatics-ph/ph-subsystem.png
   :alt: REV Power Distribution Hub connected to a Pneumatic Hub, compressor, pressure sensors, and solenoids.
   :width: 650

   Pneumatic Hub, power distribution, compressor, pressure sensors, and solenoids.

Use the `REV Pneumatic Hub wiring guide
<https://docs.revrobotics.com/ion-control/ph/gs/wiring>`_ for the component
connections. The controller connection and bus termination still need the
Systemcore instructions for your hardware revision.

The Compressor
--------------

The compressor can be wired directly to the Compressor connectors on the PH. If additional length is required, make sure to use 18 AWG wire or larger for the extension.

The Pressure Switch
-------------------

The PH has two options for detecting pressure, a digital pressure switch, or an analog pressure switch.

Digital
~~~~~~~

A digital pressure switch should be connected directly to the digital pressure sensor input terminals on the PH. There is no polarity on the input terminals or on the pressure switch itself, either terminal on the PH can be connected to either terminal on the switch. Ring or spade terminals are recommended for the connection to the switch screws (note that the screws are slightly larger than #6, but can be threaded through a ring terminal with a hole for a #6 screw such as the terminals shown in the image).

Analog
~~~~~~

An analog pressure switch (`REV-11-1107 <https://www.revrobotics.com/rev-11-1107/>`__ can be connected directly to the analog pressure sensor port 0 input terminals. Using an analog pressure sensor allows reading the pressure in the pneumatic system through code and setting custom trigger thresholds for turning on and off the compressor.

.. warning:: The Analog Pressure Sensor port is a very tight fit and requires special attention. See `REV Wiring an Analog Pressure Sensor <https://docs.revrobotics.com/ion-control-system/ph/gs/wiring#wiring-an-analog-pressure-sensor>`__ for more tips

Solenoids
---------

Each solenoid channel should be wired directly to a numbered pair of terminals on the PH. A single acting solenoid will use one numbered terminal pair. A double acting solenoid will use two pairs. If your solenoid does not come with color coded wiring, check the datasheet to make sure to wire with the proper polarity.

Solenoid Voltage Switch
-----------------------

The PH is capable of powering either 12V or 24V solenoids, but all solenoids connected to a single PH must be the same voltage. Set the voltage switch to the appropriate voltage for solenoids prior to use.
