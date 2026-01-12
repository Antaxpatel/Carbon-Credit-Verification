from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

# Temporary in-memory storage for prototype
verification_history = []

def calculate_ndvi(lat, lon):
    """
    Prototype NDVI logic (mocked but realistic)
    """
    ndvi_before = round(random.uniform(0.2, 0.4), 2)
    ndvi_after = round(ndvi_before + random.uniform(0.1, 0.3), 2)
    ndvi_change = round(ndvi_after - ndvi_before, 2)

    verified = ndvi_change >= 0.2

    explanation = (
        "Vegetation increase detected. Plantation verified."
        if verified
        else "Vegetation increase insufficient."
    )

    return ndvi_before, ndvi_after, ndvi_change, verified, explanation


@app.route("/verify", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        lat = float(request.form["latitude"])
        lon = float(request.form["longitude"])
        location = request.form["location"]
        area = request.form.get("area", "0") 
        radius = request.form.get("radius", "1000") # Get radius, default 1000
        if not radius or radius == "":
            radius = "1000"
        time_period = request.form.get("time_period", "1y") # Get time period

        ndvi_before, ndvi_after, ndvi_change, verified, explanation = calculate_ndvi(lat, lon)

        # Save to history
        verification_history.insert(0, {
            "date": datetime.now().strftime("%b %d, %H:%M %p"),
            "project_id": f"PRO-{random.randint(100, 999)}",
            "location": location,
            "area": area,
            "ndvi_change": ndvi_change,
            "result": "Verified" if verified else "Rejected",
            "status_class": "verified" if verified else "rejected"
        })

        return render_template(
            "verification.html",
            latitude=lat,
            longitude=lon,
            location=location,
            area=area,
            radius=radius,
            time_period=time_period,
            ndvi_before=ndvi_before,
            ndvi_after=ndvi_after,
            ndvi_change=ndvi_change,
            result="VERIFIED ✅" if verified else "REJECTED ❌",
            explanation=explanation,
            show_results=True
        )

    return render_template("verification.html")


@app.route("/verification", methods=["GET", "POST"])
def verification_alias():
    return index()

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/calculator")
def calculator():
    return render_template("calculator.html")


@app.route("/history")
def history():
    return render_template("history.html", history=verification_history)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
