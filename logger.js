const winston = require("winston");
require("winston-mongodb");

const logger = winston.createLogger({
  level: "info",
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(), //console Log
    new winston.transports.File({ filename: "logs/auth.log" }), //file Log
    new winston.transports.MongoDB({ //MongoDB Log 
      db: "mongodb://localhost:27017/auth_logs",
      options: { useUnifiedTopology: true },
      collection: "logs",
      level: "info",
    }),
  ],
});

module.exports = logger;
