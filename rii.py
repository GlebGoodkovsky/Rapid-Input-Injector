#!/usr/bin/env python3
import time
import pyautogui
import sys
import os

# --- CONFIG ---
pyautogui.FAILSAFE = True  # Slam mouse to Top-Left corner to FORCE STOP

# --- COLORS ---
class C:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
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
    print(f"{C.END}{C.RED}{C.BOLD}     Rapid Input Injector{C.END}\n")

def main():
    banner()

    try:
        # 1. INPUTS
        print(f"{C.CYAN}[INPUT]{C.END} Enter payload string to inject:")        
        message = input(f"{C.BOLD}> {C.END}")

        print(f"\n{C.CYAN}[INPUT]{C.END} How many times?")
        count = int(input(f"{C.BOLD}> {C.END}"))

        print(f"\n{C.CYAN}[INPUT]{C.END} Delay between messages (seconds)?")
        delay = float(input(f"{C.BOLD}> {C.END}"))

        print(f"\n{C.CYAN}[INPUT]{C.END} Delay before starting (seconds)?")
        start_wait = int(input(f"{C.BOLD}> {C.END}"))

        # 2. COUNTDOWN
        print(f"\n{C.YELLOW}--- ARMING IN {start_wait} SECONDS ---{C.END}")
        print(f"{C.YELLOW}--- FOCUS TARGET WINDOW NOW ---{C.END}")
        
        for i in range(start_wait, 0, -1):
            sys.stdout.write(f"\r{C.RED}T-Minus: {i}...{C.END}")
            sys.stdout.flush()
            time.sleep(1)
        
        print(f"\r{C.GREEN}>>> AUTOMATION SEQUENCE STARTED <<<{C.END}             \n")

        # 3. INJECTION LOOP
        for i in range(1, count + 1):
            # The Action
            pyautogui.write(message)
            pyautogui.press('enter')
            
            # The Log
            print(f"{C.GREEN}[{i}/{count}]{C.END} Sent: {C.BOLD}{message}{C.END}")
            
            # The Wait
            time.sleep(delay)

        print(f"\n{C.CYAN}Mission Complete.{C.END}")

    except KeyboardInterrupt:
        print(f"\n\n{C.RED}MANUALLY ABORTED (Ctrl+C){C.END}")
    except pyautogui.FailSafeException:
        print(f"\n\n{C.RED}FAILSAFE TRIGGERED (Mouse -> Top Left){C.END}")
    except ValueError:
        print(f"\n{C.RED}Error: Please enter valid numbers.{C.END}")

if __name__ == "__main__":
    main()