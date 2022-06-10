<?php
$string = 'sk_test_kk63qiifat8c8iurmnuge83uudcap_YoyeO1IAALEApUNn';
$sha256 = hash('sha256', $string, true);
$checksum64 = base64_encode($sha256);
echo $checksum64;
?>
