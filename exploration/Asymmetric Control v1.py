import numpy as np
from scipy.integrate import odeint

# --- OPTIMIZED CONFIG ---
R0 = 1.0
B0 = 1.0
N_COILS = 6
AMPLITUDE_BASE = 0.0015      # Fairer Sweet Spot nach Normalisierung
SHEAR_STRENGTH = 0.7         # Stärkerer radialer Shear
LOOPS = 400                  # Hohe Präzision

PHI_RATIO = (1 + np.sqrt(5)) / 2
PHI_MOD_STRENGTH = 0.06      # Dynamische φ-Modulation

# Fein getunte Asymmetrie
PHASE_JITTER = np.array([0, 1.2, -0.9, 1.8, -1.0, 0.7]) * (np.pi / 180)
AMPLITUDE_MOD = np.array([1.0, 0.98, 1.03, 0.97, 1.04, 0.99])

def magnetic_field_optimized(state, phi, use_asymmetry=True):
    R, Z = state
    theta = np.arctan2(Z, R - R0)
    B_phi = B0 * R0 / R
    
    # Exponentieller Shear – stärker nahe Axis
    shear_factor = SHEAR_STRENGTH * np.exp(-5 * max(0, (R - R0 - 0.02)))
    amplitude = AMPLITUDE_BASE * (1 - shear_factor)
    amplitude = max(amplitude, 1e-6)
    
    B_R = 0.0
    B_Z = 0.0
    
    for coil in range(N_COILS):
        base_phase = coil * (2 * np.pi / N_COILS)
        effective_phase = base_phase + (PHASE_JITTER[coil] if use_asymmetry else 0)
        
        coil_amplitude = amplitude * (AMPLITUDE_MOD[coil] if use_asymmetry else 1.0)
        
        if use_asymmetry:
            # Dynamische φ-Modulation (stärker im Edge)
            phi_mod = 1 + PHI_MOD_STRENGTH * np.sin(PHI_RATIO * phi + coil * np.pi / 3) * (R - R0)**1.5
            coil_amplitude *= phi_mod
        
        helix_phase = N_COILS * phi - 2 * theta + effective_phase
        
        B_R += coil_amplitude * np.sin(helix_phase) / N_COILS
        B_Z += coil_amplitude * np.cos(helix_phase) / N_COILS
    
    dR_dphi = R * (B_R / B_phi)
    dZ_dphi = R * (B_Z / B_phi)
    
    return [dR_dphi, dZ_dphi]

def run_simulation(use_asymmetry=True):
    start_radii = np.linspace(R0 + 0.02, R0 + 0.28, 12)
    phi_span = np.linspace(0, 2 * np.pi * LOOPS, LOOPS * 1200)
    
    results = []
    for i, r_start in enumerate(start_radii):
        solution = odeint(
            lambda state, phi: magnetic_field_optimized(state, phi, use_asymmetry),
            [r_start, 0.0], phi_span, rtol=1e-11, atol=1e-13
        )
        R_points = solution[:, 0]
        Z_points = solution[:, 1]
        
        steps_per_loop = len(phi_span) // LOOPS
        poincare_indices = np.arange(0, len(phi_span), steps_per_loop)
        
        std_total = np.std(np.sqrt((R_points[poincare_indices] - np.mean(R_points[poincare_indices]))**2 +
                                  (Z_points[poincare_indices] - np.mean(Z_points[poincare_indices]))**2))
        
        results.append({'surface': i+1, 'std_total': std_total})
    
    return results

# --- EXECUTION ---
print("HEXA-HELIX STELLARATOR - FAIR COMPARISON")
results_sym = run_simulation(use_asymmetry=False)
results_asym = run_simulation(use_asymmetry=True)

print("\nVERGLEICH Symmetric vs. Asymmetric")
print(f"{'Surface':<10} {'Symmetric':<18} {'Asymmetric':<18} {'Change %':<12}")
print("-"*58)

total_change = 0.0
for sym, asym in zip(results_sym, results_asym):
    change = (asym['std_total'] - sym['std_total']) / (sym['std_total'] + 1e-10) * 100
    total_change += change
    print(f"{sym['surface']:<10} {sym['std_total']:<18.6e} {asym['std_total']:<18.6e} {change:+.2f}%")

avg_change = total_change / len(results_sym)
print("-"*58)
print(f"Average Improvement: {avg_change:+.2f}% (negative = better confinement)")
