db = db.getSiblingDB("admin");

db.createUser({
  user: "anomalyze",
  pwd: "secretpassword",
  roles: [
    { role: "readWrite", db: "anomalyze" },
    { role: "dbAdmin", db: "anomalyze" }
  ]
});
