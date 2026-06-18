(function() {
    // will stop after the first 50, just remove the first 50 if you want the 51-100.
    const top100Clubs = [
        "anime", "discord", "unrestricted internet access as a kid", "gamer", "manga",
        "autism", "minecraft", "music", "gaming", "video games",
        "chronically online", "6 hour video essays are fun", "loser", "pervert", "nerd",
        "roblox", "freaky", "art", "freak", "horror",
        "retarded", "perverts dm me", "pokemon", "degenerate", "pc gaming",
        "dark souls", "metal", "nsfw", "evangelion", "cats",
        "adhd", "kinky", "weeb", "virgin", "autistic",
        "silly", "overwatch", "pervs dm me", "vocaloid", "kinky asf",
        "cosplay", "mentally ill", "elden ring", "neet", "bdsm",
        "plap plap plap", "persona", "history", "goonin", "brainrot",
"meow meow meow meow meow", "seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeex", "berserk", "dm me", "anti-ai",
        "cat", "femboy", "clingy", "0 social skills", '"jorking it"',
        "philosophy", "femcel", "jjba", "depressed", "movies",
        "videogames", "silent hill", "breakcore", "goth", "dnd",
        "pc", "emo", "lonely", "cat lover", "cooking",
        "switch", "fallout", "obsessive", "undertale", "yuri",
        "uma musume", "i love losers", "/v/", "schizo", "/a/",
        "shy", "chud", "ask me anything", "gym", "touhou",
        "marvel rivals", "terraria", "radiohead", "jojo", "books",
        "fortnite", "sleepy", "retard", "guns", "artist"
    ];

    /**
     * @param {string} token - Your Bearer token
     */
    window.joinTopClubs = async function(token) {
        if (!token || token === "YOUR_BEARER_TOKEN_HERE") {
            console.error("❌ Error: You must provide a valid Bearer token!");
            return;
        }

        const cleanToken = token.replace(/Authorization|Bearer|[:\s"']+/g, "");

        const API_URL = "https://api.duolicious.app/join-club";

        console.log(`Starting process to join ${top50Clubs.length} clubs...`);

        for (let i = 0; i < top50Clubs.length; i++) {
            const clubName = top50Clubs[i];
            console.log(`[${i + 1}/50] Sending join request for: '${clubName}'`);

            try {
                await new Promise(r => setTimeout(r, 1500));

                const response = await fetch(API_URL, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${cleanToken}`,
                        "Accept": "application/json"
                    },
                    body: JSON.stringify({ name: clubName })
                });

                if (response.ok) {
                    console.log(`%c ✅ Successfully joined: '${clubName}'`, "color: #00ff00; font-weight: bold;");
                } else if (response.status === 429) {
                    console.warn(`⚠️ Rate limited (HTTP 429). Pausing execution for 60 seconds...`);
                    await new Promise(r => setTimeout(r, 60000));
                    i--;
                } else {
                    const errorText = await response.text();
                    console.error(`❌ Failed to join '${clubName}'. Status: ${response.status}, Response: ${errorText}`);
                }
            } catch (e) {
                console.error(`❌ Connection error while trying to join '${clubName}':`, e);
                await new Promise(r => setTimeout(r, 5000));
            }
        }

        console.log("Process complete! Attempted to join all 50 clubs.");
    };

    console.log("✅ Script loaded. Run joinTopClubs('YOUR_BEARER_TOKEN_HERE') to start.");
})();
