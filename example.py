from autocompl import compl

auto_compl = compl.AutoComplete()

print(f"Loaded {len(compl.MIN_WORDS)} words")
print(f"Use Ctrl+C to exit")
print("Some words may have too much completions")

inp = input("How many completions would you like to see?(default 20) ")
if not inp.strip():
    inp = "20"

try:
    max_sug = int(inp)
except ValueError:
    print("Not a number, set to 20")
    max_sug = 20

while True:
    word = input("Enter word: ")
    completions = auto_compl.get_completions(word)
    print(f"Found {len(completions)} completions")
    print("\n".join(completions[:max_sug]))