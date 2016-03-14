<?php
  // Vars
  define('COMMAND', '/home/pi/Documents/the_lodge/scripts/set_state.py');

  // Init
  ini_set('display_errors', 1);
  error_reporting(E_ALL);

  # Get POST data
  $input = file_get_contents('php://input');

  // Execute python script
  $output = array();
  exec('sudo python3 ' . COMMAND . ' ' . $input . ' 2>&1', $output);

  // Output result
  die($output[0]);
?>
