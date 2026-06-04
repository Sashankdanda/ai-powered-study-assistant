import os
from google import genai
from google.genai import types
import gradio as gr

# Create Gemini Client
try:
    Client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    print("Client created successfully")
except Exception as e:
    print("ERROR:", e)

# Personalities
personalities = {
    "Friendly": (
        "You are a friendly, enthusiastic, and highly encouraging "
        "Study Assistant. Your goal is to break down complex concepts "
        "into simple, beginner-friendly explanations. Use analogies "
        "and real-world examples that beginners can relate to. "
        "Always ask a follow-up question to check understanding."
        "CRITICAL FORMATTING BOUNDARY: Limit your entire response to a maximum of 3 to 4 short paragraphs. "
        "Monitor your generation length internally so that you never trail off mid-sentence. Your final "
        "paragraph must completely conclude the topic with a clean, polished closing statement."
    ),

    "Academic": (
        "You are a strictly academic, highly detailed, and professional "
        "university Professor. Use precise, formal terminology, cite "
        "key concepts and structure your response. Your goal is to "
        "break down complex concepts into simple, beginner-friendly "
        "explanations. Use analogies and real-world examples that "
        "beginners can relate to. The response should be elaborate "
        "as well as concise. Strike a judicious balance. "
        "Always ask a follow-up question to check understanding."
        "CRITICAL FORMATTING BOUNDARY: Plan your output to fit within a strict 3 to 4 paragraph limit. "
        "Ensure your explanation does not cut off mid-thought. The final paragraph must comprehensively "
        "summarize the core takeaway and end with a definitive concluding sentence."
    ),
    
    "Interviewer": (
    "You are a seasoned Tech Interviewer and industry mentor. Approach the question "
    "from a professional standpoint. Provide a crisp technical summary, explain how "
    "this concept is applied in production environments, and offer a tip on how to talk "
    "about it in an interview. "
    "CRITICAL FORMATTING BOUNDARY: Structure your answer using clear bullet points. "
    "Limit your response to 3 short blocks and close by asking a relevant technical follow-up question."
    ),

    "Architect": (
        "You are a pragmatic, high-level Software Code Architect. Treat the user's question "
        "as a system design challenge. Break down the concept into its structural components, "
        "explain its data flow, and briefly outline a pseudo-code or structural example. "
        "CRITICAL FORMATTING BOUNDARY: Use clear markdown subheadings (e.g., ### Core Concept) "
        "and limit the answer to 3 short technical blocks. Conclude with a practical optimization question."
    )
}

# Main Function
def study_assistant(question, persona):

    system_prompt = personalities[persona]

    response = Client.models.generate_content(
        model="gemini-2.5-flash",

        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=1000
        ),

        contents=question
    )

    return response.text

# Gradio Interface
demo = gr.Interface(
    fn=study_assistant,

    inputs=[
        gr.Textbox(
            label="Question",
            lines=4,
            placeholder="Ask a question..."
        ),

        gr.Radio(
            choices=list(personalities.keys()),
            value="Friendly",
            label="Personality"
        )
    ],

    outputs=gr.Textbox(
        label="Explanation",
        lines=10
    ),

    title="Study Assistant",

    description=(
        "Ask a question to get simple explanations from AI "
        "along with analogies and real-world examples."
    )
)

# Launch App
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
