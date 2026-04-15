from __future__ import annotations

import tkinter as tk

from src.config.settings import COLORS, FONT_MONO
from src.models.key_event import KeyEvent


_TAG_COLORS: dict[str, str] = {
    "normal":   COLORS["tag_normal"],
    "special":  COLORS["tag_special"],
    "function": COLORS["tag_function"],
    "space":    COLORS["tag_space"],
    "enter":    COLORS["tag_enter"],
    "time":     COLORS["tag_time"],
}


class LogWidget:
    def __init__(self, parent: tk.Misc) -> None:
        self._frame = tk.Frame(parent, bg=COLORS["bg"])
        self._frame.pack(expand=True, fill="both", padx=10, pady=(10, 0))

        scrollbar = tk.Scrollbar(self._frame)
        scrollbar.pack(side="right", fill="y")

        self._text = tk.Text(
            self._frame,
            font=FONT_MONO,
            bg=COLORS["bg_dark"],
            fg=COLORS["fg"],
            insertbackground=COLORS["fg"],
            wrap="word",
            state="disabled",
            yscrollcommand=scrollbar.set,
        )
        self._text.pack(side="left", expand=True, fill="both")
        scrollbar.config(command=self._text.yview)

        self._block_user_input()
        self._configure_tags()


    def append(self, event: KeyEvent) -> None:
        self._text.config(state="normal")
        self._text.insert(tk.END, f"[{event.timestamp}] ", "time")
        self._text.insert(tk.END, f"{event.display}\n", event.tag)
        self._text.see(tk.END)
        self._text.config(state="disabled")

    def clear(self) -> None:
        self._text.config(state="normal")
        self._text.delete("1.0", tk.END)
        self._text.config(state="disabled")

    def get_content(self) -> str:
        return self._text.get("1.0", tk.END).strip()

    def _block_user_input(self) -> None:
        for seq in ("<Key>", "<<Paste>>", "<Control-Key-v>"):
            self._text.bind(seq, lambda e: "break")

    def _configure_tags(self) -> None:
        for tag, color in _TAG_COLORS.items():
            self._text.tag_config(tag, foreground=color)