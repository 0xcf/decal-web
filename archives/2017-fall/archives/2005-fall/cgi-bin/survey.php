<html>
 <body>
<?php

if(!isset($_POST['name']) ||
   !isset($_POST['email']) ||
   !isset($_POST['linux']) ||
   !isset($_POST['program']) ||
   !isset($_POST['html'])) {
   die("Please fill in all forms.");
}

if(!$fh = fopen("survey_results","a")) {
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
