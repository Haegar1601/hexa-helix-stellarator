## Preliminary Toy-Model Exploration (Analytical Field-Line Tracing)
To gain initial intuition about the confinement properties of the N=6 interlaced geometry, a simplified analytical model was implemented in Python (field-line integration via scipy.odeint, Poincaré sections).

### Key findings:

•	Stability Threshold: At high perturbation amplitude ($\epsilon \approx 0.05$), significant stochasticity and breakdown of flux surfaces occur.

•	Confinement Recovery: At low amplitude ($\epsilon \approx 0.001$) with mild radial shear, perfectly closed, nested flux surfaces are recovered across all tested radii ($\sigma \approx 0$, unique Poincaré points = 1 per surface).

•	Dynamic Potential: These results suggest the geometry is capable of good confinement. The "Breathing Mode" (dynamic phase modulation) is hypothesized to further stabilize these surfaces at higher amplitudes by avoiding static resonance overlaps.

### Limitations:

•	This is a vacuum, analytic toy model using sinusoidal approximations – higher harmonics from complex discrete coil shapes are not yet included.

•	No finite-$\beta$ effects, transport, or MHD stability analysis.

### Conclusion: 
The toy model provides a strong positive signal that the Hexa-Helix geometry produces closed flux surfaces under appropriate parameter regimes. Full 3D MHD validation with VMEC/SPEC using the provided discrete coil data is the critical next step to bridge the "Grounding Gap".
