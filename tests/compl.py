from typing import List, Tuple

import test
from autocompl.compl import *

class AutoCompleteBaseTest:
    def test(self, auto_compl: AutoComplete, input: str, expected: List[str]):
        # Order does not matter
        assert sorted(auto_compl.get_completions(input)) == sorted(expected)

@test.test
class TestDefaultDictionary(AutoCompleteBaseTest):
    test_cases: List[Tuple[str, List[str]]] = [
        ("appl", [
            "applaud", "applaudable", "applaudably", "applauded", "applauder", "applauders", "applauding",
            "applaudingly", "applauds", "applause", "applauses", "applausive", "applausively", "apple", 
            "applecart", "applecarts", "appledrain", "appledrains", "applejack", "applejacks", "appleringie", 
            "appleringies", "apples", "applesauce", "applesauces", "applet", "applets", "appley", "appliable", 
            "appliance", "appliances", "applicabilities", "applicability", "applicable", "applicableness", 
            "applicably", "applicant", "applicants", "applicate", "application", "applications", "applicative", 
            "applicatively", "applicator", "applicators", "applicatory", "applied", "applier", "appliers", 
            "applies", "applique", "appliqued", "appliqueing", "appliques", "apply", "applying"
        ]),
        ("farmlands", ["farmlands"]),
        ("asdwdacwd", [])
    ]

    def __init__(self):
        self.auto_complete = AutoComplete()

    def test(self, input: str, expected: List[str]):
        super().test(self.auto_complete, input, expected)

@test.test
class TestCustomDictionary(AutoCompleteBaseTest):
    test_cases: List[Tuple[str, List[str], List[str]]] = [
        ("word", ["word", "words"], ["word", "words", "not-a-match"]),
        ("empty", [], ["no-match", "second", "third"])
    ]

    def test(self, input: str, expected: List[str], dictionary: List[str]):
        super().test(AutoComplete(dictionary), input, expected)