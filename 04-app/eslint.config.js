// Configuración mínima de ESLint (flat config, ESLint 9+)
// Reglas básicas a propósito: el objetivo es que el taller vea un lint
// real corriendo en CI, no una configuración exhaustiva.

module.exports = [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "commonjs",
      globals: {
        require: "readonly",
        module: "readonly",
        process: "readonly",
        console: "readonly",
        __dirname: "readonly",
      },
    },
    rules: {
      "no-unused-vars": "error",
      "no-undef": "error",
      "no-var": "error",
      "prefer-const": "warn",
      eqeqeq: "warn",
    },
  },
  {
    ignores: ["node_modules/**"],
  },
];
