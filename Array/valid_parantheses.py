'''
given a str that contaains only characters (){}[]
example ouput : 
input : () -> output : True
input : ()[]{} -> output : True
input : (] -> output : False
input : ({)} -> output : False
input : ([]) -> output : True
'''

s=''
def valid_paranthesis(s):
    stack = []
    if not s:
        return False
    for char in s:
        if char == '(':
            stack.append(')')
        elif char == '{':
            stack.append('}')
        elif char == '[':
            stack.append(']')
        elif not stack or stack.pop() != char:
            return False
    return not stack

print(valid_paranthesis(s))


# ===================== WORKFLOW =====================
# Uses a stack to validate bracket pairs
# 1. If string is empty -> return False
# 2. Loop through each character:
#    - '(' -> push ')' onto stack
#    - '{' -> push '}' onto stack
#    - '[' -> push ']' onto stack
#    - Closing bracket:
#        If stack is empty OR stack.pop() != char -> return False
# 3. After loop: if stack is empty -> True (all matched)
#                if stack has items -> False (unmatched open brackets)
# Examples:
#   "()"     -> push ')' -> pop ')' == ')' -> stack empty -> True
#   "(]"     -> push ')' -> pop ')' != ']' -> False
#   "([])"   -> push ')', push ']' -> pop ']'==']', pop ')'==')' -> True
#   ""       -> empty string -> False
# Time Complexity : O(n) | Space Complexity : O(n)
# =====================================================