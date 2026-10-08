#!/usr/bin/env python3
"""Regenerate the face clamp. Numbers match design.md."""
import sys
import trimesh
plate = trimesh.creation.box(extents=(16.0, 14.0, 3.0))
def hole(radius, x):
    solid = trimesh.creation.cylinder(radius=radius, height=10.0, sections=64)
    solid.apply_translation((x, 0.0, 0.0))
    return solid
mesh = trimesh.boolean.difference([plate, hole(0.9, -4.5), hole(0.9, 4.5), hole(1.7, 0.0)])
if mesh is None or not mesh.is_watertight:
    sys.exit('clamp mesh failed')
if [round(float(v), 3) for v in mesh.extents] != [16.0, 14.0, 3.0]:
    sys.exit('unexpected extents')
mesh.export(sys.argv[1] if len(sys.argv) > 1 else 'clamp-plate.stl')
