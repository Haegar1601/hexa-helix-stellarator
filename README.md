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

Current theoretical models suggests that N=6 symmetry combined with specific resonance frequencies might couple to the microscopic lattice structure of spacetime (Quantum Vacuum Geometry). Therefore, operation at constant resonance frequencies is strictly discouraged to avoid constructive interference with the vacuum metric.

---

## 🧬 The Origin Story: AI-Assisted Discovery

This topology is not the result of a traditional physics optimizer. Instead, it emerged from a computational dialogue between a **Software Engineer** and two state-of-the-art AI models (**Google Gemini 3** and **Anthropic Claude Opus 4.5**).

The goal was to map biological redundancy principles (inspired by hypothetical **Hexa-Helix DNA structures**) onto a toroidal magnetic field. Both models independently converged on this specific interlaced geometry as a method to achieve **Geometric Mode Cancellation** of error fields.

---

## ⚙️ Technical Specifications

The design utilizes 6 independent helical coils wound around a torus with a specific "Breathing Mode" modulation.

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Major Radius ($R_0$)** | 5.5 m | Scale comparable to W7-X |
| **Minor Radius ($a$)** | 1.5 m | |
| **Symmetry ($N$)** | 6 | Hexagonal Symmetry |
| **Coil Count** | 6 | Continuous Helical Coils |
| **Turns per Transit** | 8 | Poloidal turns per toroidal transit |
| **Phase Offset ($\delta_h$)** | $60^{\circ}$ | Strict offset: $\delta_h = (h/6) \cdot 2\pi$ |
| **Modulation ($\epsilon$)** | 0.15 | "Breathing Mode" amplitude |

### The "Interlaced" Algorithm
The core innovation is the phase-locked interleaving of the coils. Opposing helices (e.g., Helix 1 and Helix 4) operate in strict anti-phase ($180^{\circ}$), theoretically leading to a cancellation of radial drift components.

The radius modulation is defined as:
$$r(t) = a \cdot [1 + \epsilon \cdot \sin(6\phi + 2\delta_h)]$$

---

## 📸 Visualization

*(Please run the simulation in `/simulation` to see the 3D structure)*

The simulation reveals:
1.  **Closed Topology:** Formation of a toroidal cage without visible loss cones.
2.  **Shear:** Visual confirmation of high torsion in the field lines.
3.  **Destructive Nodes:** Regions where field components from opposing helices cancel out.

---

## 📂 Repository Structure

* `/paper`: Contains the Whitepaper "Geometric Stabilization via 6-Fold Interlaced Symmetry" (PDF).
* `/simulation`: The interactive 3D Web-Simulation (HTML/JS/Three.js).
* `/cad`: 3D Models of the coil geometry (STEP/STL files) for import into physics codes. *(Add your files here)*
* `/src`: Generation scripts for the geometry.

---

## 🚀 Getting Started

### Running the Web Simulation
1.  Navigate to the `/simulation` folder.
2.  Open `index.html` in any modern web browser.
3.  Use the controls to rotate the torus and toggle the "Plasma" view to see the flux surface estimation.

### Validating the Geometry
We explicitly invite physicists to export the coil data from `/cad` and run it through:
* **VMEC** (Variational Moments Equilibrium Code)
* **SPEC** (Stepped Pressure Equilibrium Code)

**Key Research Questions:**
* Does the induced magnetic shear sufficiently dampen the $N=6$ resonances (especially $\iota = 1$)?
* Is the Mercier criterion for stability satisfied?

---

## 📜 License

To ensure this concept remains accessible for scientific advancement, this project is released under Open Source licenses:

* **Hardware/Geometry Designs:** Released under the **CERN Open Hardware Licence Version 2 - Weakly Reciprocal (CERN-OHL-W-2.0)**.
* **Software/Simulation Code:** Released under the **MIT License**.

---

## ✉️ Contact & Citation

If you use this topology in your research, please cite this repository.

**Author:** Hagen Loehrmann
**Project Link:** https://github.com/Haegar1601/hexa-helix-stellarator

*Created with the assistance of Gemini and Claude AI.*
