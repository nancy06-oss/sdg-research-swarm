import google.generativeai as genai

def report_agent(research: str, synthesis: str, topic: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""You are a UN SDG Policy Report Agent.
Topic: {topic}
Research: {research}
Synthesis: {synthesis}
Write a report with these sections:
# SDG IMPACT REPORT: {topic.upper()}
## Executive Summary
## SDG Alignment
## Problem Analysis
## Key Insights
## Recommended Actions (5 steps)
## Success Metrics
## Conclusion"""
    print("[AGENT 3 - REPORT WRITER] Writing report...")
    try:
        r = model.generate_content(prompt)
        print(f"[AGENT 3] Done — {len(r.text)} chars")
        return r.text
    except Exception as e:
        print(f"[AGENT 3] Failed: {e} — retrying fallback...")
        return model.generate_content(f"Brief SDG policy report about {topic}").text
