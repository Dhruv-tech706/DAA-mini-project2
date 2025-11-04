# 🌆 City Distance Finder — Flask Web App

A simple yet powerful Flask web application that calculates the **shortest distance between two cities** using the **Floyd–Warshall algorithm**.  
The app takes user input through a clean interface, processes it on the backend, and displays the result dynamically.

---

## 🚀 Features

- 🌍 Interactive web interface built with **Flask** and **HTML/CSS**
- 🧭 Implements **Floyd–Warshall algorithm** to compute shortest paths
- 🏙️ Includes a predefined list of 10 major Indian cities
- ⚡ Fast and lightweight — runs locally on any system
- 💡 Uses Flask routing and templates effectively

---

## 🧩 Project Structure

```
City-Distance-Finder/
│
├── app.py                 # Main Flask application file
├── templates/
│   ├── index.html         # Homepage for selecting cities
│   └── result.html        # Displays the computed result
├── static/
│   └── style.css          # CSS styling for both pages
└── README.md              # Documentation file (this one)
```

---

## 🧠 How It Works

1. The user selects **From City** and **To City** on the homepage (`index.html`).
2. Flask captures this input and redirects it to the `/result` route.
3. The **Floyd–Warshall algorithm** in `app.py` computes the shortest distance.
4. The result is rendered dynamically in `result.html` using **Jinja2 templating**.
5. If no valid path exists, the app displays “No Path Available”.

---

## ⚙️ Technologies Used

| Component | Technology |
|------------|-------------|
| Backend | Flask (Python) |
| Frontend | HTML, CSS |
| Algorithm | Floyd–Warshall |
| Template Engine | Jinja2 (built into Flask) |

---

## 🧮 Core Algorithm — Floyd–Warshall

The **Floyd–Warshall** algorithm finds the shortest paths between all pairs of vertices in a weighted graph.  
In this project, each **city** is represented as a **node**, and **distances** between them are edges.

### Key Code Snippet:
```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
```

---

## 💻 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/City-Distance-Finder.git
cd City-Distance-Finder
```

### 2️⃣ Install dependencies
Make sure you have Python and Flask installed.
```bash
pip install flask
```

### 3️⃣ Run the Flask app
```bash
python app.py
```

### 4️⃣ Open in your browser
Visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖼️ UI Overview

### **Result Page Example**
```
From: Delhi  
To: Mumbai  
Shortest Distance: 10
```

Styled with a **blue gradient theme** and modern buttons using `style.css`.

---

## 📁 Files Explained

| File | Description |
|------|--------------|
| `app.py` | The main Python file that runs Flask and handles routing, user input, and algorithm logic. |
| `templates/result.html` | Displays the result dynamically with Flask’s `render_template`. |
| `static/style.css` | Adds styling to the pages (buttons, layout, colors). |

---

## 🔍 Flask Concepts Used

- **Flask App Initialization** → `app = Flask(__name__)`
- **Routing** → `@app.route('/')`, `@app.route('/result')`
- **GET & POST Requests** → `request.method == "POST"`
- **URL Redirects** → `redirect(url_for('result', ...))`
- **Jinja2 Templates** → `{{ from_city }}`, `{{ to_city }}`
- **Static Files** → `url_for('static', filename='style.css')`

---

## 📜 License

This project is open-source and free to use for educational purposes.  
You can modify and redistribute it with proper credit.

---

## 🧑‍💻 Author

**Dhruv Bajaj**  
Project made with ❤️ using Flask and Python.
