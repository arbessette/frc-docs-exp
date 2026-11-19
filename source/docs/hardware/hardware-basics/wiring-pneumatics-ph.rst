Wiring Pneumatics - REV Pneumatic Hub
=====================================


This page describes wiring pneumatics with the REV Pneumatic Hub (:external+wpilib:term:`PH`). For instructions on wiring pneumatics with the CTRE Pneumatic Control Module (:external+wpilib:term:`PCM`) see :doc:`this page <wiring-pneumatics-pcm>`.

.. hint:: For pneumatics safety & mechanical requirements, consult this year's Robot Construction rules. For mechanical design guidelines, refer to the `FIRST Pneumatics Manual <https://info.firstinspires.org/hubfs/web/program/frc/resources/pneumatics-manual.pdf>`__.

.. seealso:: For Pneumatic Hub configuration, firmware updates, and detailed technical specifications, see the `REV Pneumatic Hub Documentation <https://docs.revrobotics.com/ion-control-system/ph>`__.


Wiring Overview
---------------

For complicated robot designs requiring more channels or multiple solenoid voltages, additional PHs, or PCMs can be added to the control system.

PCM Power and Control Wiring
----------------------------


.. image:: images/wiring-pneumatics-ph/ph-subsystem.png
   :alt: Pneumatics wiring diagram showing all of the connections to the PH.

Additional PHs can be wired to a standard WAGO connector on the side of the PDP and protected with a 20A or smaller circuit breaker or to a 15A port on the PDH. Additional PHs should also be placed anywhere in the middle of the CAN chain.

The Compressor
--------------


The compressor can be wired directly to the Compressor connectors on the PH. If additional length is required, make sure to use 18 AWG wire or larger for the extension.

The Pressure Switch
-------------------


The PH has two options for detecting pressure, a digital pressure switch, or an analog pressure switch.

Digital
^^^^^^^


A digital pressure switch should be connected directly to the digital pressure sensor input terminals on the PCM. There is no polarity on the input terminals or on the pressure switch itself, either terminal on the PH can be connected to either terminal on the switch. Ring or spade terminals are recommended for the connection to the switch screws (note that the screws are slightly larger than #6, but can be threaded through a ring terminal with a hole for a #6 screw such as the terminals shown in the image).

Analog
^^^^^^


An analog pressure switch (`REV-11-1107 <https://www.revrobotics.com/rev-11-1107/>`__ can be connected directly to the analog pressure sensor port 0 input terminals. Using an analog pressure sensor allows reading the pressure in the pneumatic system through code and setting custom trigger thresholds for turning on and off the compressor.

.. warning:: The Analog Pressure Sensor port is a very tight fit and requires special attention. See `REV Wiring an Analog Pressure Sensor <https://docs.revrobotics.com/ion-control-system/ph/gs/wiring#wiring-an-analog-pressure-sensor>`__ for more tips

Solenoids
---------


Each solenoid channel should be wired directly to a numbered pair of terminals on the PH. A single acting solenoid will use one numbered terminal pair. A double acting solenoid will use two pairs. If your solenoid does not come with color coded wiring, check the datasheet to make sure to wire with the proper polarity.

Solenoid Voltage Switch
-----------------------


The PH is capable of powering either 12V or 24V solenoids, but all solenoids connected to a single PH must be the same voltage. Set the voltage switch to the appropriate voltage for solenoids prior to use.

.. note:: Systemcore scope

   The wording above is retained from the upstream article. Controller-specific
   material and illustrations that do not apply to this site's Systemcore scope
   are excluded rather than relabeled. Use the
   `Systemcore wiring guide <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_
   for the installed revision's connection requirements.

Source: `WPILib upstream, 2f175339
<https://github.com/wpilibsuite/wpilib-docs/blob/2f175339ca2f66bdd8b733eb5832d9ab9291f1c1/source/docs/hardware/hardware-basics/wiring-pneumatics-ph.rst>`_,
`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__.
