APP_TITLE = "HKG - Keystroke Tracker"
APP_GEOMETRY = "650x500"


COLORS: dict[str, str] = {
    "bg":           "#1e1e1e",
    "bg_dark":      "#141414",
    "bg_menu":      "#2b2b2b",

    "fg":           "#ffffff",
    "fg_muted":     "#888888",
    "fg_dim":       "#b0b0b0",

    "status_active":   "#4cff4c",
    "status_stopped":  "orange",
    "status_error":    "#ff5555",
    "status_inactive": "gray",

    "tag_normal":   "#65a8ff",
    "tag_special":  "#ff7b7b",
    "tag_function": "#d7ff6b",
    "tag_space":    "#b0b0b0",
    "tag_enter":    "#b565ff",
    "tag_time":     "#888888",
}


FONT_MONO:     tuple[str, int]        = ("Consolas", 13)
FONT_UI:       tuple[str, int]        = ("Arial", 12)
FONT_UI_BOLD:  tuple[str, int, str]   = ("Arial", 12, "bold")


SPECIAL_KEYS: dict[str, tuple[str, str]] = {
    "space": ("[space]", "space"),
    "enter": ("[enter]", "enter"),
    "shift": ("[shift]", "special"),
    "alt":   ("[alt]",   "special"),
    "ctrl":  ("[ctrl]",  "special"),
    "tab":   ("[tab]",   "special"),
}