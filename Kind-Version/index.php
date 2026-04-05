<?php
require 'vendor/autoload.php'; // Assuming you use Composer for the MongoDB driver

try {
    // The hostname 'mongo-service' matches the Kubernetes Service name
    $client = new MongoDB\Client("mongodb://mongo-service:27017");
    $db = $client->testdb;
    
    echo "<h1>Success!</h1>";
    echo "<p>Connected to MongoDB successfully from the Apache Pod.</p>";
} catch (Exception $e) {
    echo "<h1>Connection Failed</h1>";
    echo $e->getMessage();
}
?>