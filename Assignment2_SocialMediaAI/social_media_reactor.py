import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma4:e4b"

# --- CURATED LINKEDIN POST ---
LINKEDIN_POST = {
    "author": "Engineering Director & Tech Recruiter",
    "timestamp": "1 day ago",
    "caption": """Hot take: LeetCode algorithmic interviews are officially obsolete in 2026. 

If a candidate can use an AI coding agent to spin up a production-ready microservice in 10 minutes, why are we still quizzing senior devs on abstract dynamic programming problems? 

We need to shift technical hiring toward system architecture, security auditing, and code review skills instead of whiteboard memorization. Thoughts? 

#SoftwareEngineering #TechHiring #ArtificialIntelligence #CodingInterviews #WebDev""",
    "overlay_text_in_image": "Tech Hiring Shift: 78% of engineering leads now prioritize system design over algorithmic tests.",
    "metrics": {
        "likes": 2450,
        "comments_count": 512,
        "reposts": 184
    },
    "sample_comments": [
        "User A: Spot on! Memorizing sorting algorithms has zero correlation with building scalable systems.",
        "User B: Hard disagree. If you don't understand the underlying data structures, you won't even know when your AI agent writes buggy O(n^2) code.",
        "User C: The real question is how companies plan to test AI literacy without making interviews entirely subjective."
    ]
}

# --- PROMPT SPECIFICATION FOR ASSIGNMENT #2 ---
prompt = f"""
You are an expert Social Media AI Analyst. Analyze the following LinkedIn post across 5 specific layers, then generate 6 distinct reaction comments.

LINKEDIN POST DATA:
- Author: {LINKEDIN_POST['author']} ({LINKEDIN_POST['timestamp']})
- Caption: "{LINKEDIN_POST['caption']}"
- Image Overlay Text: "{LINKEDIN_POST['overlay_text_in_image']}"
- Engagement Metrics: {LINKEDIN_POST['metrics']['likes']} Likes, {LINKEDIN_POST['metrics']['comments_count']} Comments, {LINKEDIN_POST['metrics']['reposts']} Reposts
- Sample Comments: {json.dumps(LINKEDIN_POST['sample_comments'])}

PART 1: 5-LAYER ANALYSIS
Provide a clear analysis for each layer:
1. Content and Semantic Understanding: Parse main caption, sample comments, and image overlay text.
2. Sentiment and Emotion Identification: Detect overall sentiment (positive, negative, neutral, or mixed) and dominant emotions.
3. Entity and Intent Recognition: Identify key entities (brands, tools, concepts) and the author's primary intent.
4. Content and Metadata Integration: Analyze engagement metrics, hashtags, and reach to evaluate post virality and audience impact.
5. Risk, Moderation, and Safety Filtering: Flag potential policy violations, misinformation risk, or toxic outrage-baiting.

PART 2: 6 REACTION COMMENTS
Generate 6 distinct comments tailored to LinkedIn. To make them human-like, use realistic tone, conversational phrasing, natural punctuation, professional nuances, or intentional internet colloquialisms where appropriate.

1. Value-Add: Demonstrate expertise, add data, or offer actionable insight.
2. Experience Share: Share a personal/professional story or anecdote to build trust.
3. Respectful Challenge: Offer a constructive counterpoint or alternative perspective.
4. Discussion Starter: Ask an engaging question inviting the author to elaborate.
5. Supportive / Social: Brief, encouraging network presence and goodwill.
6. The Disruptor (Troll): A volatile, sarcastic, or outrage-farming comment designed to derail or provoke reaction.

Format the output cleanly using Markdown headers.
"""

def query_ollama(prompt_text):
    data = {
        "model": MODEL_NAME,
        "prompt": prompt_text,
        "stream": False
    }
    req = urllib.request.Request(
        OLLAMA_URL, 
        data=json.dumps(data).encode('utf-8'), 
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        return result.get("response", "")

if __name__ == "__main__":
    print("Sending curated LinkedIn post to local Gemma 4 model via Ollama...\n")
    response_text = query_ollama(prompt)
    print("=== GEMMA 4 ANALYSIS & REACTION OUTPUT ===")
    print(response_text)