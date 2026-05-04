<?php
$mysqli = new mysqli("db", "appuser", "apppass", "myapp");

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

if (isset($_POST['add'])) {
    $name = $_POST['name'];
    $mysqli->query("INSERT INTO people (name) VALUES ('$name')");
}

if (isset($_POST['delete'])) {
    $id = $_POST['id'];
    $mysqli->query("DELETE FROM people WHERE id = $id");
}

$result = $mysqli->query("SELECT * FROM people");
?>

<h2>Add Person</h2>
<form method="POST">
    <input name="name" placeholder="Name">
    <button name="add">Add</button>
</form>

<h2>People</h2>
<ul>
<?php while ($row = $result->fetch_assoc()): ?>
    <li>
        <?= $row['id'] ?> - <?= $row['name'] ?>
        <form method="POST" style="display:inline">
            <input type="hidden" name="id" value="<?= $row['id'] ?>">
            <button name="delete">Delete</button>
        </form>
    </li>
<?php endwhile; ?>
</ul>

