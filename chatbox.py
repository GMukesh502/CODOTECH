import spacy
from spacy.matcher import PhraseMatcher
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import json

class SpacyChatbot:
    def __init__(self):
        # Load the English language model
        self.nlp = spacy.load("en_core_web_sm")
        
        # Load knowledge base from JSON file
        with open('knowledge_base.json') as f:
            self.knowledge = json.load(f)
        
        # Initialize the phrase matcher
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
        
        # Prepare patterns for matching
        for intent, data in self.knowledge.items():
            patterns = [self.nlp(text) for text in data['patterns']]
            self.matcher.add(intent, patterns)
        
        # Set up TF-IDF vectorizer for general responses
        self.vectorizer = TfidfVectorizer()
        self.corpus = []
        self.responses = []
        
        for intent, data in self.knowledge.items():
            self.corpus.extend(data['patterns'])
            self.responses.extend(data['responses'] * len(data['patterns']))
        
        self.vectorizer.fit(self.corpus)
    
    def identify_intent(self, user_input):
        doc = self.nlp(user_input.lower())
        matches = self.matcher(doc)
        
        if matches:
            match_id, start, end = matches[0]
            return self.nlp.vocab.strings[match_id]
        return None
    
    def generate_response(self, user_input):
        # First try to match specific intent
        intent = self.identify_intent(user_input)
        
        if intent:
            return random.choice(self.knowledge[intent]['responses'])
        
        # Fall back to TF-IDF similarity for general responses
        query_vec = self.vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(
            query_vec, 
            self.vectorizer.transform(self.corpus)
        )
        best_match_idx = similarity_scores.argmax()
        
        if similarity_scores[0][best_match_idx] > 0.5:
            return self.responses[best_match_idx]
        
        # Default response for unclear queries
        return "I'm not sure I understand. Could you please rephrase that?"