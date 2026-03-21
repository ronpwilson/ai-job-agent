# app/tools/keyword_extractor.py

def extract_keywords(text: str):
    words = text.lower().split()
    return list(set([w for w in words if len(w) > 4]))[:30]