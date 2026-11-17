Zero to Robot
=============

Build your chassis and mount the components here, then continue to WPILib
for Systemcore wiring and Robot to Motion.

Before starting, review :doc:`../yearly-overview/2027-overview`. Returning
teams can use :doc:`returning` to plan their updates.

Assemble Your Robot
-------------------

Use :doc:`step-1/kitbot-starterbot-assembly` for Kitbot resources and assembly
checks. See :doc:`../assembly/index` for mounting, access, and build records.

Plan the Electronics Layout
---------------------------

Leave room for the battery, main breaker, power distribution, Systemcore,
radio, and motor controllers. Keep connectors accessible and leave space for
cable routing. Use :doc:`step-1/basic-robot-wiring` for general mounting and
wiring practices.

Continue: Wire Systemcore in WPILib
-----------------------------------

With the chassis assembled and the components mounted, continue to the
`Systemcore drivetrain wiring guide in WPILib
<{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_. It covers the controller connections and leads into
Robot to Motion for software setup, configuration, and your first program.

The `wiring guide <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_
links back to our :doc:`physical inspection checklist
<../hardware/hardware-basics/preemptive-troubleshooting>` before powered tests.
After inspection, continue with software setup in WPILib.

.. button-link:: {{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html
   :color: primary

   Continue to Systemcore wiring →

.. toctree::
   :maxdepth: 1
   :caption: Assembly

   step-1/kitbot-starterbot-assembly
   step-1/basic-robot-wiring

.. toctree::
   :maxdepth: 1
   :caption: Returning Teams

   returning
