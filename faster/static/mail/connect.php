<?php
$Username = $_POST['Username'];
$email = $_POST['email'];
$Password = $_POST['Password'];
$Repeat_Password = $_POST['Repeat Password'];


//Database connection
$conn = new mysqli('localhost','root', '', 'Bright-faster');
if($conn->connect_error){
    die(connection_aborted : '.$conn->connect_error')
}else{
    $stmt = $$conn->prepare("insert into sign up(Username, Email, Password, Repeat Password");
    $stmt->bind_param("ssii", $Username, $Email, $Password, $Repeat_Password);
    $stmt->execute();
    echo "Registration Successfully";
    $stmt->close();
    $conn->close();
}
?>