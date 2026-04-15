from __future__ import annotations

import tkinter as tk

from src.config.settings import COLORS, FONT_MONO, FONT_UI_BOLD


class StatsWindow:
    def __init__(
        self,
        parent: tk.Misc,
        total: int,
        sorted_counts: list[tuple[str, int]],
    ) -> None:
        self._win = tk.Toplevel(parent)
        self._win.title("Key Statistics")
        self._win.geometry("400x320")
        self._win.config(bg=COLORS["bg"])
        self._win.resizable(False, False)

        self._build(total, sorted_counts)


    def _build(self, total: int, sorted_counts: list[tuple[str, int]]) -> None:
        tk.Label(
            self._win,
            text=f"Total events: {total}",
            font=FONT_UI_BOLD,
            bg=COLORS["bg"],
            fg=COLORS["fg"],
        ).pack(pady=8)

        frame = tk.Frame(self._win, bg=COLORS["bg"])
        frame.pack(expand=True, fill="both", padx=8, pady=(0, 8))

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        box = tk.Text(
            frame,
            font=FONT_MONO,
            bg=COLORS["bg_dark"],
            fg=COLORS["fg"],
            wrap="none",
            state="normal",
            yscrollcommand=scrollbar.set,
        )
        for key, count in sorted_counts:
            box.insert(tk.END, f"{key}: {count}\n")
        box.config(state="disabled")
        box.pack(side="left", expand=True, fill="both")
        scrollbar.config(command=box.yview)
