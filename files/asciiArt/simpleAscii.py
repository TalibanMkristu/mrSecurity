from colorama import Fore, Back, Style, init
from pyfiglet import Figlet, FigletFont
import os, time, random


# f = Figlet(font='slant')
# print(f.renderText('Taliban'))

init(autoreset=True)
class EnhancedFiglet():
    def __init__(self):
        self.available_fonts = FigletFont.getFonts()
        self.default_font = 'standard'
        self.color_palettes = {
            'fire': [Fore.RED, Fore.YELLOW, Fore.LIGHTRED_EX],
            'ice': [Fore.CYAN, Fore.BLUE, Fore.LIGHTCYAN_EX],
            'rainbow': [
                Fore.RED, Fore.YELLOW, Fore.GREEN,
                Fore.CYAN, Fore.BLUE, Fore.MAGENTA
            ]
        }
    
    def listFonts(self):
        """To display all available fonts with samples"""
        print(f"\n {Fore.CYAN}Available fonts ({len(self.available_fonts)}):")
        for i, font in enumerate(self.available_fonts[:10]):
            print(f"{i+1}. {font}")
        print(f"{Style.DIM}Showing first ten of ({len(self.available_fonts)})")
    
    def previewFont(self, font_name , text='FontPreview'):
        """Preview how font looks like befogre using it"""
        try:
            f = Figlet(font=font_name)
            print(f"{Fore.GREEN}Font preview: <<{font_name}>>")
            print(f.renderText(text))
            return True
        except Exception as err:
            print(f'{Fore.RED}Font ({font_name}) not found!!')
            print(f"Reason: {err}")
            return False
        
    def gradientText(self, text, font=None ,palette='rainbow'):
        """Create a gradient colored text"""
        font = font or self.default_font
        figlet = Figlet(font=font)
        ascii_art = figlet.renderText(text)

        colored_lines = []
        colors = self.color_palettes.get(palette ,self.color_palettes['rainbow'])

        for i, line in enumerate(ascii_art.split('\n')):
            color = colors[i % len(colors)]
            colored_lines.append(color + line)

        return '\n'.join(colored_lines)
    
    def animateText(self, text, font=None, speed=0.1):
        """Animate text appearance character by character"""
        font = font or self.default_font
        figlet = Figlet(font=font)
        ascii_art = figlet.renderText(text)

        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(ascii_art)):
            print(ascii_art[i], end='\r')
            time.sleep(speed)
        print(ascii_art)

    def addBorder(self, ascii_text, border_char='\u2726', padding=1):
        """Adding decorative border around ascii"""
        lines = ascii_text.split('\n')
        max_length = max(len(line) for line in lines)

        border_line = border_char * (max_length + 2 + padding*2)
        padded_lines = [
            f"{border_char}{' ' * padding}{line.ljust(max_length)}{' ' * padding}{border_char}"
            for line in lines
        ]
        return '\n'.join([border_line] + padded_lines + [border_line])
    
    def shadowEffect(self, ascii_text, offset=2, shadow_char=''): #\u2591
        """Creating 3d shadow effect"""
        lines = ascii_text.split('\n')
        shadow_lines = []

        for line in lines:
            shadow_line = ' ' * offset + shadow_char *  len(line)
            combined = f"{line}\n{shadow_line}"
            shadow_lines.append(combined)
    
        return '\n'.join(shadow_lines)
        


if __name__ == '__main__':
    enhancer = EnhancedFiglet()
    # enhancer.listFonts()
    text = 'PYTHON'

    """1. Gradient text"""
    print(f"\n<< Starting Gradient Text >>")
    print(enhancer.gradientText(text, font='slant', palette='rainbow'))

    """2. figlet with border and shadow"""
    basic = Figlet(font='big').renderText(text)
    print(f'\n With border and shadow ')
    bordered = enhancer.addBorder(basic, border_char='\u2726', padding=10)
    shadowed = enhancer.shadowEffect(bordered)
    print(Fore.LIGHTCYAN_EX + Back.BLACK + shadowed)

    """3. Animated """
    # print("\n Animated figlet")
    # enhancer.animateText('HELLO', font='slant', speed=0.05)

    """
    Features to add enhancer

    >>font combination
    >>advanced color system
    >>Export options
    >>Dynamic effects
    >>Font health check

    """
class HackerTerminal():
    pass