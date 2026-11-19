# Upstream hardware wording review — November 19, 2026

Source: [official WPILib main at 2f175339ca2f66bdd8b733eb5832d9ab9291f1c1](https://github.com/wpilibsuite/wpilib-docs/tree/2f175339ca2f66bdd8b733eb5832d9ab9291f1c1).
The earlier stable-site comparison and paraphrased restoration are superseded.

Exception requested afterward: Zero to Robot Step 2 uses the specific
[stable Kitbot wiring article](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
at `step-1/intro-to-frc-robot-wiring.rst`, with retained wording and the same
explicit Systemcore exclusions. The general `basic-robot-wiring.rst` reference
remains available through article links but is not duplicated in navigation.

The 16 recopied hardware and wiring articles retain the upstream prose.
Changes are limited to native reStructuredText headings, equivalent link/role
markup, cross-site software links, and separately labeled Systemcore scope
notes and source credits. Source spelling and wording are retained.

## Exclusions

This is not a byte-for-byte copy of every upstream file. The Systemcore-only
scope excludes old-controller sections, instructions, and illustrations rather
than rewriting them as Systemcore procedures. Source paragraphs containing
legacy controller assumptions are omitted as whole blocks. Missing local or
controller-specific illustrations are not replaced with invented diagrams.

The upstream digital pull-down/signal-to-power procedure is excluded because
FIRST's later updated-hardware announcement specifies pull-ups for beta and
later units. That exception is identified in the digital-input article.

The prior reviewed exclusions of force/drop testing and blanket security-disable
instructions remain. Software-owned setup sections stay in WPILib.

The status-light article was restored to its pre-review state to preserve the
manufacturer-verified corrections already present before this task. It is not
claimed to be a verbatim copy of upstream main.

The Hardware Basics, Hardware Tutorials, and Sensors navigation follows the
upstream groups. No software sections were added. Nothing was committed or
pushed in this review.

Validation: checked 133 retained prose paragraphs against the pinned source
with link/role markup normalized; no paraphrases were found. The strict Sphinx
HTML build passed with warnings treated as errors. All referenced local image
files exist. Unsupported TODO directives were rendered as notes without
changing their wording; empty illustration tabs were removed after excluding
the legacy diagrams. The local preview was refreshed.
