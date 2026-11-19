.. include:: <isonum.txt>

Robot Preemptive Troubleshooting
================================


.. note::

    In *FIRST*\ |reg| Robotics Competition, robots take a lot of stress while driving around the field. It is important to make sure that connections are tight, parts are bolted securely in place and that everything is mounted so that a robot bouncing around the field does not break.

Check Battery Connections
-------------------------

The tape that should be covering the battery connection in these examples has been removed to illustrate what is going on. On your robots, the connections should be covered.

Wiggle battery harness connector. Often these are loose because the screws loosen, or sometimes the crimp is not completely closed.  You will only catch the really bad ones though because often the electrical tape stiffens the connection to a point where it feels stiff. Using a voltmeter or Battery Beak will help with this.

Securing the Battery to the Robot
---------------------------------


.. image:: images/preemptive-troubleshooting/preCheckConnecc.png
   :alt: Disconnected battery of a robot mid match.
   :width: 350

In almost every event we see at least one robot where a not properly secured battery connector (the large Anderson) comes apart and disconnects power from the robot. This has happened in championship matches on the Einstein and everywhere else. Its an easy to ensure that this doesn't happen to you by securing the two connectors by wrapping a tie wrap around the connection. 10 or 12 tie wraps for the peace of mind during an event is not a high price to pay to guarantee that you will not have the problem of this robot from an actual event after a bumpy ride over a defense. Also, secure your battery to the chassis with hook and loop tape or another method, especially in games with rough defense, obstacles, or climbing.

Securing the Battery Connector & Main Power Leads
-------------------------------------------------


A loose robot-side battery connector (the large Anderson SB) can allow the main power leads to be tugged when the battery is replaced. If the main power leads are loose, that "tug" can get all the way back to the crimp lugs attached to the 120 Amp Circuit Breaker or Power Distribution Panel (PDP), bend the lug, and over time cause the lug end to break from fatigue. Putting a couple tie wraps attaching the main power leads to the chassis and bolting down the robot-side battery connector can prevent this, as well as make it easier to connect the battery.

Main Breaker (120 Amp Circuit Breaker)
--------------------------------------


.. note:: Ensure nuts are tightened firmly and the breaker is attached to a rigid element.

The original nut has a star locking feature, which can wear out over time: these may require checking every few matches, especially if your robot-side battery connector is not attached to the chassis.

The nut is normally a relatively uncommon 1/4-28 thread: ensure this is correct if the nut is replaced.

Because the metal stud is just molded into the case, every once in awhile you may break off the stud. Don't stress, just replace the assembly.

When subjected to multiple competition seasons, the Main Breaker is susceptible to fatigue damage from vibration and use, and can start opening under impact. Each time the thermal fuse function is triggered, it can become progressively easier to trip. Many veteran teams start each season with a fresh main breaker, and carry spares.

Power Distribution Panel (PDP)
------------------------------


.. image:: images/preemptive-troubleshooting/pdp-bolts.png
  :alt: Battery terminals on the PDP.
  :width: 500

Make sure that split washers were placed under the PDP screws, but it is not easy to visually confirm, and sometimes you can’t.  You can check by removing the case.
Also if you squeeze the red and black wires together, sometimes you can catch the really lose connections.

Tug Testing
-----------

.. image:: images/preemptive-troubleshooting/preCheckTug-2.png
  :alt: Tug test on the connectors at the bottom of the PDP.
  :width: 350

Look for possible or impending shorts with Weidmuller connections that are close to each other, and have too-long wire-lead lengths (wires that are stripped extra long).

Spade connectors can also fail due to improper crimps, so tug-test those as well.

Blade Fuses
-----------


Be sure to place the 20A fuse (yellow) on the left and the 10A fuse (red) on the right.

.. image:: images/preemptive-troubleshooting/pdp-blade-fuses.svg
   :alt: PDP diagram showing the bottom connections and fuses.
   :width: 600

.. image:: images/preemptive-troubleshooting/blade-fuses.png
   :alt: Bottom of the PDP focusing on the 20A and 10A fuses.
   :width: 600

.. warning:: Take care to ensure fuses are fully seated into the fuse holders. The fuses should descend at least as far as the figure below (different brand fuses have different lead lengths). It should be nearly impossible to remove the fuse with bare hands (without the use of pliers). If this is not properly done, the robot/radio may exhibit intermittent connectivity issues.

If you can remove the blade fuses by hand then they are not in completely. Make sure that they are completely seated in the PDP so that they don't pop out during robot operation.

Ethernet Cable
--------------

Loose Cables
------------


Cables must be tightened down, particularly the radio power and ethernet cable.

Ethernet cable is also pretty heavy, if it’s allowed to swing freely, the plastic clip may not be enough to hold the ethernet pin connectors in circuit.

Reproducing Problems in the Pit
-------------------------------

When doing this test it’s important to be ethernet tethered and not USB tethered, otherwise you are not testing all of the critical paths.

Handy Tools
-----------


.. image:: images/preemptive-troubleshooting/tools.png
  :alt: A Wago screwdriver and flashlight.
  :width: 500

There never seems to be enough light inside robots, at least not enough to scrutinize the critical connection points, so consider using a handheld LED flashlight to inspect the connections on your robot. They're available from home depot or any hardware/automotive store.

A WAGO tool is nice tool for redoing Weidmuller connections with stranded wires.  Often I’ll do one to show the team, and then have them do the rest using the WAGO tool to press down the white-plunger while they insert the stranded wire.  The angle of the WAGO tool makes this particularly helpful.

.. note:: Systemcore scope

   The wording above is retained from the upstream article. Controller-specific
   material and illustrations that do not apply to this site's Systemcore scope
   are excluded rather than relabeled. Use the
   `Systemcore wiring guide <{{ wpilib_docs_url }}docs/zero-to-robot/systemcore-wiring.html>`_
   for the installed revision's connection requirements.

Source: `WPILib upstream, 2f175339
<https://github.com/wpilibsuite/wpilib-docs/blob/2f175339ca2f66bdd8b733eb5832d9ab9291f1c1/source/docs/hardware/hardware-basics/preemptive-troubleshooting.rst>`_,
`CC BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__.
