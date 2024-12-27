import os
import spacy
import json
from modules.nlp import NLPManager
from modules.voice import VoiceManager
from modules.database import DatabaseManager
from modules.auto_improve import AutoImprover
from modules.auto_train import AutoTrainer
from modules.internet import InternetManager

class EVACore:
    def __init__(self):
        print("Inicializando EVA...")
        self.nlp_manager = NLPManager()
        self.voice_manager = VoiceManager()
        self.database = DatabaseManager("data/eva_memory.db")
        self.knowledge_base = self.load_knowledge_base()
        self.auto_improver = AutoImprover()
        self.auto_trainer = AutoTrainer()
        self.internet_manager = InternetManager()

    def load_knowledge_base(self):
        kb_path = "data/knowledge_base.json"
        if os.path.exists(kb_path):
            with open(kb_path, "r", encoding="utf-8") as kb_file:
                return json.load(kb_file)
        else:
            return {"greetings": ["Hola, soy EVA. ¿En qué puedo ayudarte?"]}

    def process_input(self, user_input):
        intent = self.nlp_manager.detect_intent(user_input)
        if intent == "improve":
            return self.auto_improver.improve_self()
        elif intent == "train":
            return self.auto_trainer.train_with_interactions()
        elif intent == "internet_search":
            return self.internet_manager.search(user_input)
        response = self.nlp_manager.generate_response(user_input)
        self.database.save_interaction(user_input, response)
        return response