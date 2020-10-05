def balanced_parenthesis(list_of_parentheses):
	open_brackets = ['(', '[', '{']
	stack = []
	for parenthesis in list_of_parentheses:
		if parenthesis in open_brackets:
			stack.append(parenthesis)
		else:
			if not stack:
				return False
			current_parenthesis = stack.pop()
			if current_parenthesis == '(':
				if parenthesis != ')':
					return False
			if current_parenthesis == '{':
				if parenthesis != '}':
					return False
			if current_parenthesis == '[':
				if parenthesis != ']':
					return False
	if stack:
		return False
	return True

if __name__ == "__main__" :  
    expr = ""  
    if balanced_parenthesis(expr): 
        print("Balanced") 
    else : 
        print("Not Balanced")  