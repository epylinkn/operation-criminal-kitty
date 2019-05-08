// let divs = document.querySelectorAll("div.KittyCard-details-item.KittyCard-details-item--highlight")
// divs.forEach(d => console.log("hello from outside: " + d.textContent))

console.log("hello i am working")

// chrome.runtime.onMessage.addListener(
// 	function(message, callback) {
// 		if (message == "runContentScript"){
// 			chrome.tabs.executeScript({
// 				file: 'contentScript.js'
// 			});
// 		}
// 	}
// );

// chrome.tabs.executeScript(1, {code}, function(result){
// 	const { forkUrl, url, href } = result[0]
// 	console.log("hello")
// 	if(forkUrl){
// 		console.log(document.getElementById("div").innerText)
// 	}
// })

chrome.tabs.onUpdated.addListener(function(tabId, changInfo, tab){
	chrome.tabs.sendMessage(tabId, {greeting: "updated"}, function(response){
		console.log("content script responded")
	})
	// if(tab.url.includes("cryptokitties.co")){
	// 	chrome.tabs.executeScript({
	// 		file: 'contentScript.js'
	// 	});
	// }
})