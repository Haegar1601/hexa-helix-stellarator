import numpy as np
import math

def generate_hexa_helix():
    """
    Generates the point cloud data for the 6-fold Interlaced Helix Stellarator.
    Based on the concept by Hagen Loehrmann.
    """
    # Parameters from the Whitepaper
    R0 = 5.5        # Major Radius (meters)
    a = 1.5         # Minor Radius (meters)
    N = 6           # Symmetry (Number of coils)
    turns = 8       # Poloidal turns per toroidal transit
    points_per_coil = 1000
    epsilon = 0.15  # Modulation amplitude ("Breathing Mode")
    
    # Twist scaling (from your JS simulation default)
    twist_scale = 0.5 

    coils = []

    print(f"Generating {N} interlaced helical coils...")

    for h in range(N):
        # Phase offset: 60 degrees (2pi/6)
        phase_offset = (h / N) * 2 * np.pi
        
        coil_points = []
        
        for i in range(points_per_coil + 1):
            t = (i / points_per_coil) * 2 * np.pi  # Toroidal angle phi
            
            # Helical winding angle theta
            helix_angle = t * turns + phase_offset
            
            # "Breathing Mode" Modulation
            # Matches JS: 1 + 0.15 * sin(t * 6 + phaseOffset * 2)
            breathing_factor = 1 + epsilon * np.sin(t * 6 + phase_offset * 2)
            
            # Effective minor radius at this point
            r_eff = a * breathing_factor * twist_scale
            
            # Toroidal Coordinates to Cartesian (X, Y, Z)
            # Normal vector logic adapted from Frenet frame approximation in torus
            
            # Position on the major circle (center of the tube)
            torus_x = np.cos(t) * R0
            torus_z = np.sin(t) * R0
            
            # Normal vector (pointing inward to torus center)
            normal_x = -np.cos(t)
            normal_z = -np.sin(t)
            
            # Local helix position
            local_x = np.cos(helix_angle) * r_eff
            local_y = np.sin(helix_angle) * r_eff # Up/Down
            
            # Final Cartesian Coordinates
            x = torus_x + local_x * normal_x
            y = local_y
            z = torus_z + local_x * normal_z
            
            coil_points.append((x, y, z))
        
        coils.append(coil_points)

    return coils

def save_to_csv(coils, filename="hexa_helix_coils.csv"):
    """Saves the coils to a simple CSV format: Coil_ID, X, Y, Z"""
    with open(filename, "w") as f:
        f.write("Coil_ID,X,Y,Z\n")
        for coil_id, points in enumerate(coils):
            for x, y, z in points:
                f.write(f"{coil_id},{x:.6f},{y:.6f},{z:.6f}\n")
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    coils = generate_hexa_helix()
    save_to_csv(coils)
