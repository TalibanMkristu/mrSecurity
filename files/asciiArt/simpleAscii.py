from colorama import Fore, Back, Style, init
from pyfiglet import Figlet, FigletFont
import os, time, random, sys


# f = Figlet(font='slant')
# print(f.renderText('Taliban'))

"""Initilizing colorama"""
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

"""
Creating a hacker style Ascii art with custom colors
 starting with custom Hacker palettes
"""
HACKER_GREEN = Fore.LIGHTGREEN_EX
HACKER_BG = Back.BLACK
TERMINAL_FONT = 'ansi_shadow' # also doom from pyfiglet

class HackerTerminal():
    def __init__(self):
        self.border_char = '\u2588'
        self.shadow_char = '\u2592'
        self.accent_char = '\u25D8'

    def createBanner(self, text):
        """Hacker style banner with shaddow effect"""
        banner = f"""
        {HACKER_BG}{HACKER_GREEN}
        {self.border_char * 60}
        {self.border_char}{' ' * 58}{self.border_char}
        {self.border_char}{' SYSTEM INITIALIZED '.center(58, self.accent_char)}{self.border_char}
        {self.border_char}{' ' * 58}{self.border_char}
        {self.border_char}{text.center(58)}{self.border_char}
        {self.border_char}{' ' * 58}{self.border_char}
        {self.border_char * 60}
        """
        '''Shadow effect'''
        shadow = f"{' ' * 2}{self.shadow_char * 60}"
        return f"{banner}{shadow}"
    
    """TODO not writing on BG"""
    def typeWriter(slef, text, delay=0.05):
        '''Simualting terminal typing effect'''
        sys.stdout.write(HACKER_BG + HACKER_GREEN)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
            print(Style.RESET_ALL)

class HackerArtGenerator():
    def __init__(self):
        self.fonts = ['ansi_shadow', 'doom', 'ogre', 'slant']
        self.border_char ='\u2588'
        self.shadow_char = '\u2592'
        self.scanline_char = ''
        self.warning_color = Fore.LIGHTRED_EX
        self.text_color = Fore.LIGHTGREEN_EX
        self.bg_color = Back.BLACK
        self.glitch_chars = ['\\', '/', '|', '_', '#', '@', '\u2726']

    def _get_figlet(self,text, font=None):
        '''Initialise figlet with fallback fonts'''
        font = font or random.choice(self.fonts)
        try:
            f =Figlet(font=font, width=80)
            return f.renderText(text)
        except:
            """Fallback font if prefered not available"""
            f = Figlet(font='standard', width=80)
            return f.renderText(text)
        
    def _add_border(self, text, padding=1):
        """add boredr around the text"""
        lines = [line for line in text.split('\n') if line.strip()]
        max_len = max(len(line) for line in lines )

        bordered = []
        top_bottom = self.border_char * (max_len + 2 + padding*2)
        bordered.append(top_bottom)

        for line in lines:
            bordered_line = (
                f'{self.border_char}{' ' * padding}'
                f'{line.ljust(max_len)}'
                f'{' ' * padding}{self.border_char}'
            )
            bordered.append(bordered_line)
        bordered.append(top_bottom)
        return '\n'.join(bordered)
    
    def _add_shadow(self, text, offset = 2):
        '''shadow effect '''
        lines = text.split('\n')
        shadow_lines = []

        for line in lines:
            shadow_line = ' ' * offset + self.shadow_char * len(line)
            combined = f'{line}\n{shadow_line}'
            shadow_lines.append(combined)

        return '\n'.join(shadow_lines)
    
    '''TODO Scanlines not working properly'''
    def _add_scanlines(self, text, density=3):
        '''Add CRT scanline effect '''
        lines = text.split('\n')
        scanline = self.scanline_char * max(len(line) for line in lines)
        result = []

        for i , line in enumerate(lines):
            result.append(line)
            if i % density == 0:
                result.append(f'{Fore.BLACK}{scanline}{Style.RESET_ALL}')

            return '\n'.join(result)
    
    def _glitch_text(self, text, intensity=0.1):
        '''Add glitch effect to text'''
        chars = list(text)
        num_glitches = int(len(chars) * intensity)

        for _ in range(num_glitches):
            idx = random.randint(0, len(chars)-1)
            chars[idx] = random.choice(self.glitch_chars)

        return ''.join(chars)
    
    def generateBanner(self, main_text, sub_text=None, warning=None, effects=True):
        '''Generate complete  hacker art banner'''
        # main ascii 
        ascii_art = self._get_figlet(main_text)
        # add border
        bordered = self._add_border(ascii_art)
        
        # additional text if provided
        full_art = bordered
        if sub_text:
            sub_lines = sub_text.split('\n')
            for line in sub_lines:
                full_art += f'\n{self.border_char} {line.center(len(bordered.split('\n')[0]))} {self.border_char}'

        # warning 
        if warning:
            warning_line = f'\n{self.border_char} {self.warning_color} {warning.center(len(bordered.split('\n')[0]))} {self.border_char}'
            full_art += warning_line

        # close the box 
        full_art += f'\n{self.border_char * len(bordered.split('\n')[0])}'

        # apply effects 
        if effects:
            full_art = self._add_shadow(full_art)
            # full_art = self._add_scanlines(full_art)
            if random.random() > 0.7 : #30% chance of glitch
                full_art = self._glitch_text(full_art)

        # apply colors
        return f'{self.bg_color}{self.text_color}{full_art}{Style.RESET_ALL}'
    
    def animateTyping(self, text, delay=0.03, glitch_chance=0.7):
        '''Simulating terminal typing with possible glitches '''
        sys.stdout.write(f'{self.bg_color}{self.text_color}')
        for char in text:
            if random.random() < glitch_chance:
                # gitch_effect 
                sys.stdout.write(random.choice(self.glitch_chars))
                time.sleep(delay * 2)
                sys.stdout.write(f'{Back.BLACK}{Fore.LIGHTGREEN_EX}{char}') #backspace and correct
            else:
                sys.stdout.write(f"{Back.BLACK}{Fore.LIGHTGREEN_EX}{char}")
            sys.stdout.flush()
            time.sleep(delay)
        print(Style.RESET_ALL)

def main():
    enhancer = EnhancedFiglet()
    # # enhancer.listFonts()
    # text = 'PYTHON'

    # """1. Gradient text"""
    # print(f"\n<< Starting Gradient Text >>")
    # print(enhancer.gradientText(text, font='slant', palette='rainbow'))

    # """2. figlet with border and shadow"""
    # basic = Figlet(font='big').renderText(text)
    # print(f'\n With border and shadow ')
    # bordered = enhancer.addBorder(basic, border_char='\u2726', padding=10)
    # shadowed = enhancer.shadowEffect(bordered)
    # print(Fore.LIGHTCYAN_EX + Back.BLACK + shadowed)

    # """3. Animated """
    # # print("\n Animated figlet")
    # # enhancer.animateText('HELLO', font='slant', speed=0.05)

    terminal = HackerTerminal()
    # '''1. CREATING A BANNER'''
    # print(terminal.createBanner('ACCESS GRANTED'))
    # '''2. SIMULATING A TERMINAL OUTPUT'''
    # terminal.typeWriter('Initialising neural network ...')
    # terminal.typeWriter('Bypassing firewall ...')
    # terminal.typeWriter('Root accss achieved ...')
    # '''3. MAtrix type falling code'''
    # print(f"\n {HACKER_BG}{HACKER_GREEN}")
    # for _ in range(5):
    #     print(" ".join([str(random.randint(0, 1)) for _ in range(20)]))
    # print(Style.RESET_ALL)

    generator = HackerArtGenerator()
    '''1. Generating a banner'''
    banner = generator.generateBanner(
        main_text='CYBERDINE',
        sub_text='System core v3.18',
        warning='WARNING: <<UNAUTHORISED ACCESS DETECTED>>',
        effects=True
    )
    print(banner)
    print(f" {Fore.RED}{Back.BLACK}Initializing systemm ...")
    generator.animateTyping(text="Bypassing Firewall >>>>")
    generator.animateTyping(text="Cracking Encryption ***")
    generator.animateTyping(text="Root acess granted !!!")
    generator.animateTyping(text="BOOOOM !! Loading PAYLOAD")

if __name__ == '__main__':
    main()