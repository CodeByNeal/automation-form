function sendEmailWithPDF(e) {
  try {
    Logger.log("Raw event values: " + JSON.stringify(e.values));

    var userName = e.values[1];      // Name
    var userEmail = e.values[2];     // Email

    var fileId = '1pEfY3kAQliGVlkfDM7UHbK49qW6AvhkT';
    var file = DriveApp.getFileById(fileId);
    var blob = file.getBlob().setName("Company_Overview.pdf");

    Logger.log("Sending to: " + userEmail);
    Logger.log("Blob size: " + blob.getBytes().length);

    GmailApp.sendEmail(userEmail, "✅Thank you for your submission!", 
      "Hi " + userName + ",\n\nThank you for filling out the form.\nPlease find your PDF attached.\n\nBest regards,\nNeha Kori",
      {
        attachments: [blob],
        name: "Rveiya Dynamics"
      });

    Logger.log("✅ Email sent successfully!");

  } catch (error) {
    Logger.log("❌ Error: " + error.toString());
  }
}
