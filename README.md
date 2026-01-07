# Rapid Input Injector

A lightweight, terminal-based automation tool designed for rapid text injection. Built with Python and `pyautogui`, it features a custom TUI (Text User Interface) with gradient aesthetics and zero restriction logic.

---

## Features
- **High Performance:** No hard-coded limits on speed or message count.
- **Visual Interface:** Custom ASCII banner with RGB gradient rendering.
- **Configurable Logic:** Precise control over start delay and interval delay.
- **Safety Failsafe:** Integrated "Panic Switch" to abort execution instantly.

---

## Prerequisites
- Python 3.x
- `pyautogui` library
- X11 or XWayland (if running on Linux)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/GlebGoodkovsky/Rapid-Input-Injector.git
cd rapid-input-injector
```

2. **Make executable**

```bash
chmod +x rii.py
```

---

## Usage

Run the script directly from your terminal:

```bash
./rii.py
```

**Configuration Steps:**
1.  **Payload:** Enter the text string to inject.
2.  **Count:** Number of iterations.
3.  **Interval:** Delay in seconds between injections.
4.  **Arming:** Delay in seconds before the script begins typing.

*Once the countdown finishes, the script will type the payload and press ENTER automatically.*

---

## Emergency Stop (Failsafe)

If the script is running too fast to stop via keyboard:

**Slam your mouse cursor into the top-left corner of the screen.**
*(Coordinate 0,0)*

This triggers the `pyautogui` failsafe exception and kills the process instantly.

---

## Disclaimer
This tool is intended for testing input fields, load testing chat applications, and automation tasks. The user is responsible for where this script is pointed.

---

### Important Note

Developed utilizing AI-assisted workflows for rapid prototyping and code optimization, demonstrating modern pair-programming methodologies

---