.. include:: <isonum.txt>

Triangulating Rangefinders
==========================


.. image:: images/triangulating-rangefinders/infrared-proximity-sensor.png
   :alt: Sharp-brand triangulating rangefinder.

Triangulating rangefinders (often called "IR rangefinders," as they commonly function in the infrared wavelength band) are another common type of rangefinder used in FRC\ |reg|. The sensor shown above is a `common Sharp-brand sensor <https://www.sparkfun.com/products/242>`__

Unlike :doc:`LIDAR <lidar>`, triangulating rangefinders do not measure the time between the emission of a pulse and the receiving of a reflection.  Rather, most IR rangefinders work by emitting a constant beam at a slight angle, and measuring the position of the reflected beam.  The closer the point of contact of the reflected beam to the emitter, the closer the object to the sensor.

Using IR rangefinders
---------------------

Caveats
-------


IR rangefinders suffer similar drawbacks to 1D LIDAR sensors - they are very sensitive to the reflectivity of the target in the wavelength of the emitted laser.

Additionally, while IR rangefinders tend to offer better resolution than LIDAR sensors when measuring at short distances, they are also usually more sensitive to differences in orientation of the target, *especially* if the target is highly-reflective (such as a mirror).

.. note:: Systemcore scope

   The wording above is retained from the upstream article. Controller-specific
   material and illustrations that do not apply to this site's Systemcore scope
   are excluded rather than relabeled. Use the
   `Systemcore wiring guide <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_
   for the installed revision's connection requirements.

Source: `WPILib upstream, 2f175339
<https://github.com/wpilibsuite/wpilib-docs/blob/2f175339ca2f66bdd8b733eb5832d9ab9291f1c1/source/docs/hardware/sensors/triangulating-rangefinders.rst>`_,
`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__.
