import express from "express";
import kue from "kue";
import redis from "redis";
import { promisify } from "util";

// Create an Express application
const app = express();
const port = 1245;

// Create a Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// Key for storing the number of available seats in Redis
const seatsKey = "available_seats";

// Function to reserve a seat
function reserveSeat(number) {
  client.set(seatsKey, number);
}

// Function to get the current number of available seats
async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync(seatsKey);
  return availableSeats;
}

// Event handler for Redis client errors
client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

// Event handler for successful connection to Redis server
client.on("connect", () => {
  console.log("Redis client connected to the server");

  // Reserve 50 seats initially
  reserveSeat(50);

  // Enable seat reservation
  reservationEnabled = true;
});

// Create a Kue queue
const queue = kue.createQueue();
const queueName = "reserve_seat";

// Start the Express server
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});

// Route to get the number of available seats
app.get("/available_seats", async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get("/reserve_seat", (req, res) => {
  if (reservationEnabled === false) {
    res.json({ status: "Reservation are blocked" });
    return;
  }

  const jobFormat = {};

  const job = queue.create(queueName, jobFormat).save((err) => {
    if (err) {
      res.json({ status: "Reservation failed" });
    } else {
      res.json({ status: "Reservation in process" });
    }
  });

  job.on("complete", () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on("failed", (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the queue
app.get("/process", async (req, res) => {
  queue.process(queueName, async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();

    if (availableSeats <= 0) {
      done(Error("Not enough seats available"));
    }

    availableSeats = Number(availableSeats) - 1;

    reserveSeat(availableSeats);

    if (availableSeats <= 0) {
      reservationEnabled = false;
    }

    done();
  });

  res.json({ status: "Queue processing" });
});
