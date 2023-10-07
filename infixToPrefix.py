def infix_to_prefix(infix_expression):
    def precedence(operator):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence.get(operator, 0)

    def is_operator(char):
        return char in '+-*/^'

    def reverse_expression(expression):
        return expression[::-1]

    def replace_parentheses(expression):
        return expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    def infix_to_postfix(expression):
        postfix = []
        stack = []
        expression = reverse_expression(expression)
        expression = replace_parentheses(expression)

        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Pop the '('
            elif is_operator(char):
                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(char):
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:
            postfix.append(stack.pop())

        return ''.join(postfix[::-1])

    infix_expression = infix_expression.replace(' ', '')  # Remove spaces
    postfix_expression = infix_to_postfix(infix_expression)
    prefix_expression = reverse_expression(postfix_expression)
    
    return prefix_expression

# Example usage:
infix_expression = "A + B * ( C / D - E )"
prefix_expression = infix_to_prefix(infix_expression)
print("Infix Expression:", infix_expression)
print("Prefix Expression:", prefix_expression)
