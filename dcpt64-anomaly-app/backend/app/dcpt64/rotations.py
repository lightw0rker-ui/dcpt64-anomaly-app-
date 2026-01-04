from __future__ import annotations
import os
import numpy as np

CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "cache")
CACHE_DIR = os.path.abspath(CACHE_DIR)

def _ensure_cache_dir():
    os.makedirs(CACHE_DIR, exist_ok=True)

def build_rot_idx(days: int = 60, omega: float = 1.0) -> np.ndarray:
    """
    Precompute index mapping for phase rotation.
    shift[t] = round(t * omega) mod 64
    evolved[t, k] = base[rot_idx[t, k]]

    Returns rot_idx shape (days, 64), dtype int16.
    """
    t = np.arange(days, dtype=np.int32)
    shift = (np.rint(t * omega).astype(np.int32)) % 64
    k = np.arange(64, dtype=np.int32)[None, :]
    rot_idx = (k - shift[:, None]) % 64
    return rot_idx.astype(np.int16)

def load_or_build(days: int = 60, omega: float = 1.0, filename: str | None = None) -> np.ndarray:
    """
    Loads rot_idx from cache if present, otherwise builds and saves.
    """
    _ensure_cache_dir()

    if filename is None:
        filename = f"rot_idx_days{days}.npy"

    path = os.path.join(CACHE_DIR, filename)

    if os.path.exists(path):
        return np.load(path)

    rot_idx = build_rot_idx(days=days, omega=omega)
    np.save(path, rot_idx)
    return rot_idx
