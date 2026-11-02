# Base64 XML + GitHub Pages starter

এটি নিজের/অনুমোদিত ভিডিও ও XML configuration-এর জন্য starter kit; HelixMedia360-এর private backend/template clone নয়।

## GitHub Pages
1. https://github.com/new এ Public repository তৈরি করুন, যেমন `my-player-config`।
2. `config.xml` root-এ upload করে Commit করুন।
3. Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save।
4. XML URL: `https://YOUR-USERNAME.github.io/my-player-config/config.xml`

## Generator
`generator.html` browser-এ খুলুন। নিজের player page URL, Post ID এবং XML content দিন। Generate চাপলে Base64 ও URL পাবেন।

## গুরুত্বপূর্ণ
- XML-এর সঠিক MIME declaration সাধারণত `data:application/xml;base64,`। উদাহরণে `data:video/mp4;base64,` থাকলেও payload XML—এটি custom/non-standard হতে পারে।
- Base64 encryption নয়; যে কেউ decode করতে পারে।
- GitHub Pages static hosting; server-side code চালায় না।
- `player.html` একটি সাধারণ HTML5 MP4 demo, krpano viewer নয়। প্রকৃত krpano viewer-এর জন্য আপনার licensed krpano package ও official embed code লাগবে।
- শুধু নিজের বা ব্যবহারের অনুমতি থাকা ভিডিও/স্ট্রিম ব্যবহার করুন। গোপন token XML-এ রাখবেন না।
