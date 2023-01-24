# Write a Python program to plot a few activation functions that are being used in neural networks

def and_gate(input_nodes):
    if len(set(input_nodes)) == 1 and input_nodes[0] == 1:
        return 1
    return 0
    
def or_gate(input_nodes):
    if 1 in input_nodes:
        return 1
    return 0

def not_gate(input_node):
    return 0 if input_node == 1 else 1

def xor_gate(input_nodes):
    return not_gate(or_gate(input_nodes))



print(f"And gate for input nodes: [1,1,1,1,1]: {and_gate([1,1,1,1,1])}")
print(f"And gate for input nodes: [1,1,1,0,1]: {and_gate([1,1,1,0,1])}")
print(f"OR gate for input nodes: [1,0,0,0,1]: {or_gate([1,0,0,0,1])}")
print(f"OR gate for input nodes: [0,0,0,0,0]: {or_gate([0,0,0,0,0])}")
print(f"XOR gate for input nodes: [1,0,0,0,1]: {xor_gate([1,0,0,0,1])}")
print(f"XOR gate for input nodes: [0,0,0,0,0]: {xor_gate([0,0,0,0,0])}")