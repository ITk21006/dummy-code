const logger = require("../logger"); //import logger

async function loginUser(req, res) {
  const { email, password } = req.body;
  const user = await User.findOne({ email });   //simulated user lookup
  
  if (!user) {
    logger.warn(`Failed login attempt: ${email}`);
    return res.status(401).json({ error: "Invalid credentials" });
  }

  //password check
  const isMatch = await bcrypt.compare(password, user.password);
  
  if (!isMatch) {
    logger.warn(`Failed login attempt (wrong password): ${email}`);
    return res.status(401).json({ error: "Invalid credentials" });
  }

  logger.info(`User logged in: ${email}`);
  res.json({ message: "Login successful" });
}

//error logging
function errorHandler(err, req, res, next) {
  logger.error(err.message);
  res.status(500).json({ error: "Internal Server Error" });
}

module.exports = { loginUser, errorHandler };
