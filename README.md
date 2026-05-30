# Muse_BrainReader

Overview
--------

Muse_BrainReader is an experimental collection of Python scripts and small games demonstrating basic Muse EEG headset input integration. The project started as a high-school experiment to use Muse-derived signals as game controllers.

Highlights
----------

Has many issues, but the was able to have the headset communicate with my computer and send a somewhat interperable EEG signal. I atttempted making three working games: Flappy Bird, Pong, and Tower Stacker (there are some other games that I could not get done). I used joke names in a futile attempt to be funny.

Quickstart
----------

1. Create and activate a Python virtual environment (Python 3.8+ recommended).
2. See docs/INSTALL.md for environment setup details.
3. Run an example entrypoint, for example:

```
python Main.py
```

Behavior Notes
--------------

- Flappy Bird and Tower Stacker use delta-band deviations triggered by blinks as control signals.
- Pong uses beta-band signals intended for focus-based control; it may require tuning and is known to be less stable.
- This repository is experimental: signal processing, weights, and responsiveness may need further tuning.

Credits
-------

This project builds on work from projects such as PyLSL and MuseLSL (https://github.com/alexandrebarachant/muse-lsl), and tools like Petal Metrics (https://petal.tech/).

Documentation
-------------

Detailed setup and usage instructions are in the `docs/` folder included with this repository.
