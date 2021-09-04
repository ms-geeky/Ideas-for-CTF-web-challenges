<!DOCTYPE html>
<html>
<body>

<?php
// Get client certificate data
$client_verify = $_SERVER['SSL_CLIENT_VERIFY'];
$client_subject_dn = $_SERVER['SSL_CLIENT_S_DN'];
$client_issuer_dn = $_SERVER['SSL_CLIENT_I_DN'];


$client_certificate_data = [
    'client_verify' => $client_verify,
    'client_subject_dn' => $client_subject_dn,
    'client_issuer_dn' => $client_issuer_dn    
    
];

echo json_encode(
    $client_certificate_data
    
);
?>

</body>
</html>