from __future__ import annotations
import os
import numpy as np
from .grid import make_grid

# Cache directory: backend/app/cache
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "cache")
CACHE_DIR = os.path.abspath(CACHE_DIR)

def _ensure_cache_dir() -> None:
    os.makedirs(CACHE_DIR, exist_ok=True)

def earth_state_index(lat: int, lon: int) -> int:
    b5 = 1 if lat >= 0 else 0
    b4 = 1 if lon >= 0 else 0

    lat_bin = int(np.clip(((lat + 90) / 180) * 8, 0, 7))
    lon_parity = (abs(lon) // 10) % 2

    return (b5 << 5) | (b4 << 4) | (lat_bin << 1) | int(lon_parity)

def _build_earth_L(grid: np.ndarray, sigma: float = 2.0) -> np.ndarray:
    N = grid.shape[0]
    centers = np.zeros(N, dtype=np.int16)

    for i, (lat, lon) in enumerate(grid):
        centers[i] = earth_state_index(int(lat), int(lon))

    k = np.arange(64, dtype=np.int16)[None, :]
    c = centers[:, None]

    d = np.abs(k - c).astype(np.float32)
    d = np.minimum(d, 64.0 - d)

    W = np.exp(-(d**2) / (2.0 * float(sigma) ** 2)).astype(np.float32)
    W /= W.sum(axis=1, keepdims=True)
    return W

def load_or_build(step_deg: int = 5, sigma: float = 2.0) -> tuple[np.ndarray, np.ndarray]:
    _ensure_cache_dir()

    grid_path = os.path.join(CACHE_DIR, f"grid_points_step{step_deg}.npy")
    L_path = os.path.join(CACHE_DIR, f"earth_L_step{step_deg}_sigma{sigma}.npy")

    if os.path.exists(grid_path) and os.path.exists(L_path):
        return np.load(grid_path), np.load(L_path)

    grid = make_grid(step_deg=step_deg)
    L = _build_earth_L(grid, sigma=sigma)

    np.save(grid_path, grid)
    np.save(L_path, L)
    return grid, L
