import ast

s = "a:int = 1 + 2\nb = 3\n1+2\nreturn"

tree = ast.parse(s)
print(ast.dump(tree, indent=4))
# compile(tree, filename="<ast>", mode="exec")
