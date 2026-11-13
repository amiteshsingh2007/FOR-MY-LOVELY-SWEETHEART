from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>For My Angel ❤️</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #050505;
    color: white;
    font-family: Georgia, serif;
    overflow: hidden;
}

.page {
    display: none;
    height: 100vh;
    height: 100svh;
    width: 100%;
    position: relative;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
    padding: 25px;
    animation: fade 1s ease;
}

.page.active {
    display: flex;
}

@keyframes fade {
    from { opacity: 0; }
    to { opacity: 1; }
}

h1 {
    color: #ff1744;
    font-size: clamp(32px, 7vw, 60px);
    margin-bottom: 25px;
    text-shadow: 0 0 20px red;
}

p {
    font-size: 20px;
    line-height: 1.7;
    max-width: 650px;
}

button {
    padding: 15px 32px;
    margin-top: 30px;
    background: #e50932;
    border: 1px solid #ff4968;
    color: white;
    border-radius: 30px;
    font-size: 17px;
    cursor: pointer;
    box-shadow: 0 0 20px #e50932;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.08);
    background: #ff1744;
}

/* INTRO VIDEO */

#page0 {
    padding: 25px;
    overflow: hidden;
}

.intro-video {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    z-index: 0;
}

#page0::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        rgba(0,0,0,0.35),
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.70)
    );
    z-index: 1;
    pointer-events: none;
}

.intro-content {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 750px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

#page0 h1 {
    font-size: clamp(35px, 6vw, 65px);
    margin-bottom: 18px;
}

#page0 p {
    font-size: clamp(15px, 2vw, 20px);
    line-height: 1.6;
    color: white;
    text-shadow: 0 2px 10px black;
}

/* PHOTO PAGES */

.photo-page {
    background-size: contain;
    background-position: center;
    background-repeat: repeat-x;
}

.photo-page::before {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.62);
}

.content {
    position: relative;
    z-index: 2;
    max-width: 750px;
}

.reason {
    font-size: clamp(25px, 5vw, 40px);
    line-height: 1.5;
    text-shadow: 0 0 15px red;
}

.counter {
    margin-top: 20px;
    color: #ff4968;
}

/* NO BUTTON MOVEMENT */

#page24 {
    overflow: hidden;
}

#noButton {
    position: relative;
    z-index: 10;
    transition:
        left 0.25s ease,
        top 0.25s ease,
        opacity 0.15s ease;
}

/* MUSIC BUTTON */

.music-btn {
    position: fixed;
    top: 15px;
    right: 15px;
    z-index: 100;
    margin: 0;
    padding: 10px 18px;
    font-size: 14px;
}

/* FLOATING HEARTS */

.hearts {
    position: fixed;
    bottom: -30px;
    color: red;
    font-size: 25px;
    animation: float 6s linear forwards;
    pointer-events: none;
    z-index: 5;
}

@keyframes float {
    to {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}

/* RESPONSE */

#response {
    color: #ff4968;
    font-size: 22px;
    margin-top: 25px;
    line-height: 1.7;
}

.reaction {
    animation: funnyPop 0.6s ease;
}

@keyframes funnyPop {
    0% {
        transform: scale(0.5) rotate(-5deg);
        opacity: 0;
    }

    60% {
        transform: scale(1.15) rotate(3deg);
        opacity: 1;
    }

    100% {
        transform: scale(1);
    }
}

/* EMOJI EFFECT */

.emoji-effect {
    position: fixed;
    pointer-events: none;
    z-index: 200;
    font-size: 30px;
    animation: emojiFly 2s ease-out forwards;
}

@keyframes emojiFly {
    0% {
        transform: translateY(0) scale(0.5);
        opacity: 1;
    }

    100% {
        transform: translateY(-250px) rotate(360deg) scale(1.5);
        opacity: 0;
    }
}

/* MOBILE */

@media (max-width: 600px) {

    #page0 {
        padding: 15px;
    }

    .intro-content {
        padding: 10px;
    }

    #page0 h1 {
        font-size: 36px;
    }

    #page0 p {
        font-size: 15px;
    }

    button {
        padding: 12px 25px;
        font-size: 15px;
    }

    .music-btn {
        top: 10px;
        right: 10px;
    }

}

</style>

</head>

<body>

<!-- MUSIC PLAYER -->

<audio id="music" preload="auto">

    <source
        src="{{ url_for('static', filename='music/music.m4a') }}"
        type="audio/mp4">

</audio>

<button class="music-btn"
id="musicButton"
onclick="toggleMusic()">

🎵 Music OFF

</button>


<!-- PAGE 0 : WELCOME -->

<section class="page active" id="page0">

    <video class="intro-video"
    autoplay muted loop playsinline>

        <source
        src="{{ url_for('static', filename='videos/intro.mp4') }}"
        type="video/mp4">

    </video>

    <div class="intro-content">

        <h1>Hey My Angel ❤️</h1>

        <p>

            Some people enter our lives and make everything
            more beautiful.

            <br><br>

            And then there is YOU.

            <br><br>

            I have something special for you.
            A little surprise from my heart.

        </p>

        <button onclick="startWebsite()">

            Open My Heart ❤️

        </button>

    </div>

</section>


<!-- PAGE 1 : YOUR PHOTO -->

<section class="page photo-page"
id="page1"
style="background-image:url('/static/images/myphoto.jpeg')">

    <div class="content">

        <h1>22 Reasons</h1>

        <h1>Why I Like You ❤️</h1>

        <p>

            22 pictures, 22 reasons,
            and one very special person.

        </p>

        <button onclick="nextPage()">

            Let's Begin ❤️

        </button>

    </div>

</section>


<!-- 22 REASONS -->

{% for i in range(1, 23) %}

<section class="page photo-page"
id="page{{ i+1 }}"
style="background-image:url('/static/images/angel{{ i }}.jpg')">

    <div class="content">

        <h1>Reason {{ i }} ❤️</h1>

        <div class="reason" id="reason{{ i }}"></div>

        <div class="counter">{{ i }} / 22</div>

        {% if i < 22 %}

        <button onclick="nextPage()">

            Next Reason ❤️

        </button>

        {% else %}

        <button onclick="nextPage()">

            One Last Question 💍

        </button>

        {% endif %}

    </div>

</section>

{% endfor %}


<!-- FINAL PROPOSAL PAGE -->

<section class="page"
id="page24"

style="background-image:
linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.75)),
url('{{ url_for('static', filename='images/proposal.jpeg') }}');

background-size: contain;
background-position: center;
background-repeat: no-repeat;
background-color: black;">

    <h1>Will You Marry Me? 💍</h1>

    <p>

        I don't know what the future holds,
        but I would love to create beautiful
        memories together.

        ❤️

    </p>

    <button onclick="yesAnswer()">

        Of Course! ❤️

    </button>

    <button id="noButton" onclick="noAnswer()">

        No 😂

    </button>

    <div id="response"></div>

</section>


<script>

/* =================================
   PAGE NAVIGATION
================================= */

let currentPage = 0;

function showPage(number) {

    document.querySelectorAll(".page").forEach(page => {

        page.classList.remove("active");

    });

    const target = document.getElementById("page" + number);

    if (target) {

        target.classList.add("active");

        currentPage = number;

    }

}

function nextPage() {

    if (currentPage < 24) {

        showPage(currentPage + 1);

    }

}


/* =================================
   MUSIC PLAYER
================================= */

const music = document.getElementById("music");

const startTime = 28;

const endTime = 130;

const musicButton = document.getElementById("musicButton");


function updateMusicButton(isPlaying) {

    musicButton.innerText = isPlaying
        ? "🎵 Music ON"
        : "🎵 Music OFF";

}


async function playMusic() {

    try {

        if (music.currentTime < startTime ||
            music.currentTime >= endTime) {

            music.currentTime = startTime;

        }

        await music.play();

        updateMusicButton(true);

    }

    catch (error) {

        console.log("Music error:", error);

        updateMusicButton(false);

    }

}


function startWebsite() {

    showPage(1);

    playMusic();

}


function toggleMusic() {

    if (music.paused) {

        playMusic();

    }

    else {

        music.pause();

        updateMusicButton(false);

    }

}


/* STOP MUSIC AT 2:45 */

music.addEventListener("timeupdate", function() {

    if (music.currentTime >= endTime) {

        music.pause();

        music.currentTime = startTime;

        updateMusicButton(false);

    }

});


music.addEventListener("ended", function() {

    updateMusicButton(false);

});


/* =================================
   22 REASONS
================================= */

let reasons = [

    "Your beautiful smile makes my day.",

    "The way you care about me.",

    "Your cute little talks.",

    "Your beautiful personality.",

    "The way you make me smile.",

    "Your innocence.",

    "Your lovely voice.",

    "The way you understand me.",

    "Your little habits.",

    "Your beautiful eyes.",

    "The happiness you bring.",

    "Your kindness.",

    "The way you make ordinary moments special.",

    "Your honesty.",

    "The way you make me laugh.",

    "Your adorable nature.",

    "The way you listen to me.",

    "Your beautiful heart.",

    "Every little thing about you.",

    "The memories we create together.",

    "Because you are so special.",

    "Simply because you are YOU. ❤️"

];


reasons.forEach((reason, index) => {

    const element = document.getElementById(
        "reason" + (index + 1)
    );

    if (element) {

        element.innerText = reason;

    }

});


/* =================================
   PROPOSAL ANSWERS
================================= */

let noCount = 0;


/* YES BUTTON */

function yesAnswer() {

    document.getElementById("response").innerHTML =

        "You just made this moment special! ❤️💍";

    document.getElementById("noButton").style.display = "none";

}


/* NO BUTTON MOVEMENT */

function moveNoButton() {

    const proposal = document.getElementById("page24");

    const noBtn = document.getElementById("noButton");

    const padding = 20;

    // Button ko absolute position dena

    noBtn.style.position = "absolute";

    noBtn.style.margin = "0";

    // Proposal slide ke dimensions

    const maxX = proposal.clientWidth -
                 noBtn.offsetWidth - padding;

    const maxY = proposal.clientHeight -
                 noBtn.offsetHeight - padding;

    // Random position calculate karna

    const randomX = padding +
        Math.random() * Math.max(0, maxX - padding);

    const randomY = padding +
        Math.random() * Math.max(0, maxY - padding);

    // Pehle button gayab hoga

    noBtn.style.opacity = "0";

    setTimeout(() => {

        // Nayi position

        noBtn.style.left = randomX + "px";

        noBtn.style.top = randomY + "px";

        // Phir appear hoga

        noBtn.style.opacity = "1";

    }, 150);

}


/* NO MESSAGES */

const noMessages = [

    "WHATTT! 😭 Itni jaldi reject? Meri presentation toh abhi shuru hui thi! 😂",

    "Madam, ek baar aur soch lo! Maine itni mehnat se website banayi hai! 🥺",

    "Mera confidence abhi bhi zinda hai! 💀😂",

    "Lagta hai meri presentation weak thi! Next time PowerPoint bhi banaunga! 🤣",

    "Angel ji, aap toh bahut strict nikli! 😂❤️",

    "Okay, you win! Lekin aapka sense of humour kamaal hai! 😂",

    "NO ka button itna pasand aa gaya kya? 😭",

    "Plot twist: Aapka answer important hai, Madam! ❤️",

    "Haha! Theek hai, main haar maan leta hoon! 😂❤️",

    "Last dialogue: Thank you for being you, Angel! ❤️"

];


/* NO BUTTON CLICK */

function noAnswer() {

    noCount++;

    let response = document.getElementById("response");

    let message = noMessages[
        (noCount - 1) % noMessages.length
    ];

    response.classList.remove("reaction");

    void response.offsetWidth;

    response.classList.add("reaction");

    response.innerHTML =

        "<h2>NO. " + noCount + " 😂</h2>" +

        "<p>" + message + "</p>";


    // EMOJI ANIMATION

    let emojis = ["😭", "😂", "💀", "❤️", "🥺", "🤣"];

    for (let i = 0; i < 8; i++) {

        let emoji = document.createElement("div");

        emoji.className = "emoji-effect";

        emoji.innerText =
            emojis[Math.floor(Math.random() * emojis.length)];

        emoji.style.left = Math.random() * 100 + "vw";

        emoji.style.bottom = "20px";

        document.body.appendChild(emoji);

        setTimeout(() => {

            emoji.remove();

        }, 2000);

    }


    // NO BUTTON KO NAYI JAGAH BHEJNA

    moveNoButton();

}


/* =================================
   FLOATING HEARTS
================================= */

function createHeart() {

    let heart = document.createElement("div");

    heart.className = "hearts";

    heart.innerHTML = "❤️";

    heart.style.left = Math.random() * 100 + "vw";

    heart.style.animationDuration =

        (4 + Math.random() * 4) + "s";

    document.body.appendChild(heart);

    setTimeout(() => {

        heart.remove();

    }, 8000);

}


setInterval(createHeart, 600);


</script>

</body>

</html>

"""


@app.route("/")
def home():

    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(debug=True)