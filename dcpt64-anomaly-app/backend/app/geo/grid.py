import numpy as np

def make_grid(step_deg: int = 5) -> np.ndarray:
    """
    Returns (N,2) array of [lat, lon] in degrees.
    step_deg=5 -> ~2701 points.
    """
    lats = np.arange(-90, 91, step_deg, dtype=np.int16)
    lons = np.arange(-180, 181, step_deg, dtype=np.int16)
    grid = np.array([(lat, lon) for lat in lats for lon in lons], dtype=np.int16)
    return grid
