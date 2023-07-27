import express from "express";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// GET route for /api/hello
app.get("/api/hello", (req, res)  => {
    res.json('Hello from Express');
});

// POST route for /api/world
app.post('/api/world', (req, res) => {
    const input = req.body.form;
    console.log('Received input:', input);
    res.json({ message: `I received your POST request. This is what you sent me: ${input}` });
  });
  
app.listen(3000, () => {
    console.log(`run on port 3000`);
});
