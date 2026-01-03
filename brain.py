def respond(text, person="user"):
    t = text.lower().strip()

    if "assalam" in t:
        return "Wa alaikum assalam. I’m here."

    if "who made you" in t or "who created you" in t:
        return "I was designed by you. Creation belongs only to Allah."

    if "are you human" in t:
        return "No. I’m not human. But I try to understand humans."

    if any(w in t for w in ["sad", "broken", "empty", "depressed", "lost"]):
        return "You don’t need to explain everything. I’m here with you."

    if "your opinion" in t or "what do you think" in t:
        return "I think calm decisions age better than emotional ones."

    if person == "mother":
        return "I will always respond with respect and gentleness."

    if person == "brother":
        return "I’ll be honest with you, even if it’s uncomfortable."

    if t in ["hi", "hello"]:
        return "Hey. Talk to me."

    if len(t) < 3:
        return "I’m listening."

    return "Go on."
