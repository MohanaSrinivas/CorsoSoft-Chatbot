from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    if user_message == "hello":
        response = "Hi there! How can I help you today?"
    elif "integer" in user_message:
        response = "Please enter a list of integers (comma-separated):"
    elif all(c.isdigit() or c in {',', ' '} for c in user_message):
        numbers = list(map(int, user_message.split(",")))
        response = (
            f"Sum: {sum(numbers)}<br>"
            f"Maximum: {max(numbers)}<br>"
            f"Minimum: {min(numbers)}<br>"
            f"Reversed List: {list(reversed(numbers))}<br>"
            f"Sorted List: {sorted(numbers)}"
        )
    elif user_message in["thanks","Thanks"]:
        response = "You're welcome! Have a great day!"
    elif user_message in ["bye","Bye"]:
        response = "Goodbye! Have a great day!"
    elif user_message == "help":
        response = "You can ask me to sum a list of integers, find the maximum, minimum"
    else:
        response = "I'm sorry, I didn't understand that. Can you rephrase?"

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
