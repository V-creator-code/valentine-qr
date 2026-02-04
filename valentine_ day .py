from flask import Flask, request
import qrcode

app = Flask(__name__)

# --------- QR CODE ----------
def generate_qr():
    url = "http://127.0.0.1:5000"
    qr = qrcode.make(url)
    qr.save("valentine_qr.png")
    print("💖 QR Code generated: valentine_qr.png")

# --------- QUIZ PAGE ----------
@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        if request.form.get("q1") == "You":
            score += 1
        if request.form.get("q2") == "Forever":
            score += 1
        if request.form.get("q3") == "Yes":
            score += 1

        return f"""
        <html>
        <body style="background:#ffe6f0; text-align:center; font-family:Comic Sans MS;">
        <h1>❤️ Result Time ❤️</h1>
        <h2>You scored {score}/3 🎉</h2>
        <h3>No matter the score…</h3>
        <h1>💍 You are my forever Valentine 💖</h1>
        <p>Love you endlessly 😘</p>
        </body>
        </html>
        """

    return """
    <html>
    <head>
    <style>
        body {
            background: linear-gradient(to bottom right, #ffb6c1, #ffe6f0);
            font-family: 'Comic Sans MS', cursive;
            text-align: center;
            overflow: hidden;
        }
        .heart {
            position: fixed;
            font-size: 24px;
            animation: float 6s linear infinite;
        }
        @keyframes float {
            0% { bottom: -10%; opacity: 1; }
            100% { bottom: 110%; opacity: 0; }
        }
    </style>
    </head>

    <body>
        <h1>💘 Valentine Love Quiz 💘</h1>
        <p>Answer honestly 😍</p>

        <form method="post">
            <p>💖 1. Who owns my heart?</p>
            <input type="radio" name="q1" value="You"> You ❤️<br>
            <input type="radio" name="q1" value="Someone else"> Someone else 😜<br><br>

            <p>💞 2. How long will I love you?</p>
            <input type="radio" name="q2" value="Forever"> Forever ♾️<br>
            <input type="radio" name="q2" value="Till food"> Till food 🍕<br><br>

            <p>💍 3. Will you be my Valentine?</p>
            <input type="radio" name="q3" value="Yes"> Yes ❤️<br>
            <input type="radio" name="q3" value="Always"> Always 💘<br><br>

            <button style="font-size:18px; padding:10px;">Submit ❤️</button>
        </form>

        <!-- Floating Hearts -->
        <script>
            const hearts = ["❤️","💖","💘","💕","😍"];
            setInterval(() => {
                const heart = document.createElement("div");
                heart.className = "heart";
                heart.style.left = Math.random() * 100 + "vw";
                heart.innerText = hearts[Math.floor(Math.random() * hearts.length)];
                document.body.appendChild(heart);
                setTimeout(() => heart.remove(), 6000);
            }, 500);
        </script>
    </body>
    </html>
    """

if _name_ == "_main_":
    generate_qr()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

