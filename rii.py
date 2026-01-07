#!/usr/bin/env python3
import time
import pyautogui
import sys
import os
import random
import string

# --- CONFIG ---
# Disable default top-left failsafe to avoid GNOME Activities trigger
pyautogui.FAILSAFE = False  

# --- COLORS ---
class C:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

def banner():
    os.system('clear')
    print(f"{C.BLUE}")
    print(r"""
   ███████████   █████ █████
  ░░███░░░░░███ ░░███ ░░███ 
   ░███    ░███  ░███  ░███ 
   ░██████████   ░███  ░███ 
   ░███░░░░░███  ░███  ░███ 
   ░███    ░███  ░███  ░███ 
   █████   █████ █████ █████
  ░░░░░   ░░░░░ ░░░░░ ░░░░░ 
    """)
    print(f"{C.END}{C.RED}{C.BOLD}   Rapid Input Injector v2.1{C.END}\n")

def get_random_string(length=12):
    """Generates random alphanumeric string for Fuzzing."""
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(length))

def check_failsafe():
    """Checks if mouse is in Top-Right corner to kill script."""
    x, y = pyautogui.position()
    width, height = pyautogui.size()
    # If mouse is within 5 pixels of the Top-Right corner
    if x >= width - 5 and y <= 5:
        raise KeyboardInterrupt("Custom Failsafe Triggered")

def main():
    banner()

    try:
        # --- PHASE 1: SELECT MODE ---
        print(f"{C.CYAN}[CONFIG] Select Injection Mode:{C.END}")
        print(f"  {C.GREEN}1.{C.END} Static Payload (Repeats one phrase)")
        print(f"  {C.GREEN}2.{C.END} Dictionary Attack (Cycles through a list)")
        print(f"  {C.GREEN}3.{C.END} Fuzzer (Random garbage data)")
        
        mode_in = input(f"\n{C.BOLD}Select [1-3] > {C.END}")
        
        # Default to 1 if empty
        mode = mode_in if mode_in in ['1', '2', '3'] else '1'

        payload_list = []
        static_payload = ""

        if mode == '1':
            print(f"\n{C.BLUE}[INPUT] Enter word or phrase:{C.END}")
            static_payload = input(f"{C.BOLD}> {C.END}")
        
        elif mode == '2':
            print(f"\n{C.BLUE}[INPUT] Enter words separated by comma (e.g. apple,banana,cherry):{C.END}")
            raw_list = input(f"{C.BOLD}> {C.END}")
            payload_list = [x.strip() for x in raw_list.split(',')]
        
        elif mode == '3':
            print(f"\n{C.MAGENTA}[INFO] Fuzzing mode selected. Random strings will be generated.{C.END}")

        else:
            print(f"{C.RED}Invalid selection. Defaulting to Static.{C.END}")
            static_payload = "TEST_PACKET"

        # --- PHASE 2: CONFIGURATION ---
        print(f"\n{C.CYAN}[CONFIG] Loop Count:{C.END}")
        count_in = input(f"{C.BOLD}> {C.END}")
        count = int(count_in) if count_in else 100

        # --- PHASE 3: TIMING (Jitter Logic) ---
        print(f"\n{C.CYAN}[TIMING] Configure Human Jitter (Anti-Bot):{C.END}")
        print(f"Enter the {C.GREEN}MINIMUM{C.END} delay between messages (seconds):")
        min_in = input(f"{C.BOLD}> {C.END}")
        min_delay = float(min_in) if min_in else 0.1
        
        print(f"Enter the {C.GREEN}MAXIMUM{C.END} delay between messages (seconds):")
        max_in = input(f"{C.BOLD}> {C.END}")
        max_delay = float(max_in) if max_in else 0.5

        print(f"\n{C.YELLOW}[ARMING] Start Delay (seconds)?{C.END}")
        start_in = input(f"{C.BOLD}> {C.END}")
        start_wait = int(start_in) if start_in else 5

        # --- PHASE 4: EXECUTION ---
        print(f"\n{C.YELLOW}--- ARMING IN {start_wait} SECONDS ---{C.END}")
        print(f"{C.YELLOW}--- MOVE MOUSE TO TOP-RIGHT TO KILL ---{C.END}")
        
        for i in range(start_wait, 0, -1):
            check_failsafe() # Check during countdown
            sys.stdout.write(f"\r{C.RED}T-Minus: {i}...{C.END}")
            sys.stdout.flush()
            time.sleep(1)
        
        print(f"\r{C.GREEN}>>> AUTOMATION SEQUENCE STARTED <<<{C.END}             \n")

        for i in range(1, count + 1):
            # 1. SAFETY CHECK (THIS WAS MISSING)
            check_failsafe()

            # 2. Determine Payload
            if mode == '1':
                current_payload = static_payload
            elif mode == '2':
                current_payload = random.choice(payload_list)
            elif mode == '3':
                current_payload = get_random_string(16)

            # 3. Inject
            pyautogui.write(current_payload)
            pyautogui.press('enter')
            
            # 4. Calculate Jitter Delay
            actual_delay = random.uniform(min_delay, max_delay)
            
            # 5. Log
            print(f"{C.GREEN}[{i}/{count}]{C.END} Injected: {C.BOLD}{current_payload}{C.END} {C.MAGENTA}(Delay: {actual_delay:.2f}s){C.END}")
            
            # 6. Sleep
            time.sleep(actual_delay)

        print(f"\n{C.CYAN}Mission Complete.{C.END}")

    except KeyboardInterrupt:
        print(f"\n\n{C.RED}MANUALLY ABORTED (Top-Right Corner or Ctrl+C){C.END}")
    except ValueError:
        print(f"\n{C.RED}Error: Please enter valid numbers.{C.END}")

if __name__ == "__main__":
    main()