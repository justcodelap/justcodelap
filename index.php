<?php 
    include_once'conn.php';
  $sqli = "SELECT film, date, time  FROM `sheesh` WHERE id > 0";
  $lol = mysqli_query($conn, $sqli);
  
?>

<!DOCTYPE html>
<html>
    <head lang="de">
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    </head>
    <body>   

        <?php while($row = $lol ->fetch_assoc()) { ?>
        <div class="filme">
        <p class='film'><?php echo $row["film"]; ?></p>
        <p class='time'><?php echo $row["time"]; ?></p>
        <p class='date'><?php echo $row["date"]; ?></p>      
        </div>
        <?php }; ?>

    </body>
</html>