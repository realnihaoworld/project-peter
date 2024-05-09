
chrome.tabs.query({ active: true, lastFocusedWindow: true }, async tabs => {
    // Gets the current tab
    var url = new URL(tabs[0].url)
    var domain = url.hostname
    document.getElementById("url").innerHTML=domain
    
    // Making post request to the local host
    const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST", 
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify({
        "url": domain,
        })
        });
    
    // Sends the post request and logs it
    const url_post = await response.json();
    console.log(url_post);
});