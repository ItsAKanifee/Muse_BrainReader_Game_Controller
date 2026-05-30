Project structure
=================

This document describes the repository layout and purpose of key files/folders.

Top-level
---------

- `Main.py` — primary runner script (example entrypoint)
- `Game.py`, `Viewer.py`, `Scanner.py` — supporting utilities and demos
- `README.md` — project overview (this file)

Folders
-------

- `Game_Folder/` — contains example games and subfolders for each game
- `lib/` — native or third-party libraries (included for build or packaging support)
- `Muse_Reader_Assets/` — Muse EEG reader scripts and helpers (Calibrate, Reader, utils)

Notes
-----

Explore individual scripts to find specific run patterns — many modules are small demos rather than a single integrated application.
