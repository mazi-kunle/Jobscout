<?php
	session_start();

	if (isset($_SESSION['emailaddress'])) {
		header('Location: home.php');
		exit();
	}

	if (isset($_POST['emailaddress']) && isset($_POST['password'])) {
		$emailaddress = $_POST['emailaddress'];
		$password = $_POST['password'];

		if ($emailaddress === 'example' && $password === 'password') {
		
			$_SESSION['emailaddress'] = $emailaddress;

			header('Location: home.php');
			exit();
		} else {
			$error = 'Invalid emailaddress or password';
		}
	}
?>

<!DOCTYPE html>
<html>
<head>
	<title>Auction System Login Page</title>
	<link rel="stylesheet" type="text/css" href="scout.css">
</head>
<body>
	<div class="container">
		<h1>Auction System Login Page</h1>
		<?php if (isset($error)): ?>
			<p class="error"><?php echo $error; ?></p>
		<?php endif; ?>
		<form action="login.php" method="post">
			<label for="emailaddress">Email Address:</label>
			<input type="text" id="emailaddress" name="emailaddress" required>

			<label for="password">Password:</label>
			<input type="password" id="password" name="password" required>

			<input type="submit" value="Login">
		</form>
	</div>
</body>
</html>

