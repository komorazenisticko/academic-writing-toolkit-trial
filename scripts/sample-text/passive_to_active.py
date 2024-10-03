import re
def passive_to_active(sentence):
    # Check for a simple passive voice pattern and convert
    pattern = r'\b(is|was|were|are|be|been)\s+(\w+ed)\b'
    return re.sub(pattern, r'\2', sentence)
# Test the function
print(passive_to_active("The paper was written by John."))
