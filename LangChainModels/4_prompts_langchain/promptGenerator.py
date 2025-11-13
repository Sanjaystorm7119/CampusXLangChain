from langchain.prompts import PromptTemplate

template = PromptTemplate(
    template='''
Please summarize the following research paper in a {style_input} style with a {length_input} length:
Paper: {paper_input}
1. Mathematical concepts:
- include relevant equations and their explanations
- provide examples of how these concepts are applied in the paper
2. Analogies:
- use analogies to explain complex concepts in a simple way

if certain information is not available in the paper, please state that "insufficient information".
ensure that the summary is comprehensive and covers all key points of the paper with proper style and length .
''',
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True #automatically validate placeholders
)

template.save("template.json")