def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if(finished[i] == False):
            answer.append(todo_list[i])
    return answer

solution (["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False])

