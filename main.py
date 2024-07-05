import json,re
from langgraph.graph import Graph
from groq import Groq
from pdfminer.high_level import extract_text
from json_format import output_map
def extract_text_from_pdf(input):
    try:
        text = extract_text(input[0])
        return (text,input[1])
    except Exception as e:
        print(f"An error occurred: {e}")
        return (None,input[1])  

def llm_call(input):
    client = Groq(
        api_key = "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"
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"You are a tool designed for a specific purpose. Your task is to analyze the body of text delimited by three backticks ```{input[0]}``` and the JSON object delimited by three commas ,,,{input[1]},,,. Find suitable values for the keys in the JSON object from the text body. If you find appropriate values, replace the default values in the JSON object. If not, retain the default value as N/A. Return only the updated JSON object."
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

wflow=Graph()
wflow.add_node("nodeA",extract_text_from_pdf)
wflow.add_node("nodeB",llm_call)
wflow.add_edge("nodeA","nodeB")
wflow.set_entry_point("nodeA")
wflow.set_finish_point("nodeB")

flow = wflow.compile()
pdf_path = './Booking Confirmation - CMA CGM - 484691 - LYK0158261.pdf'
result = flow.invoke((pdf_path, output_map))

json_data = str(re.search(r'{.*}', result, re.DOTALL).group())
data = json.loads(f'''{json_data}''')
print(data)
output_path = 'output2.json'
with open(output_path, 'w') as f:
    json.dump(data, f, indent=4)
print(json_data)
