const express = require("express");
const cors = require("cors");
const path = require("path");
const session = require("express-session");
const bodyparser = require("body-parser");

const app = express();
const PORT = process.env.PORT || 3000;

// middleware
app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({ extended: true }));

// using ejs
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views')); // Set views directory

const sess = {
  secret: 'Super secret secret',
  resave: true,
  saveUninitialized: true,
};

app.use(session(sess));

//routes
app.get("/", (req, res) => {
    res.render("index", { error : null });
});

app.use("/users", require("./routes/auth"));

app.listen(PORT, () => {
    console.log(`Connected to port ${PORT}`);
})
