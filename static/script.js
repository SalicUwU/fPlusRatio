function toggleDM() {
    let element = document.getElementById("bg");
    let element2 = document.getElementById("container");
    let element3 = document.getElementById("button")
    element.classList.toggle("light-mode-bg");
    element2.classList.toggle("light-mode-container");
    element3.classList.toggle("light-mode-button");
}

function toggleChatBox() {
    let button = document.getElementById("button2");
    let chatBox = document.getElementById("chatBox");
    button.style.display = "none";
    chatBox.style.display = "inline-block";
}

function lookup() {
    let chatBox = document.getElementById("chatBox")
    let input = chatBox.value
    window.location.replace("/lookup?IP=" + input)
}

let input = document.getElementById("chatBox")
input.addEventListener("keyup", function(event) {
    if (input.style.display === "inline-block") {
        if (event.key === "Enter") {
            event.preventDefault();
            lookup();
        }
    }
    else {
        console.log("lol")
    }
}); 