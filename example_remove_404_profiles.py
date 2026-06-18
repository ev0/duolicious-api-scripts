import re

log_text = """
VM115:39 [1/5232] ✅
VM115:39 [11/5232] ✅
VM115:39 [21/5232] ✅
VM115:39 [31/5232] ✅
VM115:39 [41/5232] ✅
VM115:39 [51/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/b7647462-a895-47d9-8826-ee03ea55ad40 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 10s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:26  GET https://api.duolicious.app/prospect-profile/b7647462-a895-47d9-8826-ee03ea55ad40 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 11s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:26  GET https://api.duolicious.app/prospect-profile/b7647462-a895-47d9-8826-ee03ea55ad40 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 12s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [61/5232] ✅
VM115:39 [71/5232] ✅
VM115:39 [81/5232] ✅
VM115:39 [91/5232] ✅
VM115:39 [101/5232] ✅
VM115:39 [111/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/b6790866-69f9-4173-9b25-2020602653b2 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 13s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:26  GET https://api.duolicious.app/prospect-profile/b6790866-69f9-4173-9b25-2020602653b2 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 14s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [121/5232] ✅
VM115:39 [131/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/293257a0-22b7-4701-8cda-51c4c3742f0f 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [139/5232] ❌ 404
VM115:39 [141/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [151/5232] ✅
VM115:39 [161/5232] ✅
VM115:39 [171/5232] ✅
VM115:39 [181/5232] ✅
VM115:39 [191/5232] ✅
VM115:39 [201/5232] ✅
VM115:39 [211/5232] ✅
VM115:39 [221/5232] ✅
VM115:39 [231/5232] ✅
VM115:39 [241/5232] ✅
VM115:39 [251/5232] ✅
VM115:39 [261/5232] ✅
VM115:39 [271/5232] ✅
VM115:39 [281/5232] ✅
VM115:39 [291/5232] ✅
VM115:39 [301/5232] ✅
VM115:39 [311/5232] ✅
VM115:39 [321/5232] ✅
VM115:39 [331/5232] ✅
VM115:39 [341/5232] ✅
VM115:39 [351/5232] ✅
VM115:39 [361/5232] ✅
VM115:39 [371/5232] ✅
VM115:39 [381/5232] ✅
VM115:39 [391/5232] ✅
VM115:39 [401/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [411/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/4b1b9ded-bb8e-4da8-97c6-8ce7346384ed 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 15s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [421/5232] ✅
VM115:39 [431/5232] ✅
VM115:39 [441/5232] ✅
VM115:39 [451/5232] ✅
VM115:39 [461/5232] ✅
VM115:39 [471/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/cb1c8228-b482-4944-a2a8-a424eda8d2ef 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 16s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [481/5232] ✅
VM115:39 [491/5232] ✅
VM115:39 [501/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/e119e0b2-36b4-4434-987a-6b5355fc55d2 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [504/5232] ❌ 404
VM115:39 [511/5232] ✅
VM115:39 [521/5232] ✅
VM115:39 [531/5232] ✅
VM115:39 [541/5232] ✅
VM115:39 [551/5232] ✅
VM115:39 [561/5232] ✅
VM115:39 [571/5232] ✅
VM115:39 [581/5232] ✅
VM115:39 [591/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/fe404e86-cbcd-4a68-bf8e-3b403a76c7c1 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 17s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [601/5232] ✅
VM115:39 [611/5232] ✅
VM115:39 [621/5232] ✅
VM115:39 [631/5232] ✅
VM115:39 [641/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [651/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/3e030890-e90a-4d93-88cc-0d8bc6d03923 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 18s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [661/5232] ✅
VM115:39 [671/5232] ✅
VM115:39 [681/5232] ✅
VM115:39 [691/5232] ✅
VM115:39 [701/5232] ✅
VM115:39 [711/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/bf035051-7127-49a2-b414-01fb94106d41 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [712/5232] ❌ 404
VM115:39 [721/5232] ✅
VM115:39 [731/5232] ✅
VM115:39 [741/5232] ✅
VM115:39 [751/5232] ✅
VM115:39 [761/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [771/5232] ✅
VM115:39 [781/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [791/5232] ✅
VM115:39 [801/5232] ✅
VM115:39 [811/5232] ✅
VM115:39 [821/5232] ✅
VM115:39 [831/5232] ✅
VM115:39 [841/5232] ✅
VM115:39 [851/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [861/5232] ✅
profile:1 Notifications permission has been blocked as the user has ignored the permission prompt several times. This can be reset in Page Info which can be accessed by clicking the tune icon next to the URL. See https://www.ch40mestatus.qjz9zk/feature/6443143280984064 for more information.
AppEntry-9dd94924f810ccac04b0978311aef409.js:1725 Permissions not granted
s @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1725
await in s
u @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1725
q @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in q
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [871/5232] ✅
profile:1 Notifications permission has been blocked as the user has ignored the permission prompt several times. This can be reset in Page Info which can be accessed by clicking the tune icon next to the URL. See https://www.ch40mestatus.qjz9zk/feature/6443143280984064 for more information.
AppEntry-9dd94924f810ccac04b0978311aef409.js:1725 Permissions not granted
s @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1725
await in s
u @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1725
q @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in q
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [881/5232] ✅
VM115:39 [891/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/5faaaf4f-fac9-4fac-992e-c0f89cddc6cf 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 19s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [901/5232] ✅
VM115:39 [911/5232] ✅
VM115:39 [921/5232] ✅
VM115:39 [931/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/7fb8712e-fb62-4246-b5fe-3f2e9567083f 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [941/5232] ❌ 404
VM115:39 [951/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/4e0ba53c-aa1f-4f2e-8356-f199539767e3 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 20s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [961/5232] ✅
VM115:39 [971/5232] ✅
VM115:39 [981/5232] ✅
VM115:39 [991/5232] ✅
VM115:39 [1001/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/96a6cc88-fe8f-42d9-af63-d5ffc3f4173c 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1009/5232] ❌ 404
VM115:39 [1011/5232] ✅
VM115:39 [1021/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1031/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/cd887791-451f-4818-8fe1-8d72529b98bd 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1035/5232] ❌ 404
VM115:26  GET https://api.duolicious.app/prospect-profile/62b27ec9-d152-4704-9855-7eccab289943 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1038/5232] ❌ 404
VM115:39 [1041/5232] ✅
VM115:39 [1051/5232] ✅
VM115:39 [1061/5232] ✅
VM115:39 [1071/5232] ✅
VM115:39 [1081/5232] ✅
VM115:39 [1091/5232] ✅
VM115:39 [1101/5232] ✅
VM115:39 [1111/5232] ✅
VM115:39 [1121/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/eecb4f68-0109-455d-97fd-976f284725b2 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1126/5232] ❌ 404
VM115:39 [1131/5232] ✅
VM115:39 [1141/5232] ✅
VM115:39 [1151/5232] ✅
VM115:39 [1161/5232] ✅
VM115:39 [1171/5232] ✅
VM115:39 [1181/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/edcb9ebc-fea7-464e-9c04-983a393ca2a9 net::ERR_ABORTED 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1182/5232] ❌ 404
VM115:39 [1191/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/5552cdf5-c360-4321-aadf-2a9d9a60f793 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 21s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1201/5232] ✅
VM115:39 [1211/5232] ✅
VM115:39 [1221/5232] ✅
VM115:39 [1231/5232] ✅
VM115:39 [1241/5232] ✅
VM115:39 [1251/5232] ✅
VM115:39 [1261/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1271/5232] ✅
VM115:39 [1281/5232] ✅
VM115:39 [1291/5232] ✅
VM115:39 [1301/5232] ✅
VM115:39 [1311/5232] ✅
VM115:39 [1321/5232] ✅
VM115:39 [1331/5232] ✅
VM115:39 [1341/5232] ✅
VM115:39 [1351/5232] ✅
VM115:39 [1361/5232] ✅
VM115:39 [1371/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/5b213ed0-8f2b-47de-ad3b-cfafdb804949 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 22s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1381/5232] ✅
VM115:39 [1391/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/511a2d2f-9c58-4457-9f49-845ebb8b4073 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1400/5232] ❌ 404
VM115:39 [1401/5232] ✅
VM115:39 [1411/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1421/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1431/5232] ✅
VM115:39 [1441/5232] ✅
VM115:39 [1451/5232] ✅
VM115:39 [1461/5232] ✅
VM115:39 [1471/5232] ✅
VM115:39 [1481/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/3a5b2762-94ac-471d-900c-e47ba54d2792 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1486/5232] ❌ 404
VM115:39 [1491/5232] ✅
VM115:39 [1501/5232] ✅
VM115:39 [1511/5232] ✅
VM115:39 [1521/5232] ✅
VM115:39 [1531/5232] ✅
VM115:39 [1541/5232] ✅
VM115:39 [1551/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/0532c19b-9c85-4061-acb5-d94f8ce3dccc 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 23s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1561/5232] ✅
VM115:39 [1571/5232] ✅
VM115:39 [1581/5232] ✅
VM115:39 [1591/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1601/5232] ✅
VM115:39 [1611/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/f19e1071-efb0-4b7c-b35a-8060a516f3f8 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 24s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1621/5232] ✅
VM115:39 [1631/5232] ✅
VM115:39 [1641/5232] ✅
VM115:39 [1651/5232] ✅
VM115:39 [1661/5232] ✅
VM115:39 [1671/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1681/5232] ✅
VM115:39 [1691/5232] ✅
VM115:39 [1701/5232] ✅
VM115:39 [1711/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/c5c486b6-6ccb-4d22-8686-d37fc3dff743 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1715/5232] ❌ 404
VM115:39 [1721/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/ff38a68c-bf4c-4fef-8c91-06c7cf10c7bb 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1724/5232] ❌ 404
VM115:39 [1731/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/b2a4cfc1-ae8b-42ad-9608-24a77f6715a7 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 25s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1741/5232] ✅
VM115:39 [1751/5232] ✅
VM115:39 [1761/5232] ✅
VM115:39 [1771/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1781/5232] ✅
VM115:39 [1791/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1801/5232] ✅
VM115:39 [1811/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1821/5232] ✅
VM115:39 [1831/5232] ✅
VM115:39 [1841/5232] ✅
VM115:39 [1851/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/88610aaf-7c5c-45a4-b8ed-9cc75c06c9de 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 26s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1861/5232] ✅
VM115:39 [1871/5232] ✅
VM115:39 [1881/5232] ✅
VM115:39 [1891/5232] ✅
VM115:39 [1901/5232] ✅
VM115:39 [1911/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/2560d5cf-a76f-4dd9-af25-476dc2977159 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 27s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1921/5232] ✅
VM115:39 [1931/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/41c73f2c-4c15-4526-ac32-4e0961233d8b 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [1932/5232] ❌ 404
VM115:39 [1941/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1951/5232] ✅
VM115:39 [1961/5232] ✅
VM115:39 [1971/5232] ✅
VM115:39 [1981/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [1991/5232] ✅
VM115:39 [2001/5232] ✅
VM115:39 [2011/5232] ✅
VM115:39 [2021/5232] ✅
VM115:39 [2031/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/82f6688b-8a52-45ea-b7f0-7bdd852e82dc 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 28s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2041/5232] ✅
VM115:39 [2051/5232] ✅
VM115:39 [2061/5232] ✅
VM115:39 [2071/5232] ✅
VM115:39 [2081/5232] ✅
VM115:39 [2091/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/6974701d-954e-48cf-a570-4d01cd1cd878 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 29s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2101/5232] ✅
VM115:39 [2111/5232] ✅
VM115:39 [2121/5232] ✅
VM115:39 [2131/5232] ✅
VM115:39 [2141/5232] ✅
VM115:39 [2151/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/c740aa78-1b3c-4d91-8541-0b5cf73a4712 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 30s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2161/5232] ✅
VM115:39 [2171/5232] ✅
VM115:39 [2181/5232] ✅
VM115:39 [2191/5232] ✅
VM115:39 [2201/5232] ✅
VM115:39 [2211/5232] ✅
VM115:39 [2221/5232] ✅
VM115:39 [2231/5232] ✅
VM115:39 [2241/5232] ✅
VM115:39 [2251/5232] ✅
VM115:39 [2261/5232] ✅
VM115:39 [2271/5232] ✅
VM115:39 [2281/5232] ✅
VM115:39 [2291/5232] ✅
VM115:39 [2301/5232] ✅
VM115:39 [2311/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/38347b5d-6dbe-40d1-820f-36c24e3ec0c1 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2320/5232] ❌ 404
VM115:39 [2321/5232] ✅
VM115:39 [2331/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/efd83f43-a90c-4712-a9ce-4a2df7261662 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 31s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2341/5232] ✅
VM115:39 [2351/5232] ✅
VM115:39 [2361/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2371/5232] ✅
VM115:39 [2381/5232] ✅
VM115:39 [2391/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/cdaf06e3-97f4-49d5-add0-d47d92533841 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 32s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2401/5232] ✅
VM115:39 [2411/5232] ✅
VM115:39 [2421/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2431/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2441/5232] ✅
VM115:39 [2451/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2461/5232] ✅
VM115:39 [2471/5232] ✅
VM115:39 [2481/5232] ✅
VM115:39 [2491/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2501/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2511/5232] ✅
VM115:39 [2521/5232] ✅
VM115:39 [2531/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2541/5232] ✅
VM115:39 [2551/5232] ✅
VM115:39 [2561/5232] ✅
VM115:39 [2571/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:26  GET https://api.duolicious.app/prospect-profile/8635fb3d-508e-46a1-8c27-b78096130fcf 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 33s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2581/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2591/5232] ✅
VM115:39 [2601/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2611/5232] ✅
VM115:39 [2621/5232] ✅
VM115:39 [2631/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/bfaeae52-f813-47de-a3af-2291b6164269 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2636/5232] ❌ 404
VM115:26  GET https://api.duolicious.app/prospect-profile/6b1cf9d9-6e75-4653-9805-e93401f56032 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 34s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2641/5232] ✅
VM115:39 [2651/5232] ✅
VM115:39 [2661/5232] ✅
VM115:39 [2671/5232] ✅
VM115:39 [2681/5232] ✅
VM115:39 [2691/5232] ✅
VM115:39 [2701/5232] ✅
VM115:39 [2711/5232] ✅
VM115:39 [2721/5232] ✅
VM115:39 [2731/5232] ✅
VM115:39 [2741/5232] ✅
VM115:39 [2751/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/27263f2d-8cb0-444c-a4dd-c7b7b4bb6f23 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 35s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2761/5232] ✅
VM115:39 [2771/5232] ✅
VM115:39 [2781/5232] ✅
VM115:39 [2791/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2801/5232] ✅
VM115:39 [2811/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/ca3cf8f9-1878-4971-acca-8590c52f70df 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 36s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [2821/5232] ✅
VM115:39 [2831/5232] ✅
VM115:39 [2841/5232] ✅
VM115:39 [2851/5232] ✅
VM115:39 [2861/5232] ✅
VM115:39 [2871/5232] ✅
VM115:39 [2881/5232] ✅
VM115:39 [2891/5232] ✅
VM115:39 [2901/5232] ✅
VM115:39 [2911/5232] ✅
VM115:39 [2921/5232] ✅
VM115:39 [2931/5232] ✅
VM115:39 [2941/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [2951/5232] ✅
VM115:39 [2961/5232] ✅
VM115:39 [2971/5232] ✅
VM115:39 [2981/5232] ✅
VM115:39 [2991/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/29ab7e67-64fa-4171-93d6-f12255219554 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 37s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3001/5232] ✅
VM115:39 [3011/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3021/5232] ✅
VM115:39 [3031/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3041/5232] ✅
VM115:39 [3051/5232] ✅
VM115:39 [3061/5232] ✅
VM115:39 [3071/5232] ✅
VM115:39 [3081/5232] ✅
VM115:39 [3091/5232] ✅
VM115:39 [3101/5232] ✅
VM115:39 [3111/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/b491434c-79bb-4801-8a4e-7033a23023c1 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 38s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:26  GET https://api.duolicious.app/prospect-profile/7a8e19ff-c01a-42e7-baec-e797bf228cc3 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3120/5232] ❌ 404
VM115:39 [3121/5232] ✅
VM115:39 [3131/5232] ✅
VM115:39 [3141/5232] ✅
VM115:39 [3151/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3161/5232] ✅
VM115:39 [3171/5232] ✅
VM115:39 [3181/5232] ✅
VM115:39 [3191/5232] ✅
VM115:39 [3201/5232] ✅
VM115:39 [3211/5232] ✅
VM115:39 [3221/5232] ✅
VM115:39 [3231/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/8a2efd85-91e7-43a3-a9d1-51ca6fc71aea 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 39s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3241/5232] ✅
VM115:39 [3251/5232] ✅
VM115:39 [3261/5232] ✅
VM115:39 [3271/5232] ✅
VM115:39 [3281/5232] ✅
VM115:39 [3291/5232] ✅
VM115:39 [3301/5232] ✅
VM115:39 [3311/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/16529665-56ad-4c9f-b97c-739542c50901 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3315/5232] ❌ 404
VM115:39 [3321/5232] ✅
VM115:39 [3331/5232] ✅
VM115:39 [3341/5232] ✅
VM115:39 [3351/5232] ✅
VM115:39 [3361/5232] ✅
VM115:39 [3371/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3381/5232] ✅
VM115:39 [3391/5232] ✅
VM115:39 [3401/5232] ✅
VM115:39 [3411/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/710c6d55-58e8-4697-80d4-5930c4cceb62 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 40s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3421/5232] ✅
VM115:39 [3431/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3441/5232] ✅
VM115:39 [3451/5232] ✅
VM115:39 [3461/5232] ✅
VM115:39 [3471/5232] ✅
VM115:39 [3481/5232] ✅
VM115:39 [3491/5232] ✅
VM115:39 [3501/5232] ✅
VM115:39 [3511/5232] ✅
VM115:39 [3521/5232] ✅
VM115:39 [3531/5232] ✅
VM115:39 [3541/5232] ✅
VM115:39 [3551/5232] ✅
VM115:39 [3561/5232] ✅
VM115:39 [3571/5232] ✅
VM115:39 [3581/5232] ✅
VM115:39 [3591/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/835ece1e-9fbd-46ad-851a-f05d2dba6c83 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 41s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3601/5232] ✅
VM115:39 [3611/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3621/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3631/5232] ✅
VM115:39 [3641/5232] ✅
VM115:39 [3651/5232] ✅
VM115:39 [3661/5232] ✅
VM115:39 [3671/5232] ✅
VM115:39 [3681/5232] ✅
VM115:39 [3691/5232] ✅
VM115:39 [3701/5232] ✅
VM115:39 [3711/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/c36b53fc-75b5-4366-be75-60810369d08f 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 42s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3721/5232] ✅
VM115:39 [3731/5232] ✅
VM115:39 [3741/5232] ✅
VM115:39 [3751/5232] ✅
VM115:39 [3761/5232] ✅
VM115:39 [3771/5232] ✅
VM115:39 [3781/5232] ✅
VM115:39 [3791/5232] ✅
VM115:39 [3801/5232] ✅
VM115:39 [3811/5232] ✅
VM115:39 [3821/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/8bdfb191-f714-4c0a-98b3-f79bfe07ddd3 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3831/5232] ❌ 404
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:26  GET https://api.duolicious.app/prospect-profile/93fc6f0d-ffbb-4ff3-b8c7-5f59a743eeb9 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 43s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3841/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/6808c260-76d0-427b-94e3-b1af72639f9f 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3849/5232] ❌ 404
VM115:39 [3851/5232] ✅
VM115:39 [3861/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [3871/5232] ✅
VM115:39 [3881/5232] ✅
VM115:39 [3891/5232] ✅
VM115:39 [3901/5232] ✅
VM115:39 [3911/5232] ✅
VM115:39 [3921/5232] ✅
VM115:39 [3931/5232] ✅
VM115:39 [3941/5232] ✅
VM115:39 [3951/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/9db50f29-00d8-4cca-940b-7b343071df22 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 44s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [3961/5232] ✅
VM115:39 [3971/5232] ✅
VM115:39 [3981/5232] ✅
VM115:39 [3991/5232] ✅
VM115:39 [4001/5232] ✅
VM115:39 [4011/5232] ✅
VM115:39 [4021/5232] ✅
VM115:39 [4031/5232] ✅
VM115:39 [4041/5232] ✅
VM115:39 [4051/5232] ✅
VM115:39 [4061/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4071/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/a2817672-97e6-42c4-973e-29b6860c92e6 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 45s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4081/5232] ✅
VM115:39 [4091/5232] ✅
VM115:39 [4101/5232] ✅
VM115:39 [4111/5232] ✅
VM115:39 [4121/5232] ✅
VM115:39 [4131/5232] ✅
VM115:39 [4141/5232] ✅
VM115:39 [4151/5232] ✅
VM115:39 [4161/5232] ✅
VM115:39 [4171/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4181/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4191/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/e8e697c5-6b99-41cf-9c28-b4ddc1c20e0b 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 46s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4201/5232] ✅
VM115:39 [4211/5232] ✅
VM115:39 [4221/5232] ✅
VM115:39 [4231/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4241/5232] ✅
VM115:39 [4251/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4261/5232] ✅
VM115:39 [4271/5232] ✅
VM115:39 [4281/5232] ✅
VM115:39 [4291/5232] ✅
VM115:39 [4301/5232] ✅
VM115:39 [4311/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/0ea4b967-abae-45b6-abb6-d43d8348865c 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 47s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4321/5232] ✅
VM115:39 [4331/5232] ✅
VM115:39 [4341/5232] ✅
VM115:39 [4351/5232] ✅
VM115:39 [4361/5232] ✅
VM115:39 [4371/5232] ✅
VM115:39 [4381/5232] ✅
VM115:39 [4391/5232] ✅
VM115:39 [4401/5232] ✅
VM115:39 [4411/5232] ✅
VM115:39 [4421/5232] ✅
VM115:39 [4431/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4441/5232] ✅
VM115:39 [4451/5232] ✅
VM115:39 [4461/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4471/5232] ✅
VM115:39 [4481/5232] ✅
VM115:39 [4491/5232] ✅
VM115:39 [4501/5232] ✅
VM115:39 [4511/5232] ✅
VM115:39 [4521/5232] ✅
VM115:39 [4531/5232] ✅
VM115:39 [4541/5232] ✅
VM115:39 [4551/5232] ✅
VM115:39 [4561/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/df0e154d-3f3f-48c6-98fb-880e3b71ed83 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [4568/5232] ❌ 404
VM115:39 [4571/5232] ✅
VM115:39 [4581/5232] ✅
VM115:39 [4591/5232] ✅
VM115:39 [4601/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4611/5232] ✅
VM115:39 [4621/5232] ✅
VM115:39 [4631/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4641/5232] ✅
VM115:39 [4651/5232] ✅
VM115:39 [4661/5232] ✅
VM115:39 [4671/5232] ✅
VM115:39 [4681/5232] ✅
VM115:39 [4691/5232] ✅
VM115:39 [4701/5232] ✅
VM115:39 [4711/5232] ✅
VM115:39 [4721/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4731/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/e1746746-2aed-49d1-a924-1390abd8c524 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [4733/5232] ❌ 404
VM115:39 [4741/5232] ✅
VM115:39 [4751/5232] ✅
VM115:39 [4761/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4771/5232] ✅
VM115:39 [4781/5232] ✅
VM115:39 [4791/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/4630d2a9-6dff-4bc1-9569-9183a4299b4a 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 48s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [4801/5232] ✅
VM115:39 [4811/5232] ✅
VM115:39 [4821/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/0c12e501-feae-4139-bbf1-c90045055a3d 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [4828/5232] ❌ 404
VM115:39 [4831/5232] ✅
VM115:39 [4841/5232] ✅
VM115:39 [4851/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/bff70b27-c173-4b34-a30f-703b913c5518 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 49s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [4861/5232] ✅
VM115:39 [4871/5232] ✅
VM115:39 [4881/5232] ✅
VM115:39 [4891/5232] ✅
VM115:39 [4901/5232] ✅
VM115:39 [4911/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/3b1bf630-2614-427b-b85b-a22353eeff35 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 50s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [4921/5232] ✅
VM115:39 [4931/5232] ✅
VM115:39 [4941/5232] ✅
VM115:39 [4951/5232] ✅
VM115:39 [4961/5232] ✅
VM115:39 [4971/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/27da2685-6031-4460-8cae-55d0f5553f02 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 51s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [4981/5232] ✅
VM115:39 [4991/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/d3c39017-048d-4e24-be76-8392e044dffb 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [4998/5232] ❌ 404
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [5001/5232] ✅
VM115:39 [5011/5232] ✅
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [5021/5232] ✅
VM115:39 [5031/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/ad2d20c3-5694-4bff-a678-2362fce271b5 429 (Too Many Requests)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:33 ⚠️ Rate Limited! Waiting 52s...
startVisits @ VM115:33
await in startVisits
document.getElementById.onclick @ VM103:18
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
await in C
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
AppEntry-9dd94924f810ccac04b0978311aef409.js:1794 Notification permission denied
c @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1794
C @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1723
(anonymous) @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
o @ AppEntry-9dd94924f810ccac04b0978311aef409.js:939
E.onmessage @ AppEntry-9dd94924f810ccac04b0978311aef409.js:1709
VM115:39 [5041/5232] ✅
VM115:39 [5051/5232] ✅
VM115:26  GET https://api.duolicious.app/prospect-profile/05eb65cd-d575-49fe-9bd2-125f2245f779 net::ERR_ABORTED 404 (Not Found)
startVisits @ VM115:26
await in startVisits
document.getElementById.onclick @ VM103:18
VM115:39 [5052/5232] ❌ 404
VM115:39 [5061/5232] ✅
VM115:39 [5071/5232] ✅
VM115:39 [5081/5232] ✅
VM115:39 [5091/5232] ✅
VM115:39 [5101/5232] ✅
VM115:39 [5111/5232] ✅
VM115:39 [5121/5232] ✅
VM115:39 [5131/5232] ✅
VM115:39 [5141/5232] ✅
VM115:39 [5151/5232] ✅
VM115:39 [5161/5232] ✅
VM115:39 [5171/5232] ✅
VM115:39 [5181/5232] ✅
VM115:39 [5191/5232] ✅
VM115:39 [5201/5232] ✅
VM115:39 [5211/5232] ✅
VM115:39 [5221/5232] ✅
"""

def fix_uuid_list(text):

    uuid_pattern = re.compile(r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}', re.IGNORECASE)

    all_uuids = uuid_pattern.findall(text)
    if not all_uuids:
        print("❌ No UUIDs found in the text.")
        return []

    processed_pattern = re.compile(r'prospect-profile/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})',
                                   re.IGNORECASE)
    processed_uuids = set(processed_pattern.findall(text))


    master_seen = set()
    remaining_list = []

    for uid in all_uuids:
        uid_lower = uid.lower()
        if uid_lower not in processed_uuids and uid_lower not in master_seen:
            remaining_list.append(uid_lower)
            master_seen.add(uid_lower)

    return remaining_list


remaining = fix_uuid_list(log_text)

if remaining:
    print(f"✅ Success!")
    print(f"Total Unique UUIDs found: {len(set(re.findall(r'[a-f0-9]{8}-', log_text, re.I)))}")
    print(f"Processed (Visited): {len(set(re.findall(r'prospect-profile/[a-f0-9]{8}-', log_text, re.I)))}")
    print(f"Remaining: {len(remaining)}")
    print("\n--- START OF CLEANED LIST ---\n")
    print("\n".join(remaining))
