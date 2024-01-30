import ast

def count_functions_with_return(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    total_functions = 0
    functions_with_answer = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            total_functions += 1

            # Check if the function has a return statement
            has_return = any(isinstance(item, ast.Return) for item in ast.walk(node))
            
            # If the function has a return statement, check if it returns a valid value
            if has_return:
                return_statement = next((item for item in ast.walk(node) if isinstance(item, ast.Return)), None)
                # print(return_statement.value.)
                if return_statement and return_statement.value is not None:
                    return_value_source = ast.get_source_segment(source_code, return_statement.value)
                    if return_value_source != "answer":
                        functions_with_answer += 1


    return total_functions, functions_with_answer

if __name__ == "__main__":
    file_names = [
        "question2.py",
        "question3.py",
        "question4.py",
        "question5.py",
        "question6.py",
        "question7.py",
        "question8.py",
        "question9.py",
        "question10.py"
    ]
    total_functions = 0
    total_answers = 0
    for file_name in file_names:
        try:
            question_functions, question_answers = count_functions_with_return(file_name)
            total_functions += question_functions
            total_answers += question_answers
        except FileNotFoundError:
            print(f"File not found: {file_name}")
        except SyntaxError as e:
            print(f"Syntax error in the file: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    print(f"Answered Questions: {total_answers} / {total_functions}")
    print(f"Percentage Complete: {round(((total_answers / total_functions) * 100), 2)}% ")
