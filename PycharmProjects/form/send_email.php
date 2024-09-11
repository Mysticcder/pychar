<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Include PHPMailer library files
require 'vendor/autoload.php';

// Configuration for the receiving email address
$receiving_email_address = 'your_receiving_email@example.com';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize input
    $name = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $subject = filter_var($_POST['subject'], FILTER_SANITIZE_STRING);
    $message = filter_var($_POST['message'], FILTER_SANITIZE_STRING);

    // Check for empty fields
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        echo 'Please fill all the fields.';
        exit;
    }

    // Create an instance of PHPMailer
    $mail = new PHPMailer(true);

    try {
        // Server settings
        $mail->isSMTP();                                         // Set mailer to use SMTP
        $mail->Host = 'smtp.example.com';                        // Specify main and backup SMTP servers
        $mail->SMTPAuth = true;                                  // Enable SMTP authentication
        $mail->Username = 'your_smtp_username';                  // SMTP username
        $mail->Password = 'your_smtp_password';                  // SMTP password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;      // Enable TLS encryption, `PHPMailer::ENCRYPTION_SMTPS` also accepted
        $mail->Port = 587;                                       // TCP port to connect to

        // Recipients
        $mail->setFrom($email, $name);
        $mail->addAddress($receiving_email_address);             // Add a recipient

        // Content
        $mail->isHTML(true);                                     // Set email format to HTML
        $mail->Subject = $subject;
        $mail->Body    = nl2br($message);
        $mail->AltBody = $message; // Plain text for non-HTML mail clients

        // Send email
        $mail->send();
        echo 'Message has been sent';
    } catch (Exception $e) {
        echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
    }
} else {
    echo 'Invalid request method';
}
?>
