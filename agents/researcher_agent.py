import google.generativeai as genai

def researcher_agent(topic: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""You are a UN SDG Research Agent.
Topic: {topic}
Provide: 1) Key facts 2) Global challenges 3) Affected populations 4) SDG goal numbers
Think step by step. Use clear headers."""
    print("[AGENT 1 - RESEARCHER] Gathering intelligence...")
    try:
        r = model.generate_content(prompt)
        print(f"[AGENT 1] Done — {len(r.text)} chars")
        return r.text
    except Exception as e:
        print(f"[AGENT 1] Failed: {e} — retrying fallback...")
        return model.generate_content(f"Basic SDG facts about {topic}").text
