"""
prompt_handler.py

Contains functions to build and manage prompt templates
for the LLM pipeline. This is where you craft how the
question and context are combined and formatted before
passing to the model.
"""

def build_prompt(question: str, context: str) -> str:
    """
    Constructs an advanced prompt template for the LLM.

    Args:
        question (str): The user's question.
        context (str): The context text where the answer should be found.

    Returns:
        str: Formatted prompt string.
    """
    # Example of adding system instructions and clear structure:
    system_instruction = (
        "You are an AI assistant trained to answer questions "
        "based strictly on the provided context. "
        "Do not use any outside knowledge. "
        "If the answer cannot be found in the context, reply with 'I don't know.'"
    )
    prompt = (
        f"{system_instruction}\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        f"Answer:"
    )
    return prompt
