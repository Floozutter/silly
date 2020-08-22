"""
A demonstration of using the call stack as an algorithmic stack.

Inspired by Justin Jaffray's blog post:
http://justinjaffray.com/reflections-on-stacking-stacks/
"""

from collections import deque
from enum import Enum
from typing import Dict, List, Tuple, Sequence, Optional


class Bracket(Enum):
	ANGLE_L = "<"
	ANGLE_R = ">"
	CURLY_L = "{"
	CURLY_R = "}"
	ROUND_L = "("
	ROUND_R = ")"
	SQUARE_L = "["
	SQUARE_R = "]"
	@staticmethod
	def list_from_str(s: str) -> List["Bracket"]:
		return [Bracket(c) for c in s]

PAIRS: Dict[Bracket, Bracket] = {
	Bracket("<") : Bracket(">"),
	Bracket("{") : Bracket("}"),
	Bracket("(") : Bracket(")"),
	Bracket("[") : Bracket("]")
}


def balancedA(brackets: Sequence[Bracket]) -> bool:
	"""Uses a collections.deque as a stack."""
	stack = deque()
	for b in brackets:
		if b in PAIRS:
			stack.append(b)
		elif not stack or b != PAIRS[stack.pop()]:
			return False
	return not stack

def balancedB(brackets: Sequence[Bracket], stack: Sequence[Bracket] = ()) -> bool:
	"""Uses a singly linked list parameter as a stack."""
	if not brackets:
		return not stack
	elif brackets[0] in PAIRS:
		return balancedB(brackets[1:], (brackets[0], stack))
	elif stack and brackets[0] == PAIRS[stack[0]]:
		return balancedB(brackets[1:], stack[1])
	else:
		return False

def balancedC(brackets: Sequence[Bracket]) -> bool:
	"""Uses the call stack as a stack."""
	def find(closer: Optional[Bracket], idx: int) -> Optional[int]:
		if idx >= len(brackets):
			return idx if closer is None else None
		elif brackets[idx] in PAIRS:
			jdx = find(PAIRS[brackets[idx]], idx+1)
			return find(closer, jdx+1) if jdx is not None else None
		else:
			return idx if brackets[idx] == closer else None
	return find(None, 0) is not None


if __name__ == "__main__":
	def test(brackets: str, is_balanced: bool) -> None:
		for f in (balancedA, balancedB, balancedC):
			assert f(Bracket.list_from_str(brackets)) == is_balanced, f"f={f}"
	test("", True)
	test("{}", True)
	test("()()", True)
	test("[<>]", True)
	test("<", False)
	test("}", False)
	test("(]", False)
	test("<<><{}>", False)
