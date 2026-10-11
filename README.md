# Supply Chain Integrity Monitor

A Python-based security tool designed to detect unauthorized
modifications to trusted software files using SHA-256 hashing.

## Overview

The Supply Chain Integrity Monitor helps detect potential software
supply chain attacks by creating cryptographic fingerprints of trusted
files and comparing them against their current state.

The system can detect:

- File modifications
- File deletion
- Integrity violations
- Potential software supply chain tampering

## Features

- SHA-256 file hashing
- Trusted file registration
- File integrity verification
- Missing file detection
- Scan logging
- Command-line interface

## Technologies

- Python
- SHA-256
- hashlib
- JSON
- File Integrity Monitoring (FIM)

## How It Works

Trusted File
    ↓
Calculate SHA-256
    ↓
Store Trusted Hash
    ↓
Verify Later
    ↓
Compare Hashes
    ↓

Same Hash → SAFE

Different Hash → WARNING

Missing File → WARNING

## Run the Project

```bash
python main.py
