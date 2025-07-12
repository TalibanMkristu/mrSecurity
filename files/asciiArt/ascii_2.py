import random
import sys
import time
from colorama import Fore, Back, Style, init

class HackerTerminal:
    def __init__(self):
        init(autoreset=True)
        self.text_color = Fore.LIGHTGREEN_EX
        self.bg_color = Back.BLACK
        self.warning_color = Fore.LIGHTRED_EX
        self.glitch_chars = ['\\', '/', '|', '_', '#', '@', '*']
    
    def _write_with_style(self, text):
        """Helper to write text with hacker colors"""
        sys.stdout.write(f"{self.bg_color}{self.text_color}{text}")
        sys.stdout.flush()
    
    def animate_typing(self, text, delay=0.03, glitch_chance=0.1):
        """Simulate terminal typing with glitch effects"""
        self._write_with_style("")  # Set initial colors
        
        for char in text:
            if random.random() < glitch_chance:
                # Glitch effect (red)
                sys.stdout.write(f"{Fore.RED}{random.choice(self.glitch_chars)}")
                sys.stdout.flush()
                time.sleep(delay * 2)
                # Correct with original colors
                sys.stdout.write(f"\b{self.bg_color}{self.text_color}{char}")
            else:
                sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        
        # Ensure colors persist after this line
        sys.stdout.write(f"{self.bg_color}{self.text_color}")
        sys.stdout.flush()

    def print_line(self, text):
        """Print a line with hacker colors"""
        self._write_with_style(text + "\n")

# Example usage
if __name__ == "__main__":
    terminal = HackerTerminal()
    
    # Initial message
    terminal.print_line("Initializing system...\n")
    
    # Animated lines
    terminal.animate_typing("> Bypassing firewall...")
    terminal.print_line("")  # New line
    
    terminal.animate_typing("> Cracking encryption...")
    terminal.print_line("")  # New line
    
    terminal.animate_typing("> Root access achieved!")
    terminal.print_line("")  # New line
    
    # Final message (with color reset)
    terminal.print_line("System ready." + Style.RESET_ALL)

from contextlib import contextmanager

class HackerTerminal(HackerTerminal):
    @contextmanager
    def hacker_style(self):
        """Context manager for hacker colors"""
        sys.stdout.write(f"{self.bg_color}{self.text_color}")
        try:
            yield
        finally:
            sys.stdout.write(Style.RESET_ALL)
    
    def animate_typing(self, text, delay=0.03, glitch_chance=0.1):
        with self.hacker_style():
            for char in text:
                if random.random() < glitch_chance:
                    sys.stdout.write(f"{Fore.RED}{random.choice(self.glitch_chars)}")
                    time.sleep(delay * 2)
                    sys.stdout.write(f"\b{char}")
                else:
                    sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write("\n")

 