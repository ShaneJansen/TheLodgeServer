<?php
  // Vars
  define('COMMAND', '/home/pi/Documents/the_lodge/scripts/get_state.py');

  // Init
  ini_set('display_errors', 1);
  error_reporting(E_ALL);

  // Execute python script
  $output = array();
  exec('sudo python3 '. COMMAND .' 2>&1', $output);

  // Output result
  die($output[0]);
?>
