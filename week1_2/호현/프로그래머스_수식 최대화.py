from itertools import permutations

def solution(expression):
    result = []
    for permu in permutations(["*", "-", "+"], 3):
        copy_expression = expression
        operator_1, operator_2, _ = permu
        copy_expression = copy_expression.split(operator_1)
        for i in range(len(copy_expression)):
            temp = []
            for j in copy_expression[i].split(operator_2):
                temp.append(str(eval(j)))
            copy_expression[i] = str(eval(operator_2.join(temp)))

        result.append(abs(eval(operator_1.join(copy_expression))))

    return result
        
print(solution("100-200*300-500+20"))