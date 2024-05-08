import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def answer_questions():
    faq_data = {
        "cost": "The application is free, with no hidden charges.",
        "lessons": "Lessons are categorized into beginner, intermediate, and advanced levels.",
        "compatibility": "Compatible with Chrome, Firefox, and Safari.",
        "internet": "An internet connection is necessary to use all features.",
        "support": "Contact our support team via email at support@help.com."
    }

    nltk.download('punkt')
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    while True:
        question = input("\nHi there! How can I help you today?\nEnter your question (or just hit enter to quit): ").strip()
        if not question:
            print("\nThank you! Have a good day!")
            break
        
        processed_question = set(lemmatizer.lemmatize(word.lower()) for word in word_tokenize(question) if word.lower() not in stop_words)
        
        for keywords, answer in faq_data.items():
            if any(lemmatizer.lemmatize(kw) in processed_question for kw in keywords.split()):
                print(answer)
                break
        else:
            print("Sorry, I couldn't find an answer to your question. Please try rephrasing.")

if _name_ == "_main_":
    answer_questions()
