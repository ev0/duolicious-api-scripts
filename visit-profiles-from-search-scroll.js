/**
 * Duolicious Profile Collector & Visitor
 * 
 * Instructions:
 * 1. Run the Collector in the console.
 * 2. Scroll the search page to find IDs.
 * 3. Run startVisits(limit, min, max, your_token)
 */

(function() {
    window.myProfileList = window.myProfileList || new Set();
    const uuidRegex = /[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/gi;

    const handleData = (text) => {
        const matches = text.match(uuidRegex);
        if (matches) {
            matches.forEach(id => {
                // Generic filter: ignore IDs that are likely not profiles
                // (Users should add their own ignore-list here)
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
    console.log("✅ Collector Active.");
})();

/**
 * @param {number} limit - Number of profiles to visit
 * @param {number} minDelay - Minimum randomized delay (ms)
 * @param {number} maxDelay - Maximum randomized delay (ms)
 * @param {string} token - Your Bearer Token
 */
async function startVisits(limit = 100, minDelay = 100, maxDelay = 300, token = "") {
    if (!token) {
        console.error("❌ You must provide a Bearer Token!");
        return;
    }

    let currentMin = minDelay;
    let currentMax = maxDelay;
    
    const allIds = Array.from(window.myProfileList);
    const toVisit = allIds.slice(0, limit);
    
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
                console.warn(`⚠️ Rate Limited! Waiting 6s...`);
                await new Promise(r => setTimeout(r, 6000));
                i--; continue; 
            } 
            else if (i % 10 === 0 || !res.ok) {
                console.log(`[${i + 1}/${toVisit.length}] ${res.ok ? "✅" : "❌ " + res.status}`);
            }

        } catch (e) {
            console.error("Connection error.");
        }

        window.myProfileList.delete(id);
        const randomDelay = Math.floor(Math.random() * (currentMax - currentMin + 1)) + currentMin;
        await new Promise(r => setTimeout(r, randomDelay));
    }
}
