#!/usr/bin/env python3
"""Map each manual/ JPG to exactly one HTML image slot (72 photos, 72 slots).

Five table/diagram slots on pages 29/41/44/45 are rendered as inline SVG, not photos.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "assets/images/manual"

# slot_key -> (filename, css_class, style)
PHOTO_SLOTS: dict[str, tuple[str, str, str]] = {
    # --- early diagram pages ---
    "p018_diag036": ("Screenshot_20260628_225919_Samsung Notes.jpg", "diag", "max-height:360px;width:100%;object-fit:contain;margin:8px 0"),
    "p019_diag037": ("Screenshot_20260628_225916_Samsung Notes.jpg", "diag", "max-height:340px;width:100%;object-fit:contain;margin:8px 0"),
    "p021_fig1": ("Screenshot_20260628_225930_Samsung Notes.jpg", "diag", "max-height:300px;width:48%;object-fit:contain"),
    "p021_fig2": ("Screenshot_20260628_230306_Samsung Notes (2) (1).jpg", "diag", "max-height:300px;width:48%;object-fit:contain"),
    "p022_fig1": ("Screenshot_20260628_225952_Samsung Notes (1).jpg", "diag", "max-height:260px;width:48%;object-fit:contain"),
    "p022_fig2": ("Screenshot_20260628_230306_Samsung Notes (4) (2).jpg", "diag", "max-height:260px;width:48%;object-fit:contain"),
    "p032_diag059": ("Screenshot_20260628_225940_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p035_diag065": ("Screenshot_20260628_225945_Samsung Notes.jpg", "diag", "max-height:260px;width:100%;object-fit:contain;margin:8px 0"),
    "p049_diag099": ("Screenshot_20260628_230247_Samsung Notes.jpg", "diag", "max-height:220px;width:100%;object-fit:contain;margin:8px 0"),
    # --- pages 60+ diagrams (order matches HTML layout) ---
    "p060_diag126": ("Screenshot_20260628_230025_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p061_diag128": ("Screenshot_20260628_230028_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p071_diag162": ("Screenshot_20260628_230038_Samsung Notes.jpg", "diag", "max-height:120px;width:100%;object-fit:contain;margin:8px 0"),
    "p073_sym168": ("Screenshot_20260628_230153_Samsung Notes (1).jpg", "sym", "max-height:52px;width:auto;display:inline-block;vertical-align:middle"),
    "p074_diag170": ("Screenshot_20260628_230102_Samsung Notes.jpg", "diag", "max-height:240px;width:100%;object-fit:contain;margin:8px 0"),
    "p080_diag182": ("Screenshot_20260628_230204_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p088_diag208_1": ("Screenshot_20260628_230218_Samsung Notes.jpg", "diag", "max-height:160px;width:100%;object-fit:contain;margin:8px 0"),
    "p088_diag208_2": ("Screenshot_20260628_230220_Samsung Notes.jpg", "diag", "max-height:160px;width:100%;object-fit:contain;margin:8px 0"),
    "p096_diag224": ("Screenshot_20260628_230015_Samsung Notes.jpg", "diag", "max-height:180px;width:100%;object-fit:contain;margin:8px 0"),
    "p097_diag228": ("Screenshot_20260628_230113_Samsung Notes.jpg", "diag", "max-height:180px;width:100%;object-fit:contain;margin:8px 0"),
    "p108_cubicle_l": ("Screenshot_20260628_230147_Samsung Notes.jpg", "diag", "max-height:200px;width:48%;display:inline-block;object-fit:contain"),
    "p108_cubicle_r": ("Screenshot_20260628_230138_Samsung Notes.jpg", "diag", "max-height:200px;width:48%;display:inline-block;object-fit:contain"),
    "p109_q258_diag": ("Screenshot_20260628_230159_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p114_diag268": ("Screenshot_20260628_230045_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p115_diag270": ("Screenshot_20260628_230156_Samsung Notes.jpg", "diag", "max-height:320px;width:100%;object-fit:contain;margin:8px 0"),
    "p118_diag282": ("Screenshot_20260628_230211_Samsung Notes.jpg", "diag", "max-height:90px;width:100%;object-fit:contain;margin:8px 0"),
    "p125_diag299": ("Screenshot_20260628_230215_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p126_diag300": ("Screenshot_20260628_230244_Samsung Notes.jpg", "diag", "max-height:240px;width:100%;object-fit:contain;margin:8px 0"),
    "p128_diag303": ("Screenshot_20260628_225926_Samsung Notes.jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p135_sys_gnd": ("Screenshot_20260628_230228_Samsung Notes.jpg", "diag", "max-height:140px;width:48%;object-fit:contain"),
    "p135_eq_gnd": ("Screenshot_20260628_230235_Samsung Notes.jpg", "diag", "max-height:140px;width:48%;object-fit:contain"),
    "p139_line_gnd": ("Screenshot_20260628_230249_Samsung Notes.jpg", "diag", "max-height:260px;width:48%;display:inline-block;object-fit:contain"),
    "p139_portable_gnd": ("Screenshot_20260628_230254_Samsung Notes.jpg", "diag", "max-height:260px;width:48%;display:inline-block;object-fit:contain"),
    "p140_diag331": ("Screenshot_20260628_230238_Samsung Notes.jpg", "diag", "max-height:260px;width:100%;object-fit:contain;margin:8px 0"),
    "p146_fig1": ("Screenshot_20260628_230110_Samsung Notes.jpg", "diag", "max-height:150px;width:48%;display:inline-block;object-fit:contain"),
    "p146_fig2": ("Screenshot_20260628_225952_Samsung Notes (2).jpg", "diag", "max-height:150px;width:48%;display:inline-block;object-fit:contain"),
    "p147_wenner": ("Screenshot_20260628_230153_Samsung Notes (2) (1).jpg", "diag", "max-height:110px;width:100%;object-fit:contain;margin:8px 0"),
    "p148_earth_tester": ("Screenshot_20260628_230153_Samsung Notes (3) (1).jpg", "diag", "max-height:200px;width:100%;object-fit:contain;margin:8px 0"),
    "p149_timed_contact": ("Screenshot_20260628_230153_Samsung Notes (3).jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "p153_relay8": ("Screenshot_20260628_230153_Samsung Notes.jpg", "diag", "max-height:300px;width:100%;object-fit:contain;margin:8px 0"),
    # --- symbol pages 159-161 ---
    "sym_sw": ("Screenshot_20260628_230306_Samsung Notes (1) (1).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_2p": ("Screenshot_20260628_230306_Samsung Notes.jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_4w": ("Screenshot_20260628_230306_Samsung Notes (1).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_outdoor": ("Screenshot_20260628_230042_Samsung Notes.jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_h400": ("Screenshot_20260628_225952_Samsung Notes.jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_m400": ("Screenshot_20260628_230306_Samsung Notes (4).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_n400": ("Screenshot_20260628_230306_Samsung Notes (4) (1).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_outlet": ("Screenshot_20260628_230306_Samsung Notes (2).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_ceiling": ("Screenshot_20260628_230051_Samsung Notes.jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_floor": ("Screenshot_20260628_230306_Samsung Notes (2) (1) (1).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_2gang": ("Screenshot_20260628_230306_Samsung Notes (3).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_3p_out": ("Screenshot_20260628_230306_Samsung Notes (2) (2).jpg", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_lk": ("Screenshot_20260628_230310_Samsung Notes.jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_et": ("Screenshot_20260628_230153_Samsung Notes (2).jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_el": ("Screenshot_20260628_230310_Samsung Notes (3).jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_e_outlet": ("Screenshot_20260628_230310_Samsung Notes (5).jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_t_outlet": ("Screenshot_20260628_230310_Samsung Notes (4).jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_wp": ("Screenshot_20260628_230310_Samsung Notes (6).jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_h_outlet": ("Screenshot_20260628_230310_Samsung Notes (3) (1).jpg", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_switch_368": ("Screenshot_20260628_230310_Samsung Notes (1).jpg", "diag", "max-height:72px;width:100%;object-fit:contain;margin:4px 0"),
    "sym_md": ("Screenshot_20260628_230310_Samsung Notes (2).jpg", "sym", "max-height:36px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_ld": ("Screenshot_20260628_230310_Samsung Notes (2) (1).jpg", "sym", "max-height:36px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_f7": ("Screenshot_20260628_230310_Samsung Notes (2) (2).jpg", "sym", "max-height:36px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_breaker_e": ("Screenshot_20260628_230313_Samsung Notes.jpg", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_b": ("Screenshot_20260628_230313_Samsung Notes (2).jpg", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_ec": ("Screenshot_20260628_230313_Samsung Notes (3).jpg", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_s": ("Screenshot_20260628_230313_Samsung Notes (5).jpg", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_g": ("Screenshot_20260628_230313_Samsung Notes (6).jpg", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_tr_tb": ("Screenshot_20260628_230313_Samsung Notes (4).jpg", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_tr": ("Screenshot_20260628_230313_Samsung Notes (1).jpg", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_tn": ("Screenshot_20260628_230313_Samsung Notes (4) (1).jpg", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_tf": ("Screenshot_20260628_230313_Samsung Notes (1) (1).jpg", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_th": ("Screenshot_20260628_230153_Samsung Notes (4).jpg", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
}

# Sequential diagram slot keys as they appear in HTML (pages 18-49 and 60+)
EARLY_DIAG_ORDER: list[str] = [
    "p018_diag036",
    "p019_diag037",
    "p021_fig1",
    "p021_fig2",
    "p022_fig1",
    "p022_fig2",
    # p029: SVG tables (2 slots)
    "p032_diag059",
    "p035_diag065",
    # p041: SVG table
    # p044, p045: SVG tables
    "p049_diag099",
]

MID_DIAG_ORDER: list[str] = [
    "p060_diag126",
    "p061_diag128",
    "p071_diag162",
    "p073_sym168",
    "p074_diag170",
    "p080_diag182",
    "p088_diag208_1",
    "p088_diag208_2",
    "p096_diag224",
    "p097_diag228",
    "p108_cubicle_l",
    "p108_cubicle_r",
    "p109_q258_diag",
    "p114_diag268",
    "p115_diag270",
    "p118_diag282",
    "p125_diag299",
    "p126_diag300",
    "p128_diag303",
    "p135_sys_gnd",
    "p135_eq_gnd",
    "p139_line_gnd",
    "p139_portable_gnd",
    "p140_diag331",
    "p146_fig1",
    "p146_fig2",
    "p147_wenner",
    "p148_earth_tester",
    "p149_timed_contact",
    "p153_relay8",
]

SYM_ORDER: list[str] = [
    "sym_sw", "sym_2p", "sym_4w", "sym_outdoor", "sym_h400", "sym_m400", "sym_n400",
    "sym_outlet", "sym_ceiling", "sym_floor", "sym_2gang", "sym_3p_out",
    "sym_lk", "sym_et", "sym_el", "sym_e_outlet", "sym_t_outlet", "sym_wp", "sym_h_outlet",
    "sym_switch_368", "sym_md", "sym_ld", "sym_f7",
    "sym_breaker_e", "sym_breaker_b", "sym_breaker_ec", "sym_breaker_s", "sym_breaker_g",
    "sym_tr_tb", "sym_tr_tr", "sym_tr_tn", "sym_tr_tf", "sym_tr_th",
]


def manual_rel_path(filename: str) -> str:
    return f"../assets/images/manual/{filename}"


def photo_img_tag(slot: str) -> str:
    filename, cls, style = PHOTO_SLOTS[slot]
    path = manual_rel_path(filename)
    return (
        f'<img class="{cls}" src="{path}" style="{style};" alt="" '
        f'data-manual="{filename}" data-slot="{slot}">'
    )


def validate_registry() -> None:
    shots = {p.name for p in MANUAL.glob("Screenshot_*.jpg")}
    used = {v[0] for v in PHOTO_SLOTS.values()}
    missing = used - shots
    extra = shots - used
    if missing:
        raise SystemExit(f"Registry references missing files: {sorted(missing)}")
    if extra:
        raise SystemExit(f"Unused manual photos ({len(extra)}): {sorted(extra)}")
    if len(PHOTO_SLOTS) != 72:
        raise SystemExit(f"Expected 72 photo slots, got {len(PHOTO_SLOTS)}")
    if len(used) != 72:
        raise SystemExit(f"Expected 72 unique files, got {len(used)}")
