<html>
 <body>
<?php

if(!isset($_POST['feedback'])) { 
   die("Please fill in all forms.");
}

if(!$fh = fopen("feedback","a")) {
    print "Failed at opening file";
} else {
    fwrite($fh,"==================\n");
    foreach($_POST as $tmp => $value) {
        fwrite($fh,$tmp.":".$value."\n") || die("Error writing file");
    }
    print "Success\n";
}

?>

 </body>
</html>
