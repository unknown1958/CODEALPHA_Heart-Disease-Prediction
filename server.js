const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 5001;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files
app.use(express.static(path.join(__dirname, "public")));

// API route: handle form submission
app.post("/api/contact", (req, res) => {
  const { name, email, message } = req.body;

  // Simple validation
  if (!name || !email || !message) {
    return res.status(400).json({
      success: false,
      message: "All fields are required.",
    });
  }

  // No database: just log or later send email
  console.log("New contact submission:", { name, email, message });

  return res.status(200).json({
    success: true,
    message: "Form Submitted Successfully",
  });
});

// Fallback: serve index.html for any unknown route
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.listen(PORT, () => {
  console.log(`Server listening at http://localhost:${PORT}`);
});