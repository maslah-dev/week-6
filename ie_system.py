"""
BIT4133 - NLP | Week 6 Practical
Simple Information Extraction System using spaCy (Named Entity Recognition)
"""
import spacy
 
nlp = spacy.load("en_core_web_sm")
 
# Map spaCy labels to the categories required by the practical
CATEGORY_MAP = {
    "PERSON": "PERSON",
    "ORG": "ORGANIZATION",
    "GPE": "LOCATION",
    "LOC": "LOCATION",
    "FAC": "LOCATION",
    "DATE": "DATE",
    "TIME": "TIME",
    "MONEY": "MONEY",
    "PERCENT": "PERCENTAGE",
    "PRODUCT": "PRODUCT",
    "EVENT": "EVENT",
}
 
TITLES = ("Dr.", "Prof.", "Mr.", "Mrs.", "Ms.")
 
def clean_text(text):
    """Basic preprocessing: collapse whitespace/newlines."""
    return " ".join(text.split())
 
def extract_entities(text):
    """Return a list of (entity text, category) for the given text."""
    doc = nlp(clean_text(text))
    results = []
    for ent in doc.ents:
        name = ent.text
        for t in TITLES:                      # strip titles such as 'Dr.'
            if name.startswith(t):
                name = name[len(t):].strip()
        results.append((name, CATEGORY_MAP.get(ent.label_, ent.label_)))
    return results
 
def show(text):
    print("TEXT:", clean_text(text))
    print(f"{'Entity':<40}{'Category'}")
    print("-" * 55)
    for name, cat in extract_entities(text):
        print(f"{name:<40}{cat}")
    print()
 
if __name__ == "__main__":
    sample = """Dr. Peter Mwangi attended the Artificial Intelligence
    Conference at Mount Kenya University in Thika on
    20 September 2026."""
 
    extra = [
        "Safaricom announced a profit of KSh 50 billion in Nairobi on Monday.",
        "Dr. Jane Wanjiku met the United Nations delegation in Mombasa at 10:00 AM.",
        "Google released a new Pixel phone in California on 5 March 2025.",
        "President William Ruto opened the Konza Technopolis project near Machakos.",
        "Kenya Airways increased ticket prices by 15% for flights to Dubai in December.",
    ]
 
    print("=== SAMPLE INPUT ===")
    show(sample)

    print("=== EXTRA INPUTS ===")
    for text in extra:
        show(text)