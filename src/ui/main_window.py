from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

import keyboard

from src.config.settings import COLORS, FONT_UI
from src.models.key_event import KeyEvent
from src.ui.log_widget import LogWidget
from src.ui.stats_window import StatsWindow
from src.utils.log_parser import parse_statistics


class MainWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.config(bg=COLORS["bg"])

        self._logging = False

        self._log_widget = LogWidget(root)
        self._build_menu()
        self._build_statusbar()


    def _build_menu(self) -> None:
        menubar = tk.Menu(
            self.root,
            font=FONT_UI,
            bg=COLORS["bg_menu"],
            fg=COLORS["fg"],
            tearoff=False,
        )

        options_menu = tk.Menu(
            menubar,
            tearoff=False,
            font=FONT_UI,
            bg=COLORS["bg_menu"],
            fg=COLORS["fg"],
        )
        options_menu.add_command(label="Start logging",       command=self.start_logging)
        options_menu.add_command(label="Stop logging",        command=self.stop_logging)
        options_menu.add_separator()
        options_menu.add_command(label="Clear log",           command=self._log_widget.clear)
        options_menu.add_command(label="Export to TXT",       command=self._export_to_txt)
        options_menu.add_command(label="Copy to clipboard",   command=self._copy_to_clipboard)
        options_menu.add_command(label="Show key statistics", command=self._show_statistics)
        options_menu.add_separator()
        options_menu.add_command(label="Exit",                command=self.root.quit)

        menubar.add_cascade(label="Options", menu=options_menu)
        self.root.config(menu=menubar)

    def _build_statusbar(self) -> None:
        self._status = tk.Label(
            self.root,
            text="Status: inactive",
            bg=COLORS["bg"],
            fg=COLORS["status_inactive"],
            font=FONT_UI,
        )
        self._status.pack(pady=6)

    def start_logging(self) -> None:
        if self._logging:
            return
        self._logging = True
        self._set_status("Status: recording…", COLORS["status_active"])
        try:
            keyboard.on_press(self._on_key_press)
        except Exception as exc:
            self._logging = False
            self._set_status(f"Status: error — {exc}", COLORS["status_error"])

    def stop_logging(self) -> None:
        if not self._logging:
            return
        self._logging = False
        self._set_status("Status: stopped", COLORS["status_stopped"])
        self._unhook()

    def _on_key_press(self, event: keyboard.KeyboardEvent) -> None:
        key_event = KeyEvent.from_keyboard_event(event)
        self._log_widget.append(key_event)

    def _export_to_txt(self) -> None:
        content = self._log_widget.get_content()
        if not content:
            messagebox.showinfo("Export", "There is no captured data to export.")
            return

        default_name = datetime.now().strftime("keystrokes_%Y%m%d_%H%M%S.txt")
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile=default_name,
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if not path:
            return

        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            messagebox.showinfo("Export", f"Export successful:\n{path}")
        except OSError as exc:
            messagebox.showerror("Export error", f"Could not save file:\n{exc}")

    def _copy_to_clipboard(self) -> None:
        content = self._log_widget.get_content()
        if not content:
            messagebox.showinfo("Copy", "There is no captured data to copy.")
            return
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            messagebox.showinfo("Copy", "Log copied to clipboard.")
        except Exception as exc:
            messagebox.showerror("Copy error", f"Could not copy to clipboard:\n{exc}")

    def _show_statistics(self) -> None:
        content = self._log_widget.get_content()
        if not content:
            messagebox.showinfo("Statistics", "No keystrokes were recorded yet.")
            return

        total, sorted_counts = parse_statistics(content)
        StatsWindow(self.root, total, sorted_counts)

    def _set_status(self, text: str, color: str) -> None:
        self._status.config(text=text, fg=color)

    def _unhook(self) -> None:
        try:
            keyboard.unhook_all()
        except Exception:
            pass

    def on_close(self) -> None:
        if self._logging:
            self._unhook()
        self.root.destroy()