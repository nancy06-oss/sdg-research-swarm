import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.researcher_agent  import researcher_agent
from agents.synthesizer_agent import synthesizer_agent
from agents.report_agent      import report_agent
from tools.file_tool          import save_report
from datetime import datetime

def run_swarm(topic: str, api_key: str):
    print("\n" + "="*55)
    print("  SDG RESEARCH SWARM — AGENTVERSE ACTIVATED")
    print("="*55)
    print(f"MISSION : {topic}")
    print(f"START   : {datetime.now().strftime('%H:%M:%S')}\n")

    print("--- PHASE 1: RESEARCH ---")
    research = researcher_agent(topic, api_key)
    if len(research) < 50:
        print("[SWARM] Too short — replanning...")
        research = researcher_agent(f"overview of {topic} and SDGs", api_key)

    print("\n--- PHASE 2: SYNTHESIS ---")
    synthesis = synthesizer_agent(research, topic, api_key)
    if len(synthesis) < 50:
        print("[SWARM] Too short — using research fallback...")
        synthesis = f"Summary: {research[:300]}"

    print("\n--- PHASE 3: REPORT ---")
    report = report_agent(research, synthesis, topic, api_key)

    print("\n--- PHASE 4: SAVING ---")
    save_report(topic, report)

    print("\n" + "="*55)
    print("MISSION COMPLETE")
    print("="*55)
    print(report)
    return report

if __name__ == "__main__":
    KEY   = os.getenv("GEMINI_API_KEY", "")
    TOPIC = "Clean Water Access in Rural Communities"
    run_swarm(TOPIC, KEY)
