def question_change(question,word,guess):
    quest=""
    if guess in word:
        l_question=[i for i in question]
        l_word=[i for i in word]
        for i in range (len(question)):
            if guess==word[i]:
                l_question[i]=guess
            quest=quest+l_question[i]
    return quest
