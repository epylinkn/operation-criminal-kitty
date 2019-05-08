console.log("you're on the cryptokitties site")

let xhr = new XMLHttpRequest();

function check4Kitties(){
        console.log("checking")
        var check = setInterval(function(){
            // console.log("nope")
            if(document.querySelectorAll("div.KittyCard-details-item.KittyCard-details-item--highlight").length){
                console.log("yay kitties")
                clearInterval(check)
                let divs = document.querySelectorAll("div.KittyCard-details-item.KittyCard-details-item--highlight")
                let kittyIDs = []
                divs.forEach(d => kittyIDs.push(d.textContent))
                console.log(kittyIDs)
                xhr.open('GET', 'https://anachronauts.com/kitty?ids='+kittyIDs.join(), true);
                xhr.send(null);
            }
        }, 100)
}
check4Kitties()


xhr.onload = function (foo) {
    let result = xhr.responseText;
    let toggle = document.createElement('button')
    toggle.classList.add("toggleButton")
    toggle.innerText = "See the criminals"
    document.querySelector("body").appendChild(toggle)
    toggle.onclick = function onclick(event){
        drawStuff(result)

        let bars = document.querySelectorAll(".bars")
        bars.forEach(bar => {bar.classList.toggle("hide")})
    }
};

function drawStuff(result){
    console.log(result)
    let response = JSON.parse(result)
    let IDs = Object.keys(response)
    console.log(IDs)
    let divs = document.querySelectorAll("div.KittyCard-details-item.KittyCard-details-item--highlight")
    let criminals = []
    IDs.forEach(id => {
        console.log(id)
        if(parseInt(id) && response[id]["criminal"]){
            criminals.push(id)
        }
    })
    divs.forEach(div => {
        if(criminals.includes(div.textContent)){
            div.classList.add("criminal")
            div.textContent = "THIS KITTY IS CRIMINAL"
            let kittyItem = div.closest('.KittiesGrid-item')
            kittyItem.classList.add("criminal")
            let statusBubble = kittyItem.querySelector('.KittyCard-status')
            statusBubble.querySelector('.CardStatusBody-title').textContent = "DO NOT BUY"
            statusBubble.querySelector('.CardStatusBody-title').style.color = "red"
            kittyItem.appendChild(statusBubble)

            const createBars = document.createElement('img')
            createBars.src = "http://files.buoydontfloat.com/cell_new.png"
            createBars.classList.add("bars")
            createBars.classList.add("hide")
            div.closest('.KittiesGrid-item').appendChild(createBars)
        }
    })

}

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
        if(request.greeting == "updated"){
            setTimeout(check4Kitties,1000)
            sendResponse({farewell: "checked"})
        }
    }
)