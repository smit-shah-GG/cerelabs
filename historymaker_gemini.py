from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
import spacy
from spacy import displacy
import google.generativeai as genai

# Load the English language model
nlp = spacy.load("en_core_web_sm")

import networkx as nx

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

text_file = r"E:\Work\sem5backups\localdata\google_apikey.txt"

with open(text_file, "r") as f:
    api_key = f.read().strip()
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# import wikipedia sentences
candidate_sentences = pd.read_csv(
    r"E:\Work\sem5backups\init_ipd\ayurveda_usable.csv"
)

df = pd.DataFrame(
    {
        "source": list(
            i.strip() for i in candidate_sentences['source']
        ),
        "edge": list(
            i.strip() for i in candidate_sentences['edge']
        ),
        "target": list(
            i.strip() for i in candidate_sentences['target']
        ),
    }
)

# create a directed-graph from a dataframe
G = nx.from_pandas_edgelist(
    df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph()
)

def return_context(noun):
    x = noun

    sentences = []

    if x in G.nodes:
        neighbor_nodes = list(G.neighbors(x))  # get the list of neighbors of node n
        neighbor_nodes.append(x)  # add node n to the list
        H = G.subgraph(neighbor_nodes)

        neighbor_edges = list(G.edges(x, data=True))

        for u, v, d in neighbor_edges:
            verb = d["edge"]  # get the verb from the edge label
            sentences.append(
                f"{u} {verb} {v}."
            )  # create a sentence with the source, verb,

    return sentences


def get_entities(sentence):
    # Parse the sentence using spaCy
    doc = nlp(sentence)

    # Print the text and label of each noun phrase
    for chunk in doc.noun_chunks:
        print(chunk.text, chunk.label_)

    lister = [i.text for i in doc.noun_chunks]

    for i in lister:
        lisst = i.split(" ")

        if "the" in lisst:
            lisst.remove("the")

        sentence = ""
        for x in lisst:
            sentence = sentence + str(x)

        i = x
    return lister

chat = model.start_chat(history=[])

@app.route("/ask", methods=["POST"])
@cross_origin()
def ask():

    question = str(request.json["question"]) + " Explain in short"

    entities = get_entities(question)

    context = []
    context.append(question)
    for i in entities:
        context.append(return_context(i))

    response = chat.send_message(str(context))


    return jsonify(
        {
            "response": response.text,
            "question": context
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5052)