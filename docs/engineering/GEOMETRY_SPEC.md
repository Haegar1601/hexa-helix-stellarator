# Hexa-Helix Stellarator Geometry Specification (v1.0)

This document provides the formal mathematical definition of the Hexa-Helix plasma boundary and coil geometry for MHD equilibrium calculations (VMEC, SPEC) and gyrokinetic simulations (GENE, Stella). The specification is designed for direct use in simulation input files.

## 1. Mathematical Foundation

The plasma boundary is approximated as a spectral surface in cylindrical coordinates $(R, \phi, Z)$, using a Fourier series expansion consistent with stellarator symmetry:

$$
R(\theta, \phi) = \sum_{m,n} R_{mn} \cos(m\theta - nN\phi)
$$

$$
Z(\theta, \phi) = \sum_{m,n} Z_{mn} \sin(m\theta - nN\phi)
$$

Where:
- $\theta$: poloidal angle (0 to $2\pi$)
- $\phi$: toroidal angle (0 to $2\pi$)
- $N=6$: number of field periods
- $m$: poloidal mode number
- $n$: toroidal mode number (relative to field period)

The coil centerline follows a modulated helical path:

$$
r(\phi) = a \left[1 + \epsilon_1 \sin(6\phi + 2\delta_h) + \epsilon_2 \sin(6\phi + \phi_{golden})\right]
$$

With $\delta_h = h \cdot \pi / 3$ (60° phase offset, $h=0..5$) and $\phi_{golden} \approx 0.618$ (Golden Ratio twist optimization).

## 2. Reference Parameters (Validation Configuration)

For initial community validation (as specified in [Issue #1](https://github.com/Haegar1601/hexa-helix-stellarator/issues/1)):

| Parameter              | Symbol   | Value    | Unit | Description                          |
|------------------------|----------|----------|------|--------------------------------------|
| Major Radius           | $R_0$    | 1.20     | m    | Central torus radius                 |
| Minor Radius           | $a$      | 0.15     | m    | Average plasma minor radius          |
| Aspect Ratio           | $A$      | 8.0      | -    | $R_0 / a$                            |
| Field Periods          | $N$      | 6        | -    | Toroidal periodicity                 |
| Primary Modulation     | $\epsilon_1$ | 0.15 | -    | Main helical torsion                 |
| Secondary Modulation   | $\epsilon_2$ | 0.03 | -    | Breathing Mode / Kelvin Resonance    |
| Poloidal Turns         | -        | 8        | -    | Per toroidal transit                 |
| Golden Ratio Twist     | $\phi$   | 0.618    | rad  | Phase optimization                   |
| On-Axis Field          | $B_0$    | 1.5–2.5  | T    | Target range for initial runs        |

**Note:** A larger reference scale (R₀ ≈ 5.5 m, a ≈ 0.53 m) is discussed in the main README for reactor-relevant comparisons.

## 3. Fourier Coefficients (Simplified Basis)

The following low-order coefficients approximate the boundary for initial VMEC/SPEC runs. Higher modes can be derived from the coil CAD/files.

| m (poloidal) | n (toroidal, rel. to N) | $R_{mn}$ (cos) | $Z_{mn}$ (sin) | Component Description                  |
|--------------|-------------------------|----------------|----------------|----------------------------------------|
| 0            | 0                       | 1.20           | 0.00           | Major Radius ($R_0$)                   |
| 1            | 0                       | 0.15           | 0.15           | Minor Radius ($a$)                     |
| 1            | 1                       | 0.02           | -0.02          | Primary Helical Torsion ($\epsilon_1$) |
| 0            | 1                       | 0.03           | 0.03           | Breathing Mode ($\epsilon_2$)          |

**VMEC Guidance:** Use `mpol ≥ 12`, `ntor ≥ 12`, `ns ≥ 99`. Global toroidal modes: $n_{global} = n \times N$.

## 4. Python Reconstruction Snippet

```python
import numpy as np
import matplotlib.pyplot as plt

def hexa_helix_surface(theta, phi, R0=1.20, a=0.15, eps1=0.15, eps2=0.03, N=6, phi_golden=0.618*np.pi):
    """Generate approximate plasma boundary points."""
    cos_term = np.cos(theta - N*phi)
    sin_term = np.sin(theta - N*phi)
    
    R = R0 + a * np.cos(theta) + eps1 * a * cos_term + eps2 * a * np.cos(N*phi + phi_golden)
    Z = a * np.sin(theta) + eps1 * a * sin_term + eps2 * a * np.sin(N*phi + phi_golden)
    
    return R, Z

# Example: Plot cross-section at phi = 0
theta = np.linspace(0, 2*np.pi, 200)
R, Z = hexa_helix_surface(theta, phi=0)

plt.figure(figsize=(6,6))
plt.plot(R, Z, 'b')
plt.axis('equal')
plt.title('Hexa-Helix Plasma Boundary Cross-Section (phi=0)')
plt.xlabel('R (m)')
plt.ylabel('Z (m)')
plt.grid(True)
plt.show()
