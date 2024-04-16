const router = require("express").Router();
const pool = require("../db");

// login

router.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        const users = await pool.query(`SELECT * FROM users WHERE user_name = '${username}' AND user_password = '${password}'`);
        if (users.rows.length === 0) {
            return res.render("index", { error : "Invalid Credentials" });
        }

        req.session.user = username;
        return res.redirect('dashboard');
    } catch (error) {
        console.error(error.message);
        res.status(500).send("server error");
    }
});

router.get('/dashboard', async (req, res) => {
    try {
        if (req.session.user) {
            const users = await pool.query(`SELECT * FROM users WHERE user_name = '${req.session.user}'`);
            if (users.rows.length > 0) {
                const user = users.rows[0];
                res.render('dashboard', { user });
            }
        } else {
            throw new Error;
        }
    } catch (error) {
        res.status(401).send("unauthorized access");
    }
})

module.exports = router;