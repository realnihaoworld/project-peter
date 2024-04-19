

chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
    var url = new URL(tabs[0].url)
    var domain = url.hostname
    document.getElementById("url").innerHTML=domain
    document.getElementById("previous").innerHTML="please help me I'm an unpaid worker being contracted to do this job for them!"
});