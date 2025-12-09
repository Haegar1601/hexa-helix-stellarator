# HexaHelix Stellarator: A 6-Fold Interlaced Coil Topology

![License: CERN-OHL-W-2.0](https://img.shields.io/badge/License-CERN--OHL--W--2.0-blue.svg)
![Status: Concept](https://img.shields.io/badge/Status-Geometric%20Concept-orange.svg)
![Symmetry: N=6](https://img.shields.io/badge/Symmetry-N%3D6-green.svg)

> **An exploratory study on geometric stabilization of magnetic fields via hexagonally interlaced helical symmetry.**

---

## 🔭 Overview

This project proposes a novel coil topology for stellarator fusion reactors. Unlike conventional modular designs (e.g., Wendelstein 7-X, $N=5$), this concept investigates a **6-fold ($N=6$) "Interlaced Helix" symmetry**.

The design hypothesis is that a continuous, hexagonally interlaced winding scheme can generate sufficient **Magnetic Shear** to suppress the MHD instabilities traditionally associated with $N=6$ symmetries, potentially offering a path to simpler, self-stabilizing coil geometries.

**⚠️ Disclaimer:** This is a geometric concept study derived from algorithmic exploration. While the topology creates closed flux surfaces in ray-tracing simulations, it has **not yet been validated** by MHD equilibrium codes (like VMEC or SPEC). We invite the fusion community to collaborate on this validation.

## 🧬 Design Methodology: AI-Assisted Discovery

This topology is not the result of a traditional physics optimizer. Instead, it emerged from a computational dialogue between a Software Engineer and two state-of-the-art AI models.

The goal was to map biological redundancy principles onto a toroidal magnetic field. Both models independently converged on this specific interlaced geometry.

### The "Kelvin Packing" Hypothesis

A key factor in the topology's selection was the correlation with the **Kelvin Cell structure** (Tetrakaidecahedron). Lord Kelvin proposed this bitruncated cubic honeycomb as the optimal partition of 3D space with minimal surface area.



* **Design Rationale:** The AI algorithm utilized the Kelvin-partitioning of the toroidal volume as a guide for the coil winding path. By aligning the magnetic field periodicity with the hexagonal faces of this theoretical lattice, the design aims to **minimize flux surface distortion** and optimize volumetric field efficiency.
* **Note:** This utilizes the Kelvin Cell purely as a geometric basis for packing efficiency, drawing on the structural stability inherent in these minimal-surface lattices.

## ⚙️ Technical Specifications

The design utilizes 6 independent helical coils wound around a torus with a specific geometric modulation.

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Major Radius ($R_0$)** | 5.5 m | Scale comparable to W7-X |
| **Minor Radius ($a$)** | 1.5 m | |
| **Symmetry ($N$)** | 6 | Hexagonal Symmetry |
| **Coil Count** | 6 | Continuous Helical Coils |
| **Turns per Transit** | 8 | Poloidal turns per toroidal transit |
| **Phase Offset ($\delta_h$)** | $60^{\circ}$ | Strict offset: $\delta_h = (h/6) \cdot 2\pi$ |
| **Modulation ($\epsilon$)** | 0.15 | Amplitude of radial excursion |

### The "Interlaced" Algorithm

The core innovation is the phase-locked interleaving of the coils. Opposing helices (e.g., Helix 1 and Helix 4) operate in strict anti-phase ($180^{\circ}$), theoretically aimed at cancelling radial drift components within the plasma volume.

**Geometric Modulation**
The radius modulation along the toroidal angle $\phi$ is defined as:
$$r(\phi) = a \cdot [1 + \epsilon \cdot \sin(6\phi + 2\delta_h)]$$

## ⚠️ Operational Safety & Engineering Hazards

**CRITICAL WARNING:** This project involves experimental magnetic field topologies with complex non-planar winding geometries. Preliminary finite-element analysis (FEM) suggests **extreme localized Lorentz forces** at the coil crossover points.

### 1. The "Inter-Coil Stress" Hazard

Conventional stellarators use modular coils to minimize interaction forces. The **Interlaced Helix** design creates regions where high-current conductors cross in close proximity with opposing current vectors.

* **Risk Analysis:** This topology creates significant shear stresses within the winding pack. There is a high probability of **mechanical deformation** of the coil casing if support structures are insufficient.
* **Operational Status:** RAMP-UP RATES MUST BE LIMITED to $< 100 \text{ A/s}$ to monitor strain gauge response.

### 2. Mitigation Protocol: Coupled Quench Protection

Due to the high mutual inductance ($M_{ij}$) between the interlaced coils, a quench (loss of superconductivity) in a single coil will induce massive voltage spikes in the adjacent overlapping coils.

* **Protocol:** In the event of a quench in Helix $N$, **ALL 6 COILS** must be discharged simultaneously via external dump resistors to prevent inductive cascading and insulation breakdown.

### 3. Pre-Ignition Check: The "Structural Integrity" Test

Before injecting plasma, the following diagnostic setup is mandatory to ensure mechanical stability:

**Fiber Bragg Grating (FBG) Monitoring**
Optical strain sensors must be embedded at the high-stress crossover points of the helices.
* **Trigger Condition:** Any strain deviation $\Delta\epsilon > 0.2\%$ indicates yield stress in the support structure.
* **Action:** **IMMEDIATE DISCHARGE.** Initiate controlled ramp-down.

## 🚀 Getting Started

**Validating the Geometry**

We explicitly invite physicists to export the coil data from `/cad` and run it through:
* **VMEC** (Variational Moments Equilibrium Code)
* **SPEC** (Stepped Pressure Equilibrium Code)

**Key Research Questions:**
1.  Does the induced magnetic shear sufficiently dampen the $N=6$ resonances (especially $\iota=1$)?
2.  Is the Mercier criterion for stability satisfied in this configuration?

## 📜 License

* **Hardware/Geometry Designs:** Released under the CERN Open Hardware Licence Version 2 - Weakly Reciprocal (CERN-OHL-W-2.0).
* **Software/Simulation Code:** Released under the MIT License.

## ✉️ Contact & Citation

**Author:** Hagen Loehrmann
**Project Link:** [https://github.com/Haegar1601/hexa-helix-stellarator](https://github.com/Haegar1601/hexa-helix-stellarator)
