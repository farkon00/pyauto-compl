from typing import Iterable

TEST_MODULES = [
    "compl"
]

def test(cls):
    instance = cls()
    if not hasattr(cls, "test_cases"):
        raise AttributeError(f"Attribute test_cases is missing from test class {cls.__name__}")
    if not isinstance(instance.test_cases, Iterable):
        raise TypeError(f"Attribute test_cases isn't iterable in test class {cls.__name__}")
    if not hasattr(cls, "test"):
        raise AttributeError(f"Method test is missing from test class {cls.__name__}")

    results = []
    for test_case in instance.test_cases:
        if not isinstance(test_case, Iterable):
            raise TypeError(f"Attribute test_cases must only contain iterables in test class {cls.__name__}")
        name = next(iter(test_case))
        try:
            instance.test(*test_case)
            results.append((name, None))
        except AssertionError as e:
            results.append((name, e))
    
    escape = "\u001b["
    is_pass = True
    output = ""
    for result in results:
        if result[1] is not None:
            is_pass = False
            output += f"{escape}91;1m✗ {result[0]}"
            if len(result[1].args) == 1:
                output += f" : {result[1].args[0]}"
            elif len(result[1].args) != 0:
                output += f" : {result[1].args}"
            output += f"{escape}0m\n"
        else:
            output += f"{escape}92;1m🗸 {result[0]}{escape}0m\n"
    output = "\n" + output
    output = output.replace("\n", "\n  ")
    output = f"{f'{escape}92;1m🗸' if is_pass else f'{escape}91;1m✗'} {cls.__name__}{escape}0m" + output

    print(output)

    return cls

if __name__ == "__main__":
    for module_path in TEST_MODULES:
        __import__(module_path)