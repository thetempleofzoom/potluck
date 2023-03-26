import streamlit as sl
#fp = "tobrings.txt"

def reading(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def writing(todos, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos)
    return todos


def claimed():
    if sl.session_state["claimform"]:
        todo = sl.session_state["claimform"]
        todos.append(todo+"\n")
        defs.writing(todos, filepath)
        sl.session_state["claimform"] = ""