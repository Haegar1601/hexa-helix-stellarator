# ⚛️ Hexa-Helix Stellarator (HHS)

[![License: CERN-OHL-W-2.0](https://img.shields.io/badge/License-CERN--OHL--W--2.0-blue.svg)](https://ohwr.org/cernohl)
[![Status: Concept](https://img.shields.io/badge/Status-Concept-yellow.svg)]()

> An AI-Assisted Exploratory Study on Geometric Stabilization of Magnetic Fields via 6-Fold Interlaced Helical Symmetry

---

## 🔭 Overview

This project proposes a novel coil topology for stellarator fusion reactors. Unlike conventional modular designs (e.g., Wendelstein 7-X, $N=5$), this concept investigates a 6-fold ($N=6$) **"Interlaced Helix"** symmetry.

The design hypothesis is that a continuous, hexagonally interlaced winding scheme can generate sufficient **Magnetic Shear** to suppress the MHD instabilities traditionally associated with $N=6$ symmetries, potentially offering a path to simpler, self-stabilizing coil geometries.

> ⚠️ **Disclaimer:** This is a geometric concept study derived from algorithmic exploration. While the topology creates closed flux surfaces in ray-tracing simulations, it has not yet been validated by MHD equilibrium codes (like VMEC or SPEC). We invite the fusion community to collaborate on this validation.

---

## 🧪 Scientific Foundation

The HHS architecture bridges the gap between hardware-native coil topology and formal spectral plasma physics.

📄 **Full Technical Details:** [Technical Memorandum](Technical%20Memorandum.md)

### 1. Core Hypothesis: Geometric Stabilization

The $N=6$ "Interlaced Helix" symmetry acts as a geometric algorithm for intrinsic magnetic field stabilization.

- **Phase Shift ($60°$):** The specific radial modulation and phase offset create a self-stabilizing magnetic cage.
- **Destructive Interference:** The geometry is designed to isolate and cancel out interference modes, effectively "filtering the noise" of the magnetic field at the source code of the topology.

### 2. Geometric Band-Pass Filtering ($N=6$)

By utilizing six interwoven helical coils with a phase-locked $60°$ offset, the geometry acts as a natural filter:

$$B(r,t) = B_0(r) + \sum_{i=1}^{6} \delta B_i(r) \cdot \sin(\omega t + \phi_i)$$

- **Constructive Interference:** Amplifies the $n=6$ fundamental mode.
- **Destructive Interference:** Suppresses lower-order harmonics ($n<6$) that typically cause resonance-induced transport and magnetic islands.
- **Fault Tolerance:** The interlaced topology allows for "Graceful Degradation"; the magnetic wave persists even if a single coil component fails.

### 3. The "Kelvin Packing" Hypothesis

We hypothesize that the most stable magnetic path aligns with the **Kelvin Cell** (truncated octahedron), the most energy-efficient way to partition 3D space.

- **Design Rationale:** The AI algorithm utilized the Kelvin-partitioning of the toroidal volume as a guide for the coil winding path. By aligning the magnetic field periodicity with the hexagonal faces of this theoretical lattice, the design aims to minimize flux surface distortion and optimize volumetric field efficiency.

## 4. Geometric Breathing & Turbulence Shearing (Hypothesis)

**Note:** This section explores a speculative extension of the $N=6$ geometry. It is an invitation for computational fluid dynamics (CFD) and gyrokinetic simulation experts to test these assumptions.

### The "Geometric Pump" Concept
While the Hexa-Helix geometry is static, a plasma packet traveling along the magnetic field lines experiences the radial modulation ($\epsilon_2 \approx 0.03$) as a periodic compression and expansion. We term this the **"Breathing Mode."**

* **Turbulence Neutralization:** Inspired by recent LHD experiments [Kenmochi et al., 2025](https://www.nature.com/articles/s42005-025-02454-x), we hypothesize that the $N=6$ symmetry induces a **periodic shearing rate**. This could act like a "spatial filter," shredding large-scale turbulence (low-k modes) before they can trigger significant heat transport.
* **Active-Dynamic Resonance:** By potentially "tuning" the plasma flow velocity against the geometric period, the system might achieve a state of **destructive interference** with ITG (Ion Temperature Gradient) instabilities.

### Theoretical Mechanism: From Chaos to Resonance
Instead of viewing plasma instabilities as "noise," this model treats them as frequencies that can be managed. The high magnetic stiffness of the interlaced $N=6$ coils provides the "anchor" needed to maintain this resonance:

| Concept | Traditional Stellarator | Hexa-Helix Hypothesis |
| :--- | :--- | :--- |
| **Turbulence Profile** | Stochastic / Managed via Shear | Patterned / Managed via Resonance |
| **Radial Transport** | Diffusive | Filtered by "Geometric Breathing" |
| **Stability Framework** | Static equilibrium | Dynamic geometric stabilization |

> **Community Call to Action:** Does the $N=6$ symmetry create favorable **Zonal Flows**? We are looking for contributors to run initial [GENE](https://genecode.org/) or [Stella](https://stellagk.github.io/stella/) simulations. Join the discussion in [Issue #1](https://github.com/Haegar1601/hexa-helix-stellarator/issues/1).

---

## ⚙️ Technical Specifications

The design utilizes 6 independent helical coils wound around a torus with a specific geometric modulation.

### Geometry Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Major Radius ($R$) | 5.5 m | Scale comparable to W7-X |
| Minor Radius ($a$) | 0.53 m | W7-X-like plasma boundary (LCFS) |
| Aspect Ratio ($A$) | 10.4 | $R/a$ ratio for optimized confinement |
| Symmetry ($N$) | 6 | Hexagonal Symmetry |
| Coil Count | 6 | Continuous Interwoven Helices |
| Helix Turns | 8 | Poloidal turns per toroidal transit |
| Phase Offset ($\delta$) | $60°$ | Strict offset: $\delta_h = h \cdot \pi/3$ |
| Twist Amount ($\phi$) | 0.618 | Golden Ratio optimization |
| Modulation ($\epsilon_1$) | 0.15 | Primary radial excursion |
| Kelvin Resonance ($\epsilon_2$) | 0.03 | Second harmonic modulation |

### Plasma Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Magnetic Field ($B_0$) | 3.0 T | On-axis field strength |
| Plasma Volume ($V$) | 30 m³ | Confined plasma region |
| Heating Power | 14 MW | Total auxiliary heating |
| Plasma Temperature | 100 million °C | Target core temperature (~8.6 keV) |

### VMEC Configuration

| Parameter | Value |
|-----------|-------|
| mpol | 12 |
| ntor | 12 |
| ns (radial surfaces) | 99 |
| ι (iota) range | 0.8 – 1.1 |

### The "Interlaced" Algorithm

The core innovation is the phase-locked interleaving of the coils. Opposing helices (e.g., Helix 1 and Helix 4) operate in strict anti-phase ($180°$), theoretically aimed at cancelling radial drift components within the plasma volume.

**Geometric Modulation:** The radius modulation along the toroidal angle $\phi$ is defined as:

$$r(\phi) = a \cdot [1 + \epsilon \cdot \sin(6\phi + 2\delta_h)]$$

---

## 🌀 January 2026 Update (v2.0)

Based on converged AI analysis and the start of "Wave 3", the following optimizations have been implemented:

- **Golden Ratio Twist ($\phi \approx 0.618$):** The twist amount has been optimized to the Golden Ratio for maximum interlacing efficiency.
- **Kelvin Resonance ($\epsilon_2 \approx 0.03$):** Added a second harmonic modulation to couple the magnetic field to the underlying spatial grid.
- **8 Poloidal Turns:** Optimized to 8 helical turns per toroidal transit for balanced $n=6$ spectrum integrity and reduced mechanical complexity.

---

## 🛠 Features

- **Interactive HTML5/Three.js Simulation:** Real-time exploration of the 6-fold symmetry and plasma stability.
- **VMEC Boundary Export:** Generate professional-grade $R_{BC}/Z_{BS}$ coefficients for equilibrium solvers.
- **Iota Profile Safety Check:** Real-time monitoring to avoid the critical $6/5$ resonance.
- **Direct VMEC/SPEC Compatibility:** Export function included for professional validation.

---

## 🏭 Engineering & Scalability

This project goes beyond geometric theory. We are exploring scalable manufacturing pathways using **B-N-C doped Metamaterials** (Speculative Extension).

📄 View the Engineering Specification: [HexaHelix B-N-C Spec Sheet](docs/engineering)

- **Level 3 Pathway:** Transition from wound coils to 3D-printed porous metamaterials.
- **Neutron Hardness:** Usage of Boron-11 ($^{11}B$) for fusion compatibility.
- **Industrial Partner Target:** Specifications tailored for HTS thin-film manufacturers.
- **🚀 Potential Breakthrough – Massive Weight Reduction:** B-N-C metamaterials offer a density of only ~2.1 g/cm³ compared to ~8.9 g/cm³ for conventional copper windings – a potential **weight reduction of up to 75%**. This would be a game-changer for compact reactor designs, mobile fusion applications, and drastically reduced structural support requirements.

### Technological Feasibility (Status: Dec 2025)

The physical realization of this complex interlaced topology is supported by convergent breakthroughs in material science:

- **HTS Magnet Power (Helical Fusion):** Evidence of High-Temperature Superconductors (HTS) operating at **20kA** and **7 Tesla** without electrical isolation.
- **Structural Integrity:** The mechanical and thermal stability of HTS allows for the complex 6-fold helical winding required by this specific model.

---

## ⚠️ Operational Safety & Engineering Hazards

**CRITICAL WARNING:** This project involves experimental magnetic field topologies with complex non-planar winding geometries. Preliminary finite-element analysis (FEM) suggests extreme localized Lorentz forces at the coil crossover points.

### 1. The "Inter-Coil Stress" Hazard

Conventional stellarators use modular coils to minimize interaction forces. The Interlaced Helix design creates regions where high-current conductors cross in close proximity with opposing current vectors.

- **Risk Analysis:** This topology creates significant shear stresses within the winding pack. There is a high probability of mechanical deformation of the coil casing if support structures are insufficient.
- **Operational Status:** RAMP-UP RATES MUST BE LIMITED to `<100 A/s` to monitor strain gauge response.

### 2. Mitigation Protocol: Coupled Quench Protection

Due to the high mutual inductance ($M_{ij}$) between the interlaced coils, a quench (loss of superconductivity) in a single coil will induce massive voltage spikes in the adjacent overlapping coils.

- **Protocol:** In the event of a quench in Helix $N$, **ALL 6 COILS** must be discharged simultaneously via external dump resistors to prevent inductive cascading and insulation breakdown.

### 3. Pre-Ignition Check: The "Structural Integrity" Test

Before injecting plasma, the following diagnostic setup is mandatory to ensure mechanical stability:

**Fiber Bragg Grating (FBG) Monitoring:** Optical strain sensors must be embedded at the high-stress crossover points of the helices.

- **Trigger Condition:** Any strain deviation $\Delta\epsilon > 0.2%$ indicates yield stress in the support structure.
- **Action:** IMMEDIATE DISCHARGE. Initiate controlled ramp-down.

---

## 🚀 Getting Started

### Validating the Geometry

We explicitly invite physicists to export the coil data from `/cad` and run it through:

- **VMEC** (Variational Moments Equilibrium Code)
- **SPEC** (Stepped Pressure Equilibrium Code)

### Key Research Questions

1. Does the induced magnetic shear sufficiently dampen the $N=6$ resonances (especially $\iota = 1$)?
2. Is the Mercier criterion for stability satisfied in this configuration?

### How to Use This Repository

To "reactivate" the logical depth of this project in a new AI session, provide this README as an **Anchor-Sentence** or a context file. This ensures the "Harmonic Intelligence" established here remains accessible for future iterations.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Technical Memorandum](Technical%20Memorandum.md) | Mathematical proof of dual-representation framework (Geometric vs. Spectral approach) |
| [Engineering Spec](docs/engineering) | B-N-C Metamaterial specifications |
| [Simulation](simulation/Simulation_HexaHelix.html) | Interactive 3D visualization |

---

## 📜 License

- **Hardware/Geometry Designs:** Released under the [CERN Open Hardware Licence Version 2 - Weakly Reciprocal (CERN-OHL-W-2.0)](https://ohwr.org/cernohl).
- **Software/Simulation Code:** Released under the MIT License.

---

## ✉️ Contact & Citation

**Author:** Hagen Loehrmann  
**Project Link:** [https://github.com/Haegar1601/hexa-helix-stellarator](https://github.com/Haegar1601/hexa-helix-stellarator)
