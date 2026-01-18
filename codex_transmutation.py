
# Prototype: Codex Transmutation Engine Interface

# Input: Emotional State A and B (Hz from David Hawkins Map)
# Output:
# - AM (Arithmetic Mean) => Narrative / Perception
# - GM (Geometric Mean) => Energetic Coherence
# - DM (Differential Mean) => Tension / Pressure
# - Phi Collapse => Transmutation Scalar
# - Closest Musical Note, Color, Wavelength
# - Phrase: "I stabilize. I harmonize. I transform."

from math import sqrt, pi

# Constants
PHI = 1.61803398875

# Color/music mapping based on your chart
color_map = [
    {"note": "G", "hz": 192, "color": "Red", "nm": 710.05},
    {"note": "A", "hz": 216, "color": "Orange", "nm": 631.16},
    {"note": "B", "hz": 240, "color": "Yellow", "nm": 568.04},
    {"note": "C", "hz": 256, "color": "Green", "nm": 532.54},
    {"note": "D", "hz": 288, "color": "Blue", "nm": 473.37},
    {"note": "E", "hz": 320, "color": "Purple", "nm": 426.03},
    {"note": "F#", "hz": 360, "color": "Indigo", "nm": 378.69},
]

# Core function
def transmute_emotions(hz_a, hz_b):
    am = (hz_a + hz_b) / 2
    gm = sqrt(hz_a * hz_b)
    dm = abs(hz_b - hz_a) / 2
    phi_collapse = dm / PHI

    # Find nearest note/color
    closest = min(color_map, key=lambda x: abs(x['hz'] - gm))

    return {
        "AM (Narrative Perception)": round(am, 2),
        "GM (Energetic Coherence)": round(gm, 2),
        "DM (Tension Field)": round(dm, 2),
        "Phi Collapse Scalar": round(phi_collapse, 2),
        "Note": closest['note'],
        "Color": closest['color'],
        "Wavelength (nm)": closest['nm'],
        "Phrase": "I stabilize. I harmonize. I transform."
    }

# Example (Fear → Love)
example = transmute_emotions(100, 500)
for k, v in example.items():
    print(f"{k}: {v}")
