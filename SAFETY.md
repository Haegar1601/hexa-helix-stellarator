
## ⚠️ Operational Safety & Engineering Hazards

**CRITICAL WARNING:** This project involves experimental magnetic field topologies (N=6 Interlaced Helix) with complex non-planar winding geometries. Preliminary finite-element analysis (FEM) suggests **extreme localized Lorentz forces** at the coil crossover points.

### 1. The "Inter-Coil Stress" Hazard

Conventional stellarators use modular coils to minimize interaction forces. The **Interlaced Helix** design creates regions where high-current conductors cross in close proximity with opposing current vectors.

* **Risk Analysis:** This topology creates significant shear stresses within the winding pack. There is a high probability of **mechanical deformation** of the coil casing if support structures are insufficient.
* **Potential Consequence:** Delamination of the superconducting insulation or structural fatigue of the coil support shell.
* **Operational Status:** RAMP-UP RATES MUST BE LIMITED to $< 100 \text{ A/s}$ to monitor strain gauge response.

### 2. Mitigation Protocol: Coupled Quench Protection

Due to the high mutual inductance ($M_{ij}$) between the interlaced coils, a quench (loss of superconductivity) in a single coil will induce massive voltage spikes in the adjacent overlapping coils.

* **Required Implementation:** The protection system must utilize **Active Quench Detection** with bridge comparators.
* **Protocol:** In the event of a quench in Helix $N$, **ALL 6 COILS** must be discharged simultaneously via external dump resistors to prevent inductive cascading and insulation breakdown.

### 3. Biological & Environmental Safety

While the topology is biomimetic, standard high-field safety protocols apply. The complex N=6 symmetry creates **stray field gradients** that extend further than in simple toroidal solenoids.

* **Protocol:**
    * **Exclusion Zone:** Personnel with ferro-magnetic implants or pacemakers must remain outside the 5 Gauss line (calculated at approx. $10 \times R_0$).
    * **Projectile Hazard:** Due to the steep field gradients, loose ferromagnetic tools pose a severe projectile risk. Strict "Clean Room" policy applies.

### 4. Pre-Ignition Check: The "Structural Integrity" Test

Before injecting plasma or ramping to full current ($I_{max}$), the following diagnostic setup is mandatory to ensure mechanical stability:

**A. Fiber Bragg Grating (FBG) Monitoring**
Optical strain sensors must be embedded at the high-stress crossover points of the helices.
* **Trigger Condition:** Any strain deviation $\Delta\epsilon > 0.2\%$ indicates yield stress in the support structure.
* **Action:** **IMMEDIATE DISCHARGE.** Initiate controlled ramp-down.

**B. Vacuum Vessel Monitoring**

A Residual Gas Analyzer (RGA) must monitor the cryostat vacuum.
* **Trigger Condition:** A sudden spike in Helium partial pressure indicates a leak in the cooling lines due to mechanical stress.
* **Action:** Emergency Stop to prevent loss of cryostat vacuum (LOVA).

**DISCLAIMER:** This coil topology presents non-trivial mechanical engineering challenges. The authors accept no liability for equipment damage due to Lorentz-force induced structural failure. Proceed with caution during high-current testing.

