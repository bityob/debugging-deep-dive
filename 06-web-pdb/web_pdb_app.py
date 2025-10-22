from flask import Flask, request

app = Flask(__name__)


def process_data(data):
    # Bug: Assumes all data entries are integers; crashes on non-integer
    total = sum(int(x) for x in data)
    average = total / len(data)  # Potential ZeroDivisionError
    return average


@app.route("/process", methods=["POST"])
def process():
    data = request.json.get("data", [])

    # Breakpoint with open web server for debugging
    import web_pdb

    web_pdb.set_trace()

    result = process_data(data)
    return {"average": result}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4444)
