/**
 * Duolicious Profile Collector & Visitor
 */
(function() {
    window.myProfileList = window.myProfileList || new Set();
    const uuidRegex = /[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/gi;

    const handleData = (text) => {
        // 1. Check for JSON usernames/handles
        try {
            const data = JSON.parse(text);
            const extractHandles = (obj) => {
                if (!obj || typeof obj !== 'object') return;
                if (obj.username) window.myProfileList.add(obj.username.toLowerCase());
                if (obj.handle) window.myProfileList.add(obj.handle.toLowerCase());
                for (let k in obj) extractHandles(obj[k]);
            };
            extractHandles(data);
        } catch (e) {
            // 2. Fallback: match raw UUIDs in text
            const matches = text.match(uuidRegex);
            if (matches) {
                matches.forEach(id => window.myProfileList.add(id.toLowerCase()));
            }
        }

        // 3. Collect visible username links from the DOM (e.g., href="/aaron164")
        document.querySelectorAll('a[href^="/"]').forEach(a => {
            const path = a.getAttribute('href').replace(/^\//, '').split(/[?#]/)[0];
            const ignored = ['search', 'inbox', 'profile', 'settings', 'login', 'explore'];
            if (path && !ignored.includes(path) && !path.includes('/')) {
                window.myProfileList.add(path.toLowerCase());
            }
        });

        console.log(`%c [Collector] Queue size: ${window.myProfileList.size}`, "color: #00ff00; font-weight: bold;");
    };

    const originalFetch = window.fetch;
    window.fetch = async (...args) => {
        const response = await originalFetch(...args);
        if (args[0] && typeof args[0] === 'string' && args[0].includes('/search')) {
            const clone = response.clone();
            const text = await clone.text();
            handleData(text);
        }
        return response;
    };

    const originalOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url) {
        this.addEventListener('load', function() {
            if (url && url.includes('/search')) handleData(this.responseText);
        });
        originalOpen.apply(this, arguments);
    };

    console.log("✅ Collector Active (Captures UUIDs & Usernames).");
})();

/**
 * @param {number} limit - Number of profiles to visit
 * @param {number} minDelay - Min delay (ms)
 * @param {number} maxDelay - Max delay (ms)
 * @param {string} token - Bearer Token
 * @param {Array} providedIds - (Optional) Array of UUIDs/Usernames
 */
async function startVisits(limit = 100, minDelay = 800, maxDelay = 800, token = "", providedIds = null) {
    if (!token) {
        console.error("❌ You must provide a Bearer Token!");
        return;
    }

    let currentMin = minDelay;
    let currentMax = maxDelay;
    let currentWait = 10000;

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
            const res = await fetch(`https://duolicious.app/${id}`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });

            if (res.status === 429) {
                currentMin += 105;
                currentMax += 105;
                console.warn(`⚠️ Rate Limited! Waiting ${currentWait / 1000}s... and increasing min and max by 105ms`);
                await new Promise(r => setTimeout(r, currentWait));
                i--; 
                continue;
            } else if (i % 10 === 0 || !res.ok) {
                console.log(`[${i + 1}/${toVisit.length}] (${id}) ${res.ok ? "✅" : "❌ " + res.status}`);
            }

        } catch (e) {
            console.error(`Connection error on ${id}`);
        }

        if (!providedIds) window.myProfileList.delete(id);

        const randomDelay = Math.floor(Math.random() * (currentMax - currentMin + 1)) + currentMin;
        await new Promise(r => setTimeout(r, randomDelay));
    }
    console.log("Batch Finished.");
}

/**
 * Opens a text area to paste usernames or UUIDs
 */
function startVisitsFromPrompt(limit = 100, min = 800, max = 800, token = "") {
    const overlay = document.createElement('div');
    overlay.style = "position:fixed;top:10%;left:25%;width:50%;height:50%;background:white;z-index:9999;border:5px solid #00ff00;padding:20px;display:flex;flex-direction:column;box-shadow:0 0 20px black;";
    overlay.innerHTML = `
        <h3 style="color:black;margin-top:0;">Paste UUID / Username List Below (One per line)</h3>
        <textarea id="idInput" style="flex:1;margin-bottom:10px;font-family:monospace;"></textarea>
        <button id="startBtn" style="padding:10px;background:#00ff00;font-weight:bold;cursor:pointer;">START VISITS</button>
    `;
    document.body.appendChild(overlay);

    document.getElementById('startBtn').onclick = () => {
        const text = document.getElementById('idInput').value;
        const idArray = text.trim().split(/\s+/).filter(id => id.length > 0);
        document.body.removeChild(overlay);

        if (idArray.length > 0) {
            console.log(`✅ Loaded ${idArray.length} IDs from prompt.`);
            startVisits(limit, min, max, token, idArray);
        } else {
            console.error("No IDs found in the text box.");
        }
    };
}

console.log(`USAGE COPY PASTE EXAMPLE: startVisitsFromPrompt(2889, 800, 800, "YOUR_TOKEN");`);
console.log(`USAGE SCROLL SEARCH EXAMPLE: startVisits(2889, 800, 800, "YOUR_TOKEN");`);
