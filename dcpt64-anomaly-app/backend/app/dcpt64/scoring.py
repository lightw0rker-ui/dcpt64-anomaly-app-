from __future__ import annotations
import numpy as np

def topk_hotspots(
    L: np.ndarray,
    grid: np.ndarray,
    base: np.ndarray,
    rot_idx: np.ndarray,
    topk: int = 5,
    keep: int = 50
):
    """
    Vectorized hotspot ranking.

    L: (N,64) float32 Earth/location matrix
    grid: (N,2) int16 [lat, lon]
    base: (64,) float32 normalized DCPT-64 state vector
    rot_idx: (T,64) int16 rotation index table (T=60 in MVP)

    Returns: list[dict] each with lat, lon, best_day, score
    """
    # E: (T,64) evolved states
    E = base[rot_idx]

    # S: (N,T) scores
    S = L @ E.T

    flat = S.ravel()
    keep = min(int(keep), flat.size)

    # get indices of top 'keep' values (unordered) then sort those
    idx = np.argpartition(flat, -keep)[-keep:]
    idx = idx[np.argsort(flat[idx])[::-1]]

    T = S.shape[1]
    results = []
    used = set()

    for j in idx:
        loc_i = int(j // T)
        t_i = int(j % T)

        lat = int(grid[loc_i, 0])
        lon = int(grid[loc_i, 1])

        # dedupe by location
        key = (lat, lon)
        if key in used:
            continue
        used.add(key)

        results.append({
            "lat": lat,
            "lon": lon,
            "best_day": t_i,
            "score": float(flat[j]),
        })

        if len(results) >= topk:
            break

    return results
