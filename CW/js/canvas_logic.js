// This is the Canvas
const c = document.getElementById("sCanvas");
const ctx = c.getContext("2d");

//(LAB 9)
function generateSpots() {
    clearCanvas();
    let xPos, yPos;
    yPos = 30;

    // (Nested Loop) 
    for (let i = 0; i < 9; i++) {
        xPos = 30;
        for (let j = 0; j < 9; j++) {
            let randomColour = '#' + Math.random().toString(16).substring(2, 8).padStart(6, '0');
            drawCircle(15, xPos, yPos, randomColour);
            xPos += 50;
        }
        yPos += 50;
    }
}

function drawCircle(size, x, y, colour) {
    ctx.beginPath();
    ctx.arc(x, y, size, 0, 2 * Math.PI);
    ctx.fillStyle = colour;
    ctx.fill();
}

//(LAB 8)
function generateMondrian() {
    clearCanvas();
    // Draw a simulation of Mondrian stochastic blocks
    for(let i = 0; i < 5; i++) {
        let w = Math.random() * 200 + 50;
        let h = Math.random() * 200 + 50;
        let x = Math.random() * (c.width - w);
        let y = Math.random() * (c.height - h);
        let colors = ["#ff0000", "#ffcc00", "#0000ff", "#000000", "#ffffff"];
        let randomColor = colors[Math.floor(Math.random() * colors.length)];
        
        ctx.fillStyle = randomColor;
        ctx.fillRect(x, y, w, h);
        ctx.strokeStyle = "black";
        ctx.lineWidth = 5;
        ctx.strokeRect(x, y, w, h);
    }
}

function clearCanvas() {
    ctx.clearRect(0, 0, c.width, c.height);
}