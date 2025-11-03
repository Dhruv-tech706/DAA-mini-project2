from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import networkx as nx
import os

app = Flask(__name__)

INF = 99999

# --- City names ---
cities = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore",
    "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
]

# --- Distance graph ---
graph = [
    [0, 10, INF, 30, INF, 25, INF, INF, 35, INF],
    [10, 0, 50, INF, 40, 20, 15, 30, INF, INF],
    [INF, 50, 0, 45, 10, 30, INF, INF, INF, 20],
    [30, INF, 45, 0, 25, 30, INF, 40, 50, INF],
    [INF, 40, 10, 25, 0, 15, 30, INF, INF, 45],
    [25, 20, 30, 30, 15, 0, 10, INF, 35, INF],
    [INF, 15, INF, INF, 30, 10, 0, 30, 40, INF],
    [INF, 30, INF, 40, INF, INF, 30, 0, 20, INF],
    [35, INF, INF, 50, INF, 35, 40, 20, 0, 35],
    [INF, INF, 20, INF, 45, INF, INF, INF, 35, 0]
]

# --- Floyd Warshall algorithm ---
def floyd_warshall():
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# --- Draw graph (simple) ---
def draw_graph():
    G = nx.Graph()
    n = len(cities)

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != INF:
                G.add_edge(cities[i], cities[j], weight=graph[i][j])

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1200, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig("static/graph.png")
    plt.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        from_city = request.form["from_city"]
        to_city = request.form["to_city"]
        return redirect(url_for("result", from_city=from_city, to_city=to_city))
    return render_template("index.html", cities=cities)

@app.route("/result")
def result():
    from_city = request.args.get("from_city")
    to_city = request.args.get("to_city")

    dist = floyd_warshall()
    i, j = cities.index(from_city), cities.index(to_city)
    result = dist[i][j] if dist[i][j] != INF else "No Path Available"

    draw_graph()  # draw simple static graph

    return render_template("result.html",
                           from_city=from_city,
                           to_city=to_city,
                           result=result)

if __name__ == "__main__":
    app.run(debug=True)
