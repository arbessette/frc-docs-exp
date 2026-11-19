.. include:: <isonum.txt>

Accelerometers - Hardware
=========================


Accelerometers are common sensors used to measure acceleration.

In principle, precise measurements of acceleration can be double-integrated and used to track position (similarly to how the measurement of turn rate from a gyroscope can be integrated to determine heading) - however, in practice, accelerometers that are available within the legal FRC\ |reg| price range are not nearly accurate for this use.  However, accelerometers are still useful for a number of tasks in FRC.

Types of accelerometers
-----------------------


There are three types of accelerometers commonly-used in FRC: single-axis accelerometers, multi-axis accelerometers, and IMUs.

Single-axis accelerometers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Multi-axis accelerometers
~~~~~~~~~~~~~~~~~~~~~~~~~

IMUs (Inertial Measurement Units)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several popular FRC devices (known as "inertial measurement units," or "IMUs") combine both an accelerometer and a gyroscope.  Popular FRC example include:

.. note:: Systemcore scope

   The wording above is retained from the upstream article. Controller-specific
   material and illustrations that do not apply to this site's Systemcore scope
   are excluded rather than relabeled. Use the
   `Systemcore wiring guide <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_
   for the installed revision's connection requirements.

Source: `WPILib upstream, 2f175339
<https://github.com/wpilibsuite/wpilib-docs/blob/2f175339ca2f66bdd8b733eb5832d9ab9291f1c1/source/docs/hardware/sensors/accelerometers-hardware.rst>`_,
`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__.
