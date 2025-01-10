class NODE:
    def _trans_to_node(self, other):
        if isinstance(other, NODE):
            return other
        elif hasattr(other, "_node"):
            return other._node
        return EXPRESSION(other)

    def __add__(self, other):
        return PLUS(self, self._trans_to_node(other))

    def __radd__(self, other):
        return self._trans_to_node(other).__add__(self)

    def __sub__(self, other):
        return MINUS(self, self._trans_to_node(other))

    def __rsub__(self, other):
        return self._trans_to_node(other).__sub__(self)

    def __mul__(self, other):
        return TIMES(self, self._trans_to_node(other))

    def __rmul__(self, other):
        return self._trans_to_node(other).__mul__(self)

    def __truediv__(self, other):
        return DIVIDE(self, self._trans_to_node(other))

    def __rtruediv__(self, other):
        return self._trans_to_node(other).__truediv__(self)

    def __pow__(self, other):
        return POWER(self, self._trans_to_node(other))

    def __rpow__(self, other):
        return self._trans_to_node(other).__pow__(self)

    def __neg__(self):
        return NEG(self)

    def __eq__(self, other):
        return EQEQ(self, self._trans_to_node(other))
    
    def __ne__(self, other):
        return NEQ(self, self._trans_to_node(other))
    
    def __lt__(self, other):
        return LT(self, self._trans_to_node(other))

    def __gt__(self, other):
        return GT(self, self._trans_to_node(other))
    
    def __le__(self, other):
        return LE(self, self._trans_to_node(other))
    
    def __ge__(self, other):
        return GE(self, self._trans_to_node(other))


class NUMBER(NODE):
    priority = 0

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number.name


class EXPRESSION(NODE):
    priority = 0

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return str(self.expr)


class PLUS(NODE):
    priority = 4

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        if self.left.priority > self.priority:
            left = f"({self.left})"
        else:
            left = str(self.left)
        if self.right.priority > self.priority:
            right = f"({self.right})"
        else:
            right = str(self.right)
        return f"{left}+{right}"


class MINUS(NODE):
    priority = 4

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        if self.left.priority > self.priority:
            left = f"({self.left})"
        else:
            left = str(self.left)
        if self.right.priority > self.priority:
            right = f"({self.right})"
        else:
            right = str(self.right)
        return f"{left}-{right}"


class TIMES(NODE):
    priority = 3

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        if self.left.priority > self.priority:
            left = f"({self.left})"
        else:
            left = str(self.left)
        if self.right.priority > self.priority:
            right = f"({self.right})"
        else:
            right = str(self.right)
        return f"{left}*{right}"


class DIVIDE(NODE):
    priority = 3

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        if self.left.priority > self.priority:
            left = f"({self.left})"
        else:
            left = str(self.left)
        if self.right.priority > self.priority:
            right = f"({self.right})"
        else:
            right = str(self.right)
        return f"{left}/{right}"


class POWER(NODE):
    priority = 1

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        if self.left.priority > self.priority:
            left = f"({self.left})"
        else:
            left = str(self.left)
        if self.right.priority > self.priority:
            right = f"({self.right})"
        else:
            right = str(self.right)
        return f"{left}**{right}"


class NEG(NODE):
    priority = 2

    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        if self.expr.priority > self.priority:
            return f"-({self.expr})"
        return f"-{self.expr}"


class EQEQ(NODE):
    priority = 5

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left},EQ,{self.right}"


class NEQ(NODE):
    priority = 5

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left},NE,{self.right}"


class LT(NODE):
    priority = 5

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left},LT,{self.right}"


class GT(NODE):
    priority = 5

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left},GT,{self.right}"


class LE(NODE):
    priority = 5

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left},LE,{self.right}"


class GE(NODE):
    priority = 5

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left},GE,{self.right}"
