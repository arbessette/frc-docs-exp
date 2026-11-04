Status Light Quick Reference
============================

Use the indicator reference for the exact component model and firmware
installed on your Systemcore robot.

Systemcore
----------

.. note::

   The Systemcore LED and display reference is pending. Do not infer controller
   faults from another controller's indicator patterns.

See the `WPILib Systemcore introduction
<https://docs.wpilib.org/en/latest/docs/software/systemcore-info/systemcore-introduction.html>`_ and the
`WPILib Systemcore imaging guide
<https://docs.wpilib.org/en/latest/docs/zero-to-robot/step-3/imaging-your-systemcore.html>`_ for the available controller
and update information.

Robot Signal Light
------------------

.. note::

   Systemcore signal-light connections and status patterns are pending.

Vivid-Hosting VH-109 Radio
--------------------------

.. image:: images/status-lights/radio-lights.png
  :alt: The 5 lights positioned on the top side of the radio.
  :width: 600

`VH-109 Status Lights <https://frc-radio.vivid-hosting.net/overview/led-status-indications>`__

+----------+----------------+------------------------------+
| Power    | Green          | On or Powering up            |
|          +----------------+------------------------------+
|          | Off            | No Power                     |
+----------+----------------+------------------------------+
| System   | Solid Green    | Able to ping the field       |
| Status   +----------------+------------------------------+
|          | Blinking (1Hz) | Unable to ping the field     |
|          +----------------+------------------------------+
|          | Blinking (20Hz)| Firmware being flashed       |
|          +----------------+------------------------------+
|          | Blinking (50Hz)| Performing "first boot"      |
|          +----------------+------------------------------+
|          | Off            | Booting Up                   |
+----------+----------------+------------------------------+
| 2.4 GHz  | Solid Green    | Wifi available               |
|          +----------------+------------------------------+
|          | Blinking (20Hz)| Battery detected,            |
|          | Sys Blinking   | Wireless is disabled         |
+----------+----------------+------------------------------+
| 6 GHz    | Solid Blue     | 6 GHz connection made        |
|          +----------------+------------------------------+
|          | Blinking (20Hz)| Battery detected,            |
|          | Sys Blinking   | Wireless is disabled         |
+----------+----------------+------------------------------+

Power Distribution Panel
------------------------

.. note::

   Status indications for this component on a Systemcore installation are
   pending review. Use the manufacturer's reference for the exact model
   and firmware.

Power Distribution Hub
----------------------

.. image:: images/status-lights/power-distribution-hub.png
  :alt: REV Power Distribution Hub with Status LED, and Channel LEDs Highlighted
  :width: 400

.. note:: These led patterns only apply to firmware version 21.1.7 and later

PDH Status LED
--------------

.. note::

   Status indications for this component on a Systemcore installation are
   pending review. Use the manufacturer's reference for the exact model
   and firmware.

PDH Channel LEDs
----------------

For firmware 21.1.7 and later, REV lists these channel indicators:

.. list-table:: Power Distribution Hub channel indicators
   :header-rows: 1
   :widths: 25 75

   * - LED
     - Meaning
   * - Off
     - Channel voltage is present and operation is normal.
   * - Solid red
     - No channel voltage; check for a tripped or missing breaker.
   * - Blinking red
     - A stored channel fault; check the breaker and clear the fault after
       resolving the cause.

For the switched channel, check its fuse instead of a breaker. See the
`REV PDH status LED reference
<https://docs.revrobotics.com/ion-control/pdh/status-led>`_ for the full patterns
and firmware scope.

Voltage Regulator Module
------------------------

.. image:: images/status-lights/vrm-status-lights.svg
  :alt: Highlights the position of the 12V and 5V status lights.
  :width: 400

The status LEDs on the VRM indicate the state of the two power supplies. If the supply is functioning properly the LED should be lit bright green. If the LED is not lit or is dim, the output may be shorted or drawing too much current.

Pneumatics Control Module (PCM)
-------------------------------

.. note::

   Status indications for this component on a Systemcore installation are
   pending review. Use the manufacturer's reference for the exact model
   and firmware.

Pneumatic Hub
-------------

.. image:: images/status-lights/pneumatic-hub.png
  :alt: REV Pneumatic Hub with Status LED, Compressor LED, and Solenoid LEDs highlighted
  :width: 400

.. note:: These led patterns only apply to firmware version 21.1.7 and later

PH Status LED
^^^^^^^^^^^^^

+-------------------------+--------------------------------------------------+
| LED Color               | Status                                           |
+=========================+==================================================+
| Blue Solid              | Device on but no communication established       |
+-------------------------+--------------------------------------------------+
| Green Solid             | Main Communication established                   |
+-------------------------+--------------------------------------------------+
| Magenta Blinking        | Keep Alive Timeout                               |
+-------------------------+--------------------------------------------------+
| Solid Cyan              | Secondary Heartbeat (connected to REV HW Client) |
+-------------------------+--------------------------------------------------+
| Orange/Blue Blinking    | Hardware Fault                                   |
+-------------------------+--------------------------------------------------+
| Orange/Yellow Blinking  | CAN Fault                                        |
+-------------------------+--------------------------------------------------+
| Orange/Red Blinking     | Fail Safe                                        |
+-------------------------+--------------------------------------------------+
| Orange/Magenta Blinking | Device Over Current                              |
+-------------------------+--------------------------------------------------+
| Orange/Green Blinking   | Orange/Green Blinking                            |
+-------------------------+--------------------------------------------------+

Compressor LED
^^^^^^^^^^^^^^

+-------------+----------------+
| LED Color   | Status         |
+=============+================+
| Green Solid | Compressor On  |
+-------------+----------------+
| Black Solid | Compressor Off |
+-------------+----------------+

Solenoid LEDs
^^^^^^^^^^^^^

+-------------+--------------+
| LED Color   | Status       |
+=============+==============+
| Green Solid | Solenoid On  |
+-------------+--------------+
| Black Solid | Solenoid Off |
+-------------+--------------+

Talon SRX & Victor SPX Motor Controllers
----------------------------------------

.. image:: images/status-lights/talon-srx-status-lights.png
  :alt: Status LEDs on either side of the center of the Talon SRX.
  :width: 600

These motor controllers use Phoenix 5. For the most up-to-date information, see the `CTRE Phoenix 5 Documentation <https://v5.docs.ctr-electronics.com/en/stable/ch13_MC.html>`__.


Talon SRX/Victor SPX Status LEDs During Normal Operation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------------------+----------------+--------------------------------------------+
| LEDs                         | Colors         | Device State                               |
+==============================+================+============================================+
| Both                         | Blinking Green | Forward throttle is applied.               |
|                              |                | Blink rate is proportional to Duty Cycle.  |
+------------------------------+----------------+--------------------------------------------+
| Both                         | Blinking Red   | Reverse throttle is applied.               |
|                              |                | Blink rate is proportional to Duty Cycle.  |
+------------------------------+----------------+--------------------------------------------+
| None                         | None           | No power is being applied                  |
+------------------------------+----------------+--------------------------------------------+
| LEDs Alternate               | Off/Orange     | CAN bus detected, robot disabled           |
+------------------------------+----------------+--------------------------------------------+
| LEDs Alternate               | Off/Slow Red   | CAN bus/PWM is not detected                |
+------------------------------+----------------+--------------------------------------------+
| LEDs Alternate               | Off/Fast Red   | Fault Detected                             |
+------------------------------+----------------+--------------------------------------------+
| LEDs Alternate               | Red/Orange     | Damaged Hardware                           |
+------------------------------+----------------+--------------------------------------------+
| LEDs Strobe towards (M-)     | Off/Red        | Forward Limit Switch or Forward Soft Limit |
+------------------------------+----------------+--------------------------------------------+
| LEDs Strobe towards (M+)     | Off/Red        | Reverse Limit Switch or Reverse Soft Limit |
+------------------------------+----------------+--------------------------------------------+
| LED1 Only (closest to M+/V+) | Green/Orange   | In Boot-loader                             |
+------------------------------+----------------+--------------------------------------------+

Talon SRX/Victor SPX Status LEDs During Calibration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------------+------------------------+
| Status LEDs Blink Code | Device State           |
+========================+========================+
| Flashing Red/Green     | Calibration Mode       |
+------------------------+------------------------+
| Blinking Green         | Successful Calibration |
+------------------------+------------------------+
| Blinking Red           | Failed Calibration     |
+------------------------+------------------------+

Talon SRX/Victor SPX B/C CAL Blink Codes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+--------------+
| B/C CAL Button Color | Device State |
+======================+==============+
| Solid Red            | Brake Mode   |
+----------------------+--------------+
| Off                  | Coast Mode   |
+----------------------+--------------+

Talon FX Motor Controller
-------------------------

The Talon FX uses Phoenix 6. For the most up-to-date information, see the `CTRE Phoenix 6 Documentation <https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/talonfx/index.html#status-light-reference>`__.


Talon FX Status LEDs
^^^^^^^^^^^^^^^^^^^^

+------------------------------+-------------------------------------+
| LED State                    | Meaning                             |
+==============================+=====================================+
| LEDs Off                     | No Power                            |
+------------------------------+-------------------------------------+
| Blinking Alternating Red     | No valid CAN/PWM signal             |
+------------------------------+-------------------------------------+
| Blinking Alternating Orange  | CAN detected but no Phoenix running |
+------------------------------+-------------------------------------+
| Blinking Simultaneous Orange | Valid CAN signal, device disabled   |
+------------------------------+-------------------------------------+
| Both Solid Orange            | Enabled with neutral output         |
+------------------------------+-------------------------------------+
| Blinking Simultaneous Red    | Driving in reverse                  |
+------------------------------+-------------------------------------+
| Blinking Simultaneous Green  | Driving forward                     |
+------------------------------+-------------------------------------+
| Offset Alternating Red/Off   | Device limit reached                |
+------------------------------+-------------------------------------+
| Offset Orange/Off            | Thermal cutoff                      |
+------------------------------+-------------------------------------+
| Alternate Red/Green          | Pro-only command while unlicensed   |
+------------------------------+-------------------------------------+
| Alternate Red/Orange         | Damaged Hardware                    |
+------------------------------+-------------------------------------+
| Single LED alternates        | Device in bootloader                |
| Green/Orange                 |                                     |
+------------------------------+-------------------------------------+

Talon FX B/C CAL Blink Codes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------+--------------+
| B/C CAL Button Color | Device State |
+======================+==============+
| Solid Red            | Brake Mode   |
+----------------------+--------------+
| Off                  | Coast Mode   |
+----------------------+--------------+

SPARK-MAX Motor Controller
--------------------------

.. image:: images/status-lights/sparkMAXLight.png
  :alt: Table listing the SPARKMAX blink codes.

REV Robotics SPARK
------------------

.. image:: images/status-lights/sparkLight.png
  :alt: Table of the SPARK blink codes.

Victor-SP Motor Controller
--------------------------

.. image:: images/status-lights/victorSPLight.png
  :alt: Status LEDs on either side of the center of the Victor-SP.
  :width: 600

Brake/Coast/Cal Button/LED - Red if the controller is in brake mode, off if the controller is in coast mode

Status
^^^^^^

+-----------+----------+------------------------------------------------------------------------+
| Green     | Solid    | Full forward output                                                    |
|           +----------+------------------------------------------------------------------------+
|           | Blinking | Proportional to forward output voltage                                 |
+-----------+----------+------------------------------------------------------------------------+
| Red       | Solid    | Full reverse output                                                    |
|           +----------+------------------------------------------------------------------------+
|           | Blinking | Proportional to forward output voltage                                 |
+-----------+----------+------------------------------------------------------------------------+
| Orange    | Solid    | FRC robot disabled, PWM signal lost, or                                |
|           |          | signal in deadband range (+/- 4% output)                               |
+-----------+----------+------------------------------------------------------------------------+
| Red/Green | Blinking | Ready for calibration. Several green flashes indicates successful      |
|           |          | calibration, and red several times indicates unsuccessful calibration. |
+-----------+----------+------------------------------------------------------------------------+

Talon Motor Controller
----------------------

.. image:: images/status-lights/talonsr-status-light.png
  :alt: Talon motor controller with a single multicolor LED in the bottom right corner.

+-----------+----------+------------------------------------------------------------------------+
| Green     | Solid    | Full forward output                                                    |
|           +----------+------------------------------------------------------------------------+
|           | Blinking | Proportional to forward output voltage                                 |
+-----------+----------+------------------------------------------------------------------------+
| Red       | Solid    | Full reverse output                                                    |
|           +----------+------------------------------------------------------------------------+
|           | Blinking | Proportional to reverse output voltage                                 |
+-----------+----------+------------------------------------------------------------------------+
| Orange    | Solid    | No CAN devices are connected                                           |
|           +----------+------------------------------------------------------------------------+
|           | Blinking | Disabled state, PWM signal lost, FRC robot disabled, or                |
|           |          | signal in deadband range (+/- 4% output)                               |
+-----------+----------+------------------------------------------------------------------------+
| Off                  | No input power to Talon                                                |
+-----------+----------+------------------------------------------------------------------------+
| Red/Green | Flashing | Ready for calibration. Several green flashes indicates successful      |
|           |          | calibration, and red several times indicates unsuccessful calibration. |
+-----------+----------+------------------------------------------------------------------------+

Venom Motor Controller
----------------------

.. image:: images/status-lights/venom.png
  :alt: The LED blink codes for the Venom.

REV Robotics Servo Power Module
-------------------------------

.. image:: images/status-lights/rev-robotics-servo-power-module.png
  :alt: One power LED and a status LED for each channel all down the center.
  :width: 400

Status LEDs
^^^^^^^^^^^

Each channel has a corresponding status LED that will indicate the sensed state of the connected :external+wpilib:term:`PWM` signal. The table below describes each state's corresponding LED pattern.

+-----------------------+----------------+
| State                 | Pattern        |
+=======================+================+
| No Signal             | Blinking Amber |
+-----------------------+----------------+
| Left/Reverse Signal   | Solid Red      |
+-----------------------+----------------+
| Center/Neutral Signal | Solid Amber    |
+-----------------------+----------------+
| Right/Forward Signal  | Solid Green    |
+-----------------------+----------------+

- 6V Power LED off, dim, or flickering with power applied = Over-current shutdown

REV Robotics Servo Hub
----------------------

Use `REV's Servo Hub status LED reference
<https://docs.revrobotics.com/rev-crossover-products/servo/servo-hub/servo-hub-status-led-patterns>`_
for the main status light and individual channel indicators. Check the firmware
scope on that page against the firmware installed on your hub.

The stable WPILib table differs from REV's current reference. Use the
manufacturer's current definitions when diagnosing this component.

CANCoder Encoder
----------------

.. image:: images/status-lights/cancoder-status-lights.png
  :alt: LED at the top of the encoder.
  :width: 400

+---------------------+-----------------+------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+
| LED Color           | LED Brightness  | CAN Bus detection                  | Magnet Field Strength                                                 | Description                                                     |
+=====================+=================+====================================+=======================================================================+=================================================================+
| Off                 | Off             |                                    |                                                                       | CANCoder is not powered                                         |
+---------------------+-----------------+------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Yellow/Green        | Bright          |                                    |                                                                       | Device is in boot-loader. See user manual for more information. |
+---------------------+-----------------+------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Slow Red Blink      | Bright          | CAN bus has been lost              |                                                                       |                                                                 |
+---------------------+-----------------+------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Rapid Red Blink     | Dim             | CAN bus never detected since boot  | Magnet is out of range (<25mT or >135mT)                              |                                                                 |
+---------------------+                 +                                    +-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Rapid Yellow Blink  |                 |                                    | Magnet in range with slightly reduced accuracy (25-45mT or 75-135mT)  |                                                                 |
+---------------------+                 +                                    +-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Rapid Green Blink   |                 |                                    | Magnet in range (between 45mT - 75mT)                                 |                                                                 |
+---------------------+-----------------+------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Rapid Red Blink     | Bright          | CAN bus present                    | Magnet is out of range (<25mT or >135mT)                              |                                                                 |
+---------------------+                 +                                    +-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Rapid Yellow Blink  |                 |                                    | Magnet in range with slightly reduced accuracy (25-45mT or 75-135mT)  |                                                                 |
+---------------------+                 +                                    +-----------------------------------------------------------------------+-----------------------------------------------------------------+
| Rapid Green Blink   |                 |                                    | Magnet in range (between 45mT - 75mT)                                 |                                                                 |
+---------------------+-----------------+------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------------------+

CANivore
--------

.. image:: images/status-lights/canivore-status-light.png
  :alt: Table showing canivore status lights
