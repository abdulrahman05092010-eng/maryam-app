memory = []

def remember(text):
    memory.append(text)
    if len(memory) > 30:
        memory.pop(0)
