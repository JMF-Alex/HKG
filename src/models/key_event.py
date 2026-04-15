from __future__ import annotations

from datetime import datetime

import keyboard

from src.config.settings import SPECIAL_KEYS


class KeyEvent:
    __slots__ = ("timestamp", "display", "tag")

    def __init__(self, timestamp: str, display: str, tag: str) -> None:
        self.timestamp = timestamp
        self.display = display
        self.tag = tag


    @classmethod
    def from_keyboard_event(cls, event: keyboard.KeyboardEvent) -> KeyEvent:
        key = event.name.lower()
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

        if key in SPECIAL_KEYS:
            display, tag = SPECIAL_KEYS[key]
        elif key.startswith("f") and key[1:].isdigit():
            display, tag = key, "function"
        elif len(key) > 1:
            display, tag = f"[{key}]", "special"
        else:
            display, tag = key, "normal"

        return cls(timestamp, display, tag)


    def __repr__(self) -> str:
        return f"KeyEvent(timestamp={self.timestamp!r}, display={self.display!r}, tag={self.tag!r})"