Special characters for programming 
Box drawing (frames and boreders)
# Single line
    '\u2500'  # ─ Horizontal
    '\u2502'  # │ Vertical
    '\u250C'  # ┌ Top-left
    '\u2510'  # ┐ Top-right
    '\u2514'  # └ Bottom-left
    '\u2518'  # ┘ Bottom-right
    '\u251C'  # ├ Left T
    '\u2524'  # ┤ Right T
    '\u252C'  # ┬ Top T
    '\u2534'  # ┴ Bottom T
    '\u253C'  # ┼ Center +

# Double line
    '\u2550'  # ═ Horizontal
    '\u2551'  # ║ Vertical
    '\u2554'  # ╔ Top-left
    '\u2557'  # ╗ Top-right
    '\u255A'  # ╚ Bottom-left
    '\u255D'  # ╝ Bottom-right

shade/blocks (shadows/texures)

    '\u2591'  # ░ Light shade
    '\u2592'  # ▒ Medium shade
    '\u2593'  # ▓ Dark shade
    '\u2588'  # █ Full block
    '\u2580'  # ▀ Upper half block
    '\u2584'  # ▄ Lower half block
    '\u258C'  # ▌ Left half block
    '\u2590'  # ▐ Right half block


Decorative elements
# Stars
    '\u2605'  # ★ Filled star
    '\u2606'  # ☆ Outline star
    '\u2726'  # ✦ Four-pointed star
    '\u2727'  # ✧ Four-pointed star (outline)
    '\u2736'  # ✶ Six-pointed star
    '\u2739'  # ✹ Twelve-pointed star

# Other symbols
    '\u2665'  # ♥ Heart
    '\u2666'  # ♦ Diamond
    '\u2663'  # ♣ Club
    '\u2660'  # ♠ Spade
    '\u263A'  # ☺ Smiley
    '\u263B'  # ☻ Smiley (filled)
    '\u2764'  # ❤ Heart (modern)

Practical usage examples snippets
1. Box with shadow
    box = (
        '\u250C\u2500\u2500\u2500\u2500\u2510\n'
        '\u2502 Hello \u2502\n'
        '\u2514\u2500\u2500\u2500\u2500\u2518\n'
        '  \u2591\u2591\u2592\u2592'
    )
    print(box)

2. Fancy title with stars
    title = f"\u2726\u2726\u2726 PYTHON \u2726\u2726\u2726"
    print(title)

3. Progress bar

    def progress_bar(percent):
        filled = '\u2588' * int(percent/5)
        empty = '\u2591' * (20 - int(percent/5))
        return f"[{filled}{empty}] {percent}%"

Tips for usage with color effects 

    from colorama import Fore
    print(Fore.RED + '\u2665' + Fore.RESET)  # Colored heart

    function for reusable components

    def make_box(text):
        length = len(text) + 2
        top = '\u250C' + '\u2500'*length + '\u2510'
        middle = '\u2502 ' + text + ' \u2502'
        bottom = '\u2514' + '\u2500'*length + '\u2518'
        return f"{top}\n{middle}\n{bottom}"