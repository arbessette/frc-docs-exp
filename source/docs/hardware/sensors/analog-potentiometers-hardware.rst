.. include:: <isonum.txt>

Analog Potentiometers - Hardware
================================


.. note:: This section covers analog potentiometer hardware.  For a software guide to analog potentiometers, see `Analog Potentiometers - Software <{{ wpilib_docs_url }}docs/software/hardware-apis/sensors/analog-potentiometers-software.html#analog-potentiometers-software>`__.

.. warning:: Potentiometers generally have a mechanically-limited travel range.  Users should be careful that their mechanisms do not turn their potentiometers past their maximum travel, as this will damage or destroy the potentiometer.

Apart from :doc:`quadrature encoders <encoders-hardware>`, another common way of measuring rotation is with analog potentiometers.  A potentiometer is simply a variable resistor - as the shaft of the potentiometer turns, the resistance changes (usually linearly).  Placing this resistor in a `voltage divider <https://en.wikipedia.org/wiki/Voltage_divider>`__ allows the user to easily measure the resistance by measuring the voltage across the potentiometer, which can then be used to calculate the rotational position of the shaft.

Wiring an analog potentiometer
------------------------------

Footnotes
---------


The way this actually works is generally by having the shaft control the position of a contact along a resistive "wiper" of fixed length along which the current flows - the resistance is proportional to the length of wiper between the contact and the end of the wiper.

.. note:: Systemcore scope

   The wording above is retained from the upstream article. Controller-specific
   material and illustrations that do not apply to this site's Systemcore scope
   are excluded rather than relabeled. Use the
   `Systemcore wiring guide <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_
   for the installed revision's connection requirements.

Source: `WPILib upstream, 2f175339
<https://github.com/wpilibsuite/wpilib-docs/blob/2f175339ca2f66bdd8b733eb5832d9ab9291f1c1/source/docs/hardware/sensors/analog-potentiometers-hardware.rst>`_,
`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__.
