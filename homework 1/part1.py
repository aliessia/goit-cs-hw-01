import ast

class ExtendedInterpreter(ast.NodeVisitor):
    def __init__(self):
        self.result = 0

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
        elif isinstance(node.op, ast.Pow):
            return left ** right
        else:
            raise ValueError(f"Unsupported operation: {type(node.op)}")

    def visit_Num(self, node):
        return node.n

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        elif isinstance(node.op, ast.UAdd):
            return +operand
        else:
            raise ValueError(f"Unsupported unary operation: {type(node.op)}")

    def interpret(self, code):
        tree = ast.parse(code)
        return self.visit(tree.body[0].value)

if __name__ == '__main__':
    interpreter = ExtendedInterpreter()
    print(interpreter.interpret("3 - 2 + 5"))  
    print(interpreter.interpret("10 - 5 + 3")) 
    print(interpreter.interpret("7 - 4 + 2"))  
    print(interpreter.interpret("15 - 10 + 5")) 
    print(interpreter.interpret("8 - 3 + 1"))  
