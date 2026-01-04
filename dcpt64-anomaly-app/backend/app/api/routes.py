from fastapi import APIRouter
from .schemas import HotspotRequest, HotspotResponse

from backend.app.geo.earth_cache import load_or_build as load_earth
from backend.app.dcpt64.encoding import encode_planet_longitudes
from backend.app.dcpt64.rotations import load_or_build as load_rot
from backend.app.dcpt64.scoring import topk_hotspots

router = APIRouter()

# Load caches ONCE at startup
GRID, L = load_earth(step_deg=5)
ROT_IDX = load_rot(days=60, omega=1.0)

@router.get("/health")
def health():
    return {"ok": True}

@router.post("/hotspots/top5", response_model=HotspotResponse)
def hotspots_top5(req: HotspotRequest):
    base = encode_planet_longitudes(req.planets)
    top5 = topk_hotspots(L=L, grid=GRID, base=base, rot_idx=ROT_IDX, topk=5, keep=50)
    return {"settings": {"grid_step": 5, "days": 60}, "top5": top5}
