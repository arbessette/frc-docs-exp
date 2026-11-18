FIRST Robotics Competition Documentation
========================================

.. rubric:: Find the Right Documentation

.. grid:: 1 1 3 3
   :gutter: 3

   .. grid-item-card:: WPILib: Systemcore and Robot Programming
      :link: {{ wpilib_docs_url }}docs/zero-to-robot/introduction.html
      :link-type: url
      :class-card: sw-card-shared

      Set up Systemcore, write robot code, and learn how to test and debug it.
      You'll also find links to hardware guides and vendor documentation.

      +++
      Browse WPILib Docs →

   .. grid-item-card:: FTC Docs: Hardware and Setup and more
      :link: https://ftc-docs.firstinspires.org/en/latest/
      :link-type: url
      :class-card: sw-card-ftc

      Find FTC assembly and wiring guides, plus setup and programming help
      for the REV control system. For Systemcore programming, use WPILib docs.

      +++
      Browse FTC Docs →

   .. grid-item-card:: FRC Docs: Team, Hardware, and Vendor Resources
      :link: docs/hardware/index
      :link-type: doc
      :class-card: sw-card-frc

      Find FRC hardware guides, assembly and wiring instructions, vendor
      links, and team resources in FRC Docs. **You are here.**

      +++
      Browse FRC Docs →

Build, wire, and prepare your robot.

.. container:: frc-home-start

   .. rubric:: Start Here

   .. grid:: 1 1 2 2
      :gutter: 3

      .. grid-item::
         :columns: 12 12 8 8

         .. rubric:: Build your robot. Get it driving.

         Start with chassis assembly and electronics mounting. Follow the four
         steps below through wiring, inspection, and your first program.

         .. button-ref:: docs/zero-to-robot/index
            :color: primary

            Start building →

         **Returning this season?** Review the
         :doc:`2027 robot overview <docs/yearly-overview/2027-overview>`
         before updating your hardware.

      .. grid-item::
         :columns: 12 12 4 4

         .. figure:: docs/controls-overviews/images/control-system-hardware/systemcore.png
            :alt: Limelight Systemcore robot controller.
            :width: 260

            Systemcore controller. Photo courtesy of Limelight.

.. rubric:: From Parts to Driving

.. grid:: 1 2 4 4
   :gutter: 2

   .. grid-item-card:: 01 · Build
      :link: docs/zero-to-robot/step-1/kitbot-starterbot-assembly
      :link-type: doc
      :class-card: frc-home-step

      Assemble the drivetrain and plan where the electronics will go.

   .. grid-item-card:: 02 · Wire
      :link: {{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html
      :link-type: url
      :class-card: frc-home-step

      Connect Systemcore and all electronics.

   .. grid-item-card:: 03 · Inspect
      :link: docs/hardware/hardware-basics/preemptive-troubleshooting
      :link-type: doc
      :class-card: frc-home-step

      Check mounting and wiring before powereing on

   .. grid-item-card:: 04 · Program →
      :link: {{ wpilib_docs_url }}docs/zero-to-robot/introduction.html
      :link-type: url
      :class-card: frc-home-step frc-home-program

      Install software and run your first drivetrain program in WPILib.

Systemcore wiring and software setup are covered in WPILib Docs. Follow the
connections for your hardware revision.

.. rubric:: Find a Reference

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: Hardware
      :link: docs/hardware/index
      :link-type: doc
      :class-card: frc-home-reference

      Find control-system components, motors, sensors, and pneumatics.

   .. grid-item-card:: Wiring Practices
      :link: docs/hardware/hardware-basics/wiring-best-practices
      :link-type: doc
      :class-card: frc-home-reference

      Route cables, add strain relief, and keep connections easy to inspect.

   .. grid-item-card:: Status Lights
      :link: docs/hardware/hardware-basics/status-lights-ref
      :link-type: doc
      :class-card: frc-home-reference

      Check component indicators when tracking down a problem.

   .. grid-item-card:: Assembly and Testing
      :link: docs/assembly/index
      :link-type: doc
      :class-card: frc-home-reference

      Plan access, document the build, and keep a test record.

   .. grid-item-card:: Competition Preparation
      :link: docs/competition/index
      :link-type: doc
      :class-card: frc-home-reference

      Prepare your robot, tools, spare parts, and pit for an event.

   .. grid-item-card:: Vendors and Resources
      :link: docs/vendors/index
      :link-type: doc
      :class-card: frc-home-reference

      Find manufacturer instructions for the components on your robot.

For previous FRC control systems, use the
`2026 WPILib documentation <https://docs.wpilib.org/en/stable/>`_.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Zero to Robot

   docs/yearly-overview/2027-overview
   docs/zero-to-robot/index

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Robot References

   docs/hardware/index
   docs/vendors/index
   docs/assembly/index
   docs/competition/index

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Resources

   docs/resources/index
   about
