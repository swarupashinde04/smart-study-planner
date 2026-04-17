from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    plan = []
    break_time = 0

    if request.method == "POST":

        subjects = request.form["subjects"].split(",")
        hours = float(request.form["hours"])
        priority = request.form["priority"]

        if priority == "high":
            hours = hours * 0.5
        elif priority == "medium":
            hours = hours * 0.3
        else:
            hours = hours * 0.2

        time_per_subject = hours / len(subjects)

        for subject in subjects:

            plan.append({
                "subject": subject.strip(),
                "time": round(time_per_subject,2)
            })

        break_time = round(len(subjects) * 0.1,2)

    return render_template("index.html", plan=plan, break_time=break_time)

app.run(debug=True)
