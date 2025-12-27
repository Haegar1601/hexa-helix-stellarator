import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# --- CONFIGURATION (optimized for stable flux surfaces) ---
R0 = 1.0                        # Major radius of the torus
B0 = 1.0                        # Strength of the main toroidal field
N_COILS = 6                     # Your N=6 Hexa-Helix symmetry
AMPLITUDE_BASE = 0.001          # Very small perturbation amplitude (0.1% – sweet spot)
SHEAR_STRENGTH = 0.5             # Mild radial shear (amplitude decreases with radius)
LOOPS = 300                     # Number of toroidal transits for high precision

def magnetic_field(state, phi):
    """
    Magnetic field model incorporating your N=6 helical perturbation + radial shear.
    """
    R, Z = state
    
    # Local coordinates
    r_local = np.sqrt((R - R0)**2 + Z**2)
    theta = np.arctan2(Z, R - R0)
    
    # Toroidal main field (1/R fall-off)
    B_phi = B0 * R0 / R
    
    # Effective amplitude with radial shear (weaker near the magnetic axis)
    amplitude = AMPLITUDE_BASE * (1 - SHEAR_STRENGTH * (R - R0) / 0.3)
    amplitude = max(amplitude, 0)  # Prevent negative values
    
    # Your N=6 helical phase (poloidal multipolarity l=2, typical for stellarators)
    helix_phase = N_COILS * phi - 2 * theta
    
    B_R = amplitude * np.sin(helix_phase)
    B_Z = amplitude * np.cos(helix_phase)
    
    # Field-line tracing equations
    dR_dphi = R * (B_R / B_phi)
    dZ_dphi = R * (B_Z / B_phi)
    
    return [dR_dphi, dZ_dphi]

# --- INITIALIZATION ---
start_radii = np.linspace(R0 + 0.02, R0 + 0.25, 10)  # 10 nested flux surfaces
phi_span = np.linspace(0, 2 * np.pi * LOOPS, LOOPS * 1000)  # High-resolution phi grid

# Plot setup
plt.figure(figsize=(10, 10))
plt.title(f"Poincaré Plot: N={N_COILS} Hexa-Helix with Radial Shear (base ε={AMPLITUDE_BASE})", 
          fontsize=14)
plt.xlabel("R (major radius)")
plt.ylabel("Z (vertical position)")
plt.grid(True, alpha=0.3)

colors = plt.cm.viridis(np.linspace(0, 1, len(start_radii)))

print("Starting high-precision simulation...")

# --- SIMULATION ---
for i, r_start in enumerate(start_radii):
    y0 = [r_start, 0.0]  # Starting point on the outboard midplane
    
    # High-precision integration
    solution = odeint(magnetic_field, y0, phi_span, rtol=1e-10, atol=1e-12)
    
    R_points = solution[:, 0]
    Z_points = solution[:, 1]
    
    # Exact Poincaré section: sample only at full toroidal turns
    steps_per_loop = len(phi_span) // LOOPS
    poincare_indices = np.arange(0, len(phi_span), steps_per_loop)
    
    plt.plot(R_points[poincare_indices], Z_points[poincare_indices], 
             'o', markersize=5, color=colors[i], alpha=0.8,
             label=f'Surface {i+1}' if i < 3 else "")
    
    # Statistics for verification
    std_R = np.std(R_points[poincare_indices])
    std_Z = np.std(Z_points[poincare_indices])
    unique_points = len(np.unique(np.round(R_points[poincare_indices], decimals=8)))
    
    print(f"  Surface {i+1}: std_R = {std_R:.2e}, std_Z = {std_Z:.2e}, "
          f"unique Poincaré points = {unique_points}")

# Reference point
plt.plot(R0, 0, 'rx', markersize=12, markeredgewidth=3, label='Magnetic Axis')
plt.axis('equal')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
