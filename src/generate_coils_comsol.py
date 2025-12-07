import numpy as np

def generate_helix_data():
    """
    Generiert die Geometrie-Daten für den 6-fach Interlaced Stellarator
    im CSV-Format für den Import in COMSOL/ANSYS.
    Skalierung: Wendelstein 7-X Größe.
    """
    
    # --- KONFIGURATION (Reaktor-Skala) ---
    R0 = 5.5          # Großer Radius (Major Radius) in Metern
    a_coil = 1.5      # Kleiner Radius der Spulen-Mitte in Metern
    N_coils = 6       # Anzahl der Spulen (Symmetrie)
    turns = 8         # Windungen um den Torus pro Spule
    epsilon = 0.15    # Modulation ("Breathing Mode")
    
    # Auflösung: Hoch wählen für Comsol (damit die Kurve glatt ist)
    points_per_coil = 5000 
    
    # Output Dateiname
    filename = "helix_geometry_w7x_scale.csv"
    
    print(f"--- BERECHNUNG GESTARTET ---")
    print(f"Konfiguration: R0={R0}m, a={a_coil}m, N={N_coils}, Turns={turns}")
    
    all_coils_data = []
    
    # Header für die CSV Datei
    header = "Coil_ID, X [m], Y [m], Z [m]"
    
    total_length_avg = 0
    
    for h in range(N_coils):
        # Phasenversatz für 6-fach Symmetrie (60 Grad)
        phase_offset = (h / N_coils) * 2 * np.pi
        
        coil_points = []
        current_coil_length = 0
        prev_point = None
        
        for i in range(points_per_coil + 1):
            # t läuft von 0 bis 2pi (Einmal um den Torus herum)
            t = (i / points_per_coil) * 2 * np.pi
            
            # Die eigentliche Helix-Wicklung (Poloidalwinkel)
            # theta = N * phi + phase
            theta = t * turns + phase_offset
            
            # Modulation (Der "Interlaced" Trick)
            # Radius atmet sinusförmig, um Platz für die anderen Spulen zu machen
            breathing = 1 + epsilon * np.sin(t * N_coils + phase_offset * 2)
            r_effective = a_coil * breathing
            
            # Transformation in Kartesische Koordinaten (Torus)
            # Hauptkreis Ebene (X-Z)
            R_torus = R0 + r_effective * np.cos(theta)
            
            x = R_torus * np.cos(t)
            y = r_effective * np.sin(theta) # Y ist hier die Höhe (Up/Down)
            z = R_torus * np.sin(t)
            
            # Punkt speichern
            coil_points.append(f"{h+1}, {x:.6f}, {y:.6f}, {z:.6f}")
            
            # Längenberechnung (Euklidische Distanz zum Vorgänger)
            current_point = np.array([x, y, z])
            if prev_point is not None:
                dist = np.linalg.norm(current_point - prev_point)
                current_coil_length += dist
            prev_point = current_point
            
        all_coils_data.extend(coil_points)
        print(f"Spule {h+1}: Länge = {current_coil_length:.2f} Meter")
        total_length_avg += current_coil_length

    # Durchschnittslänge berechnen
    avg_len = total_length_avg / N_coils
    print(f"--- ERGEBNIS ---")
    print(f"Durchschnittliche Länge pro Spule (Entfaltung): {avg_len:.2f} Meter")
    print(f"Daten werden geschrieben nach: {filename}")
    
    # Datei schreiben
    with open(filename, "w") as f:
        f.write(header + "\n")
        f.write("\n".join(all_coils_data))
        
    print("Fertig.")

if __name__ == "__main__":
    generate_helix_data()
