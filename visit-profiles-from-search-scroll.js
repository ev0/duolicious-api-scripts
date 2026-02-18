/**
 * Duolicious Profile Collector & Visitor
 ----------------------------------------------------------------------------------
 
 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
 USAGE EXAMPLE: startVisitsFromPrompt(5663, 100, 300, "ca984af67ddaa50c21feda19bbd5d8e292e8cea04d45adb585a3df94a06d6f418ebc4dbbca9c455d81a2f7de3e16c028fae32d11eda074a218a7ff3246007913");
 
 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
 ----------------------------------------------------------------------------------
 */

(function() {
    window.myProfileList = window.myProfileList || new Set();
    const uuidRegex = /[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/gi;

    const handleData = (text) => {
        const matches = text.match(uuidRegex);
        if (matches) {
            matches.forEach(id => {
                window.myProfileList.add(id.toLowerCase());
            });
            console.log(`%c [Collector] Queue size: ${window.myProfileList.size}`, "color: #00ff00; font-weight: bold;");
        }
    };

    const originalFetch = window.fetch;
    window.fetch = async (...args) => {
        const response = await originalFetch(...args);
        if (args[0].includes('/search')) {
            const clone = response.clone();
            const text = await clone.text();
            handleData(text);
        }
        return response;
    };

    const originalOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url) {
        this.addEventListener('load', function() {
            if (url.includes('/search')) handleData(this.responseText);
        });
        originalOpen.apply(this, arguments);
    };
    console.log("✅ Collector & Prompt Helper Active.");
})();

/**
 * @param {number} limit - Number of profiles to visit
 * @param {number} minDelay - Min delay (ms)
 * @param {number} maxDelay - Max delay (ms)
 * @param {string} token - Bearer Token
 * @param {Array} providedIds - (Optional) Array of UUIDs to use instead of the collected list
 */
async function startVisits(limit = 100, minDelay = 100, maxDelay = 300, token = "", providedIds = null) {
    if (!token) {
        console.error("❌ You must provide a Bearer Token!");
        return;
    }

    let currentMin = minDelay;
    let currentMax = maxDelay;
    let currentWait = 10000; // Start at 10s standard
    
    // Use providedIds if they exist, otherwise use the collected list
    let sourceList = providedIds ? providedIds : Array.from(window.myProfileList);
    const toVisit = sourceList.slice(0, limit);
    
    if (toVisit.length === 0) {
        console.error("Queue is empty!");
        return;
    }

    console.log(`Starting batch: ${toVisit.length} profiles.`);

    for (let i = 0; i < toVisit.length; i++) {
        const id = toVisit[i];
        
        try {
            const res = await fetch(`https://api.duolicious.app/prospect-profile/${id}`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });

            if (res.status === 429) {
                currentMin += 5;
                currentMax += 5;
                console.warn(`⚠️ Rate Limited! Waiting ${currentWait / 1000}s...`);
                await new Promise(r => setTimeout(r, currentWait));
                currentWait += 1000; 
                i--; continue; 
            } 
            else if (i % 10 === 0 || !res.ok) {
                console.log(`[${i + 1}/${toVisit.length}] ${res.ok ? "✅" : "❌ " + res.status}`);
            }

        } catch (e) {
            console.error("Connection error.");
        }

        // Only delete from global list if we aren't using a custom provided list
        if (!providedIds) window.myProfileList.delete(id);

        const randomDelay = Math.floor(Math.random() * (currentMax - currentMin + 1)) + currentMin;
        await new Promise(r => setTimeout(r, randomDelay));
    }
    console.log("Batch Finished.");
}

/**
 * Opens a text area for you to paste IDs, then starts the visit process.
 */
function startVisitsFromPrompt(limit = 100, min = 100, max = 300, token = "") {
    const overlay = document.createElement('div');
    overlay.style = "position:fixed;top:10%;left:25%;width:50%;height:50%;background:white;z-index:9999;border:5px solid #00ff00;padding:20px;display:flex;flex-direction:column;box-shadow:0 0 20px black;";
    overlay.innerHTML = `
        <h3 style="color:black;margin-top:0;">Paste UUID List Below (One per line)</h3>
        <textarea id="idInput" style="flex:1;margin-bottom:10px;font-family:monospace;"></textarea>
        <button id="startBtn" style="padding:10px;background:#00ff00;font-weight:bold;cursor:pointer;">START VISITS</button>
    `;
    document.body.appendChild(overlay);

    document.getElementById('startBtn').onclick = () => {
        const text = document.getElementById('idInput').value;
        const idArray = text.trim().split(/\s+/).filter(id => id.length > 5);
        document.body.removeChild(overlay);
        
        if (idArray.length > 0) {
            console.log(`✅ Loaded ${idArray.length} IDs from prompt.`);
            startVisits(limit, min, max, token, idArray);
        } else {
            console.error("No IDs found in the text box.");
        }
    };
}


console.log(`USAGE COPY PASTE PROFILE UIDS EXAMPLE: startVisitsFromPrompt(5663, 100, 300, "YOUR_TOKEN");`);
console.log(`USAGE SCROLL SEARCH PROFILES EXAMPLE: startVisits(5663, 100, 300, "YOUR_TOKEN");`);
