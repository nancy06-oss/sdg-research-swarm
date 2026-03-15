import google.generativeai as genai

def synthesizer_agent(raw_research: str, topic: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""You are a UN SDG Synthesis Agent.
Topic: {topic}
Research: {raw_research}
Extract: 1) Top 3 insights 2) Root causes 3) Solution gaps 4) SDG targets 5) Interventions
Think step by step."""
    print("[AGENT 2 - SYNTHESIZER] Synthesizing insights...")
    try:
        r = model.generate_content(prompt)
        print(f"[AGENT 2] Done — {len(r.text)} chars")
        return r.text
    except Exception as e:
        print(f"[AGENT 2] Failed: {e} — retrying fallback...")
        return model.generate_content(f"Key points from: {raw_research[:400]}").text
