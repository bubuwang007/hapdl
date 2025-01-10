from .._Command import Command
from ..arith_parser._Node_Types import *
from typing import Any
from functools import cached_property

class Number:
    name: str
    pre: str = ""

    @classmethod
    def change_pre(cls, pre: str):
        cls.pre = pre

    @cached_property
    def _node(self):
        return NUMBER(self)

    def __init__(self, name: str):
        self.name = f"{Number.pre}{name}"

    def set(self, value: Any):
        return Command(f"{self.name}={value}")

    def __lshift__(self, value: Any):
        return self.set(value)

    def delete(self):
        return Command(f"{self.name}=")

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self._node+other
    
    def __radd__(self, other):
        return other+self._node

    def __sub__(self, other):
        return self._node-other
    
    def __rsub__(self, other):
        return other-self._node

    def __mul__(self, other):
        return self._node*other
    
    def __rmul__(self, other):
        return other*self._node

    def __truediv__(self, other):
        return self._node/other
    
    def __rtruediv__(self, other):
        return other/self._node

    def __pow__(self, other):
        return self._node**other
    
    def __rpow__(self, other):
        return other**self._node
    
    def __neg__(self):
        return -self._node
    
    def __eq__(self, other):
        return self._node==other
    
    def __ne__(self, other):
        return self._node!=other
    
    def __lt__(self, other):
        return self._node<other
    
    def __gt__(self, other):
        return self._node>other
    
    def __le__(self, other):
        return self._node<=other
    
    def __ge__(self, other):
        return self._node>=other
