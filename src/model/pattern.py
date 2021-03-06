
from typing import Iterator
from collections import UserList
from itertools import product

class Pattern:

	def __init__(self, pattern):
		self.pattern = pattern

	@classmethod
	def generate_all_patterns(cls, length) -> Iterator['Pattern']:
		yield from (cls(p) for p in product((0, 1), repeat=length))

	@classmethod
	def generate_all_patterns_with_prefix(cls, prefix, length) -> Iterator['Pattern']:
		yield from (cls(prefix + p) for p in product((0, 1), repeat=length))

	def __iter__(self):
		return iter(self.pattern)

	def __eq__(self, other):
		return self.pattern == other.pattern

	def __hash__(self):
		return self.pattern.__hash__()

	def __str__(self):
		return ''.join('x' if c else ' ' for c in self)
