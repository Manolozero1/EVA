import spacy

class NLPManager:
    def __init__(self):
        self.nlp = spacy.load("es_core_news_sm")

    def detect_intent(self, text):
        doc = self.nlp(text)
        if any(token.lemma_ == "mejorar" for token in doc):
            return "improve"
        elif any(token.lemma_ == "entrenar" for token in doc):
            return "train"
        elif any(token.lemma_ in ["buscar", "internet"] for token in doc):
            return "internet_search"
        return "general"

    def generate_response(self, text):
        # Esta función debe generar respuestas basadas en la entrada del usuario
        return f"Has dicho: {text}"