.. include:: <isonum.txt>

Serial Buses
============

Both the digital and analog inputs are highly limited in the amount of data that can be sent over them.  Serial buses allow users to make use of far more-robust and higher-bandwidth communications protocols with sensors that collect large amounts of data, such as inertial measurement units (IMUs) or 2D LIDAR sensors.

Types of supported serial buses
-------------------------------

- `I2C`_
- `USB Host`_
- `CAN Bus`_

I2C
---

To communicate to peripheral devices over :external+wpilib:term:`I2C`, each pin should be wired to its corresponding pin on the device.  I2C allows users to wire a "chain" of slave devices to a single port, so long as those devices have separate IDs set.

USB Client
----------

USB Host
--------

CAN Bus
-------

One of the advantages of using the CAN bus protocol is that devices can be daisy-chained, as shown below. If power is removed from any device in the chain, data signals will still be able to reach all devices in the chain.

.. image:: images/serial-buses/can-bus-talon-srx-chain.png
   :alt: A CAN bus topology between motor controllers.

Several sensors primarily use the CAN bus. Some examples include:

- `CAN Based Time-of-Flight Range/Distance Sensor from playingwithfusion.com <https://www.playingwithfusion.com/productview.php?pdid=96&catid=1009>`__
- TalonSRX-based sensors, such as the `Gadgeteer Pigeon IMU  <https://store.ctr-electronics.com/gadgeteer-pigeon-imu/>`__ and the `SRX MAG Encoder <https://store.ctr-electronics.com/srx-mag-encoder/>`__
- `CANifier <https://store.ctr-electronics.com/canifier/>`__
- Power monitoring sensors built into the :ref:`CTRE Power Distribution Panel (PDP) <docs/controls-overviews/control-system-hardware:CTRE Power Distribution Panel>` and the :ref:`REV Power Distribution Hub (PDH) <docs/controls-overviews/control-system-hardware:REV Power Distribution Hub>`

More information about using devices connected to the CAN bus can be found in the article about `using can devices <{{ wpilib_docs_url }}docs/software/can-devices/using-can-devices.html#using-can-devices>`__.

.. note:: Systemcore scope

   The wording above is retained from the upstream article. Controller-specific
   material and illustrations that do not apply to this site's Systemcore scope
   are excluded rather than relabeled. Use the
   `Systemcore wiring guide <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_
   for the installed revision's connection requirements.

Source: `WPILib upstream, 2f175339
<https://github.com/wpilibsuite/wpilib-docs/blob/2f175339ca2f66bdd8b733eb5832d9ab9291f1c1/source/docs/hardware/sensors/serial-buses.rst>`_,
`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__.
