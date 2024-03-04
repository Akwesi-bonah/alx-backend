import kue from 'kue';
queue = kue.createQueue();

const job = queue
  .create("push_notification_code", {
    phoneNumber: "1234567890",
    message: "This is a test message.",
  })
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on("complete", () => {
  console.log("Notification job completed");
});

job.on("failed", () => {
  console.log("Notification job failed");
});
