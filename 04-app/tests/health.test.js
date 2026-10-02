const { test } = require("node:test");
const assert = require("node:assert");
const http = require("node:http");
const app = require("../src/index.js");

function getServer() {
  return app.listen(0);
}

test("GET /health responde 200 y status ok", async () => {
  const server = getServer();
  const { port } = server.address();

  const data = await new Promise((resolve, reject) => {
    http.get(`http://localhost:${port}/health`, (res) => {
      let body = "";
      res.on("data", (chunk) => (body += chunk));
      res.on("end", () => resolve({ status: res.statusCode, body: JSON.parse(body) }));
    }).on("error", reject);
  });

  assert.strictEqual(data.status, 200);
  assert.strictEqual(data.body.status, "ok");

  server.close();
});

test("GET / responde 200", async () => {
  const server = getServer();
  const { port } = server.address();

  const status = await new Promise((resolve, reject) => {
    http.get(`http://localhost:${port}/`, (res) => resolve(res.statusCode)).on("error", reject);
  });

  assert.strictEqual(status, 200);

  server.close();
});
