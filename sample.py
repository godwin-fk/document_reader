def reverse_string(input):
    return input[::-1]

def to_uppercase(input):
    return input.upper()

from langgraph.graph import Graph

wflow = Graph()
wflow.add_node("reverse", reverse_string)
wflow.add_node("uppercase", to_uppercase)
wflow.add_edge("reverse", "uppercase")
wflow.set_entry_point("reverse")
wflow.set_finish_point("uppercase")


flow = wflow.compile()
input_string = "hello world"
result = flow.invoke(input_string)
print(result)  # Output: "DLROW OLLEH"