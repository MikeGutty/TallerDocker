const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok" });
});

app.get("/error", (req, res) => {
  res.status(500).json({ status: "error", message: "Error interno del servidor" });
})

app.get("/hello", (req, res) => {
  res.status(200).json({ message: "Hola, mundo!" });
});

app.get("/goodbye", (req, res) => {
  res.status(200).json({ message: "Adiós, mundo!" });
});

app.get("/", (req, res) => {
  res.status(200).send("Bienvenido al taller de CI/CD con GitHub Actions y Docker");
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
  });
}

module.exports = app;
