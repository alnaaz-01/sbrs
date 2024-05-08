import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def question_answer():
    print("Hello there what can i help you?")
    fqa ={
        "hii":"Hello, what can i help you",
       "python":"python langauage",
       "help":"help"
        }
    stop_words = set(stopwords.words("english"))
    le = WordNetLemmatizer()
    while True:
        question = input("you:- ")
        if not question.strip():
            print("Bot: Thank you! Have a good day!")
            break
        pro_que= [le.lemmatize(word.lower()) for word in word_tokenize(question) if word not in stop_words]

        found_match = False

        for keyword , answer in fqa.items():
            le_ke = [le.lemmatize(key) for key in keyword.split()]

            for key in le_ke:
                if key in pro_que:
                    found_match=True
                    best_match=answer
                    break
            if found_match:
                break

        if found_match:
            print("Bot:- ",best_match)
        else:
            print("Bot:Sorry, I couldn't find an answer to that question.")

question_answer()
