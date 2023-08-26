def dateToDay(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):
    answer = []
    ## today
    today = dateToDay(today)

    ## terms
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1]) * 28
        
    ##privacies
    for index, privacy in enumerate(privacies):
        parts2 = privacy.split(" ")
        date = parts2[0]
        print(date)
        type = parts2[1]
        if(dateToDay(date) + termsInfo[type] <=today):
            answer.append(index + 1)
            
    return answer