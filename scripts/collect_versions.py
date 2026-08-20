#!/usr/bin/env python3
"""Collect key reproducibility versions from the active Python environment."""
import importlib
import platform
import subprocess
import sys

packages = [
    ("tensorflow", "tensorflow"),
    ("keras", "keras"),
    ("numpy", "numpy"),
    ("scikit-learn", "sklearn"),
    ("nibabel", "nibabel"),
    ("scipy", "scipy"),
    ("statsmodels", "statsmodels"),
    ("matplotlib", "matplotlib"),
    ("pandas", "pandas"),
    ("PyYAML", "yaml"),
]

print("Python:", sys.version.replace("\n", " "))
print("Platform:", platform.platform())

for display_name, module_name in packages:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "version attribute unavailable")
        print(f"{display_name}: {version}")
    except Exception as exc:
        print(f"{display_name}: NOT AVAILABLE ({exc})")

print("\nGPU / CUDA information (nvidia-smi):")
try:
    result = subprocess.run(
        ["nvidia-smi"],
        capture_output=True,
        text=True,
        check=False,
        timeout=20,
    )
    print(result.stdout if result.stdout else result.stderr)
except Exception as exc:
    print("nvidia-smi unavailable:", exc)
