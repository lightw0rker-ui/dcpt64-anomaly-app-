import numpy as np

def encode_planet_longitudes(planets: dict[str, float]) -> np.ndarray:
    """
    planets: {'sun': 75.2, 'moon': 210.1, ...} degrees in [0,360)
    MVP: bin each longitude into 64 bins and sum -> normalized 64-vector.
    """
    v = np.zeros(64, dtype=np.float32)
    for _, lon in planets.items():
        idx = int((lon % 360.0) / 360.0 * 64.0) % 64
        v[idx] += 1.0

    norm = np.linalg.norm(v)
    return v if norm == 0 else (v / norm)
