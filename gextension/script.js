
chrome.tabs.query({ active: true, lastFocusedWindow: true }, async tabs => {
    var url = new URL(tabs[0].url)
    var domain = url.hostname
    document.getElementById("url").innerHTML=domain
    
    // Post request
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
    
    const url_post = await response.json();
    console.log(url_post);
});