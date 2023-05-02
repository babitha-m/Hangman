def form_question(word):#form the question word shown to the user
    word=word.lower()
    question=""
    for i in word:
        if i not in ["a","e","i","o","u"]:
            question=question+"_"
        else:
            question=question+i
    return question
