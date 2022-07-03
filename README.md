# Pyauto-compl

__Pyauto-compl__ - library for auto complete in Python. It comes with set of standard english words for quick start.

It uses prefix tree data structure for better performance.

# Quick start
```shell
pip install pyauto-compl
```

```python
from autocompl.compl import AutoComplete 

compl = AutoComplete() # Gonna load minified words, around 274411 words
print("Loaded words")
completions = compl.get_completions("appl") # Returns list of completions
print(completions)
```
