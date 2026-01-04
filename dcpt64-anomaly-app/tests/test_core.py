import numpy as np
from backend.app.dcpt64.encoding import encode_planet_longitudes
from backend.app.dcpt64.scoring import topk_hotspots
from backend.app.dcpt64.rotations import build_rot_idx


def test_encode_planet_longitudes_shape_and_norm():
    v = encode_planet_longitudes({"sun": 75.2, "moon": 210.1})
    assert v.shape == (64,)
    norm = np.linalg.norm(v)
    # Expect norm ~ 1.0 when planets provided
    assert 0.999 <= norm <= 1.001


def test_scoring_topk_and_vectorized_shapes():
    rng = np.random.default_rng(1)
    N = 100

    # L: (N,64) float32, one-hot per location
    L = np.zeros((N, 64), dtype=np.float32)
    for i in range(N):
        idx = int(rng.integers(0, 64))
        L[i, idx] = 1.0

    # grid: unique lat/lon pairs to avoid deduping in results
    grid = np.column_stack((np.arange(N, dtype=np.int16), np.arange(N, dtype=np.int16)))

    # base: random normalized vector (64,)
    base = rng.random(64).astype(np.float32)
    base /= np.linalg.norm(base)

    rot_idx = build_rot_idx(days=60, omega=1.0).astype(np.int16)

    # dtypes and shapes preserved
    assert L.dtype == np.float32
    assert rot_idx.dtype == np.int16
    assert rot_idx.shape == (60, 64)

    # vectorized constructions
    E = base[rot_idx]
    assert E.shape == (60, 64)
    S = L @ E.T
    assert S.shape == (N, 60)

    # scoring result
    top5 = topk_hotspots(L=L, grid=grid, base=base, rot_idx=rot_idx, topk=5, keep=50)
    assert isinstance(top5, list)
    assert len(top5) == 5
    for item in top5:
        assert set(item.keys()) == {"lat", "lon", "best_day", "score"}
