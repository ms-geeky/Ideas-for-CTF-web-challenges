<!DOCTYPE html>
<html>
<body>

<?php

echo "<pre>You need a client cert with the organization \"BIT\" to access this site</pre>" ;
$ca_key = shell_exec('cat /etc/ssl/certs/ca 2>&1');
$ca_crt = shell_exec('cat /etc/ssl/certs/ca.crt 2>&1');
echo "<pre>$ca_key</pre>";
echo "<pre>$ca_crt</pre>";
?>

</body>
</html>