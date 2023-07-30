const express = require("express"),
  path = require("path"),
  app = express();
app.use(
  "/assets",
  express.static(path.resolve(__dirname, "frontend", "assets"))
),
  app.get("/", (e, s) => {
    s.sendFile(path.resolve(__dirname, "frontend", "landing.html"));
  }),
  app.get("/*", (e, s) => {
    s.sendFile(path.resolve(__dirname, "frontend", "index.html"));
  });
const server = app.listen(process.env.PORT || 1337);
