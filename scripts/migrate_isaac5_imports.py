#!/usr/bin/env python3
"""One-shot import migration: Isaac Sim 4.x omni.isaac.* -> isaacsim.* / isaaclab.*"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Order matters: longer / more specific patterns first.
REPLACEMENTS = [
    ("from omni.isaac.core.utils import prims as prim_utils, stage as stage_utils",
     "from isaacsim.core.utils import prims as prim_utils, stage as stage_utils"),
    ("from omni.isaac.core.simulation_context import SimulationContext",
     "from isaacsim.core.api.simulation_context import SimulationContext"),
    ("from omni.isaac.core.utils.extensions import enable_extension",
     "from isaacsim.core.utils.extensions import enable_extension"),
    ("from omni.isaac.core.utils.viewports import set_camera_view",
     "from isaacsim.core.utils.viewports import set_camera_view"),
    ("from omni.isaac.core.utils.semantics import add_update_semantics",
     "from isaacsim.core.utils.semantics import add_update_semantics"),
    ("from omni.isaac.core.utils.constants import AXES_TOKEN",
     "from isaacsim.core.utils.constants import AXES_TOKEN"),
    ("from omni.isaac.core.utils.types import JointsState, ArticulationActions",
     "from isaacsim.core.utils.types import JointsState, ArticulationActions"),
    ("from omni.isaac.core.utils.nucleus import get_assets_root_path",
     "from isaacsim.core.utils.nucleus import get_assets_root_path"),
    ("from omni.isaac.core.utils.stage import add_reference_to_stage, get_current_stage",
     "from isaacsim.core.utils.stage import add_reference_to_stage, get_current_stage"),
    ("from omni.isaac.core.utils.string import find_root_prim_path_from_regex",
     "from isaacsim.core.utils.string import find_root_prim_path_from_regex"),
    ("from omni.isaac.core.utils.prims import get_prim_parent, get_prim_at_path, set_prim_property, get_prim_property",
     "from isaacsim.core.utils.prims import get_prim_parent, get_prim_at_path, set_prim_property, get_prim_property"),
    ("from omni.isaac.core.utils.prims import (",
     "from isaacsim.core.utils.prims import ("),
    ("from omni.isaac.core.utils.prims import get_prim_path",
     "from isaacsim.core.utils.prims import get_prim_path"),
    ("from omni.isaac.core.utils.prims import XFormPrim",
     "from isaacsim.core.prims import XFormPrim"),
    ("from omni.isaac.core.prims import XFormPrim",
     "from isaacsim.core.prims import XFormPrim"),
    ("from omni.isaac.core.prims import XFormPrimView",
     "from isaacsim.core.prims import XFormPrim"),
    ("from omni.isaac.core.articulations import ArticulationView as _ArticulationView",
     "from isaacsim.core.articulations import Articulation as _ArticulationView"),
    ("from omni.isaac.core.articulations import ArticulationView",
     "from isaacsim.core.articulations import Articulation as ArticulationView"),
    ("from omni.isaac.core.prims import RigidPrimView as _RigidPrimView",
     "from isaacsim.core.prims import RigidPrim as _RigidPrimView"),
    ("from omni.isaac.core.prims import RigidPrimView",
     "from isaacsim.core.prims import RigidPrim"),
    ("from omni.isaac.cloner import GridCloner",
     "from isaacsim.core.cloner import GridCloner"),
    ("from omni.isaac.debug_draw import _debug_draw",
     "from isaacsim.util.debug_draw import _debug_draw"),
    ("from omni.isaac.version import get_version",
     "from isaacsim.core.version import get_version"),
    ("import omni.isaac.core.utils.prims as prim_utils",
     "import isaacsim.core.utils.prims as prim_utils"),
    ("import omni.isaac.core.utils.stage as stage_utils",
     "import isaacsim.core.utils.stage as stage_utils"),
    ("import omni.isaac.core.utils.torch as torch_utils",
     "import isaacsim.core.utils.torch as torch_utils"),
    ("import omni.isaac.core.utils.nucleus as nucleus_utils",
     "import isaacsim.core.utils.nucleus as nucleus_utils"),
    ("import omni.isaac.core.objects as objects",
     "import isaacsim.core.api.objects as objects"),
    ("import omni.isaac.core.materials as materials",
     "import isaacsim.core.api.materials as materials"),
    ("from omni.isaac.core.objects import DynamicCuboid",
     "from isaacsim.core.api.objects import DynamicCuboid"),
    ("from omni.isaac.core import objects",
     "from isaacsim.core.api import objects"),
    ("from omni.isaac.core.materials import PhysicsMaterial",
     "from isaacsim.core.api.materials import PhysicsMaterial"),
    ("from omni.isaac.core.prims import GeometryPrim",
     "from isaacsim.core.prims import SingleGeometryPrim as GeometryPrim"),
    ("import omni.isaac.lab.sim as sim_utils",
     "import isaaclab.sim as sim_utils"),
    ("from omni.isaac.lab.assets import AssetBaseCfg",
     "from isaaclab.assets import AssetBaseCfg"),
    ("from omni.isaac.lab.sensors import ContactSensorCfg, ContactSensor",
     "from isaaclab.sensors import ContactSensorCfg, ContactSensor"),
    ("from omni.isaac.lab.sensors import RayCaster, RayCasterCfg, patterns",
     "from isaaclab.sensors import RayCaster, RayCasterCfg, patterns"),
    ("from omni.isaac.lab.terrains import (",
     "from isaaclab.terrains import ("),
    ("# from omni.isaac.lab.utils.assets import NVIDIA_NUCLEUS_DIR",
     "# from isaaclab.utils.assets import NVIDIA_NUCLEUS_DIR"),
    ("omni.isaac.core.utils.numpy.deg2rad",
     "isaacsim.core.utils.numpy.deg2rad"),
    ('"omni.isaac.core.utils.torch"',
     '"isaacsim.core.utils.torch"'),
    ('"omni.isaac.cloner"',
     '"isaacsim.core.cloner"'),
    ('"omni.isaac.core"',
     '"isaacsim.core"'),
]

SKIP = {"scripts/migrate_isaac5_imports.py"}


def migrate_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP:
        return False
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    changed = []
    for path in ROOT.rglob("*.py"):
        if migrate_file(path):
            changed.append(path.relative_to(ROOT))
    for path in ROOT.rglob("*.rst"):
        if migrate_file(path):
            changed.append(path.relative_to(ROOT))
    print(f"Migrated {len(changed)} files:")
    for p in sorted(changed):
        print(f"  {p}")


if __name__ == "__main__":
    main()
