/**
 * DUOLICIOUS BASICS UPDATER
 * (You can change a basic to "Unanswered" too.
 * INSTRUCTIONS TO GET YOUR TOKEN:
 * 1. Open https://web.duolicious.app/ and log in.
 * 2. Press F12 to open Developer Tools and select the "Network" tab.
 * 3. On the website, click your profile icon -> "Edit Profile" -> "Basics".
 * 4. CHANGE YOUR HEIGHT (move the slider or just click done you don't need to really change it).
 * 5. Click the "Done" button at the top right.
 * 6. In the Network tab, look for a request with a "PATCH" method.
 * 7. Click it, go to "Headers", and scroll down to "Request Headers".
 * 8. Copy the value next to "Authorization" (the long string starting with Bearer).
 * 9. Paste this code into the Console and run it:
 */

(async (t) => {
  const res = await fetch("https://api.duolicious.app/profile-info", {
    method: "PATCH",
    headers: {
      "Authorization": `Bearer ${t.replace(/Bearer |"/g, "")}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ bio: " ", tagline: " ", drugs: "No" })
  });
  console.log(res.ok ? "Success, PRESS F5." : "Error: " + res.status);
})("PASTE_TOKEN_HERE");
