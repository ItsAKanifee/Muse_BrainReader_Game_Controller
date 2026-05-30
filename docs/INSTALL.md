Installation
============

These notes explain how to prepare a development environment for Muse_BrainReader.

Prerequisites
-------------

- Python 3.8 or newer
- `pip` and virtualenv (recommended)

Recommended setup
-----------------

1. Create a virtual environment:

```
python -m venv venv
```

2. Activate the virtual environment (Windows PowerShell):

```
.\venv\Scripts\Activate.ps1
```

3. Install dependencies (if you maintain a `requirements.txt`):

```
pip install -r requirements.txt
```

Notes
-----

- This repository contains a variety of scripts and example games. There is no centralized dependency manifest included by default — inspect individual scripts for specific requirements such as `pygame` or `pylsl`.
- If you plan to use Muse/LSL integration, install `pylsl` (PyPI: `pylsl`) and any platform-specific drivers required by your headset.
