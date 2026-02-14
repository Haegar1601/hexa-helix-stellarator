# HexaHelix Phase 1: Geometry Validation Roadmap

**One variable. One question. Does the six-fold stellarator geometry work?**

---

## The Principle

Phase 1 isolates the single most important question: Does N=6 helical symmetry with φ-twist produce superior plasma confinement?

Everything else stays conventional. Standard materials. Standard fuel. Standard heating. Only the geometry is new.

| Component | Phase 1 Choice | Reason |
|-----------|---------------|--------|
| **Geometry** | 6-fold helix, φ = 0.618 | **THIS IS THE TEST** |
| **Coil material** | REBCO / YBCO (commercial HTS) | Proven, available, de-risked |
| **Fuel** | Deuterium-Tritium (D-T) | Lowest ignition threshold, standard |
| **Heating** | ECRH or NBI (conventional) | Proven for stellarators |
| **Wall** | Standard steel/tungsten | Conventional fusion materials |

**What Phase 1 does NOT test:** B-N-C superconductivity, laser resonance heating, aneutronic fuels, direct energy conversion. These are Phase 2–4.

---

## Why This Matters

The fusion landscape in 2026:

- **Helion** reached 150M °C with D-T (Feb 2026), building 50 MW commercial plant
- **CFS** building SPARC tokamak prototype with HTS magnets
- **Type One Energy** developing stellarator with HTS
- **W7-X** (Greifswald) operating the world's most advanced stellarator

All use conventional symmetries. None use six-fold helical symmetry with irrational twist.

**If the geometry alone produces measurably better confinement, that is a publishable result independent of everything else in HexaHelix.**

---

## Step-by-Step Validation Path

### Step 0: Computational (Cost: ~€0 | Timeline: Now)

**Status: In Progress (600+ institutional clones on GitHub)**

| Task | Tool | Output |
|------|------|--------|
| VMEC equilibrium | VMEC code (open source) | Magnetic flux surfaces, rotational transform profile |
| Stability analysis | COBRAVMEC / TERPSICHORE | MHD stability boundaries |
| Coil optimization | FOCUS / SIMSOPT | Buildable coil shapes for N=6 geometry |
| Neoclassical transport | DKES / SFINCS | Particle/energy confinement estimates |
| Comparison baseline | Same codes, W7-X geometry | Quantitative comparison: HexaHelix vs. state-of-the-art |

**Key deliverable:** A peer-reviewable paper comparing predicted confinement of HexaHelix N=6 φ-twist geometry against W7-X and other optimized stellarators using identical simulation tools.

**Who can do this:** Any university plasma physics group with VMEC experience. No hardware needed. No funding needed beyond compute time.

→ *This is the immediate call to action for the 600+ cloners.*

### Step 1: Magnetic Field Verification (Cost: €50–200k | Timeline: 6–12 months)

Build a reduced-scale magnetic field demonstrator. No plasma. No vacuum. Just coils and field measurements.

| Component | Specification | Source |
|-----------|--------------|--------|
| Coils | 6× identical, copper or HTS tape | Commercial winding service |
| Structure | Modular aluminum frame, 60° segments | Standard machining |
| Power supply | DC, matched to coil parameters | Commercial |
| Diagnostics | Hall probe array, 3-axis | Commercial |

**What to measure:**
- Magnetic flux surface topology matches VMEC prediction? ✓/✗
- Field errors at module joints within tolerance? ✓/✗
- Rotational transform profile matches φ-target? ✓/✗

**What to publish:** "Experimental verification of magnetic field topology in a six-fold helical stellarator configuration"

### Step 2: First Plasma (Cost: €2–10M | Timeline: 18–36 months)

A small-scale stellarator with N=6 geometry, operating with hydrogen or deuterium.

| Component | Specification | Notes |
|-----------|--------------|-------|
| Major radius | 0.5–1.0 m | Tabletop-scale for stellarator |
| Magnetic field | 1–3 T | Achievable with copper coils or modest HTS |
| Plasma | Hydrogen or Deuterium | No tritium handling needed |
| Heating | 100–500 kW ECRH | Standard microwave source |
| Vacuum | 10⁻⁶ mbar | Standard vacuum technology |
| Diagnostics | Thomson scattering, Rogowski coils, Langmuir probes | Standard stellarator diagnostics |

**What to measure:**
- Energy confinement time τ_E compared to ISS04 scaling law
- Plasma stability at predicted operating points
- Effect of φ-twist on confinement (vary twist angle, measure τ_E)

**Critical test:** If τ_E at φ = 0.618 is measurably higher than at rational twist angles (e.g., 0.5 or 0.667), Mechanism II (Path Information Erasure) gains experimental support.

**What to publish:** "First plasma results from a six-fold symmetric stellarator with irrational rotational transform"

### Step 3: Performance Optimization (Cost: €5–15M | Timeline: 36–48 months)

Upgrade Step 2 device with HTS coils for higher field, extend pulse length, optimize heating.

| Upgrade | Purpose |
|---------|---------|
| HTS coils (REBCO) | Higher field (5–10 T), longer pulses |
| Additional ECRH power | Higher temperatures |
| Pellet injection | Density control |
| Advanced diagnostics | Detailed transport measurements |

**What to measure:**
- Confinement scaling with field strength
- Beta limits (plasma pressure / magnetic pressure)
- Impurity transport and control
- Steady-state capability

**What to publish:** "High-field operation and confinement optimization in the HexaHelix N=6 stellarator"

---

## What Each Step Proves or Disproves

| Step | If Successful | If Failed |
|------|--------------|-----------|
| **Step 0: VMEC** | Geometry produces good flux surfaces → proceed | Poor flux surfaces → modify geometry or stop |
| **Step 1: Field test** | Real coils match simulation → proceed | Field errors too large → engineering problem, fixable |
| **Step 2: First plasma** | Superior confinement → major result | Average confinement → geometry alone insufficient |
| **Step 3: Optimization** | Scales favorably → path to reactor | Doesn't scale → fundamental limit found |

**Every step is independently publishable. Every step has a clear go/no-go criterion. No step requires betting on all of HexaHelix at once.**

---

## What Phase 1 Does NOT Require

| Not Needed | Why |
|-----------|-----|
| B-N-C materials | Using commercial REBCO/YBCO instead |
| Room-temperature superconductivity | Standard cryogenic HTS is sufficient |
| Aneutronic fuel (p-¹¹B) | D-T or pure D is easier and sufficient for geometry test |
| Laser resonance heating | Conventional ECRH works for this scale |
| Direct energy conversion | Not relevant until fusion conditions achieved |
| €100M+ budget | Phased approach starts at €0 (computation) |
| Large team | Step 0 needs 1–3 people. Step 1 needs 3–5. |

---

## Comparison: HexaHelix Phase 1 vs. Industry

| Project | Approach | Budget | Timeline | Team |
|---------|----------|--------|----------|------|
| **W7-X** | 5-fold stellarator | €1.06B | 19 years | 500+ |
| **CFS SPARC** | Tokamak + HTS | $2B+ | ~8 years | 500+ |
| **Helion Polaris** | FRC, pulsed | $600M+ | 13 years, 7 prototypes | 300+ |
| **HexaHelix Phase 1** | 6-fold stellarator, phased | €0–10M | 1–4 years | 1–10 |

The difference: we test one variable at a time. They build everything at once.

---

## How to Contribute

### If you have VMEC expertise:
Run the Fourier coefficients from our repository through VMEC. Compare confinement prediction against W7-X. Publish with us or independently. The geometry is Open Source.

→ Repository: [github.com/Haegar1601/hexa-helix-stellarator](https://github.com/Haegar1601/hexa-helix-stellarator)

### If you have a coil winding facility:
Six identical coils. One winding pattern. Standard HTS tape. We provide the geometry. You provide the hardware.

### If you have a stellarator or plasma physics lab:
The magnetic field verification (Step 1) can be done as a student project. No plasma, no vacuum, no tritium. Just coils and Hall probes.

### If you have funding interest:
Phase 1 is designed for staged investment. Step 0 costs nothing. Each subsequent step has a clear deliverable and go/no-go criterion before the next investment.

---

## Open Source Commitment

All results from Phase 1 will be published openly:
- Simulation data on GitHub
- Publications as preprints on arXiv
- Hardware designs shared under open license
- No patents. No exclusivity. For humanity.

Prior art is established: GitHub repository with 600+ institutional clones, timestamped commits since 2025.

---

## The Question Phase 1 Answers

> Does six-fold helical symmetry with golden-ratio rotational transform produce measurably superior plasma confinement compared to existing stellarator designs?

If **yes** → Phase 2 tests B-N-C materials in this geometry.
If **no** → We learned something. Published it. Moved on.

Either way: science wins.

---

*"We don't squeeze harder. We arrange smarter."*

**Project:** [github.com/Haegar1601/hexa-helix-stellarator](https://github.com/Haegar1601/hexa-helix-stellarator)
**Methodology:** Twin-Code (Human + AI Collaboration: Claude, Gemini, Grok, GPT)
**License:** Open Source · For Humanity

*Contributors: H. Löhrmann + Twin-Code Synthesis*
*Version: 1.0 · February 2026*
