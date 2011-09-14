<!DOCTYPE html
PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>

	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>MagicBullet Inventory Alpha</title>
	<script type="text/javascript" src="../_lib/jquery.js"></script>
	<script type="text/javascript" src="../_lib/jquery.cookie.js"></script>
	<script type="text/javascript" src="../_lib/jquery.hotkeys.js"></script>
	<script type="text/javascript" src="../jquery.jstree.js"></script>
	<link type="text/css" rel="stylesheet" href="syntax/!style.css"/>
	<link type="text/css" rel="stylesheet" href="!style.css"/>
	<script type="text/javascript" src="syntax/!script.js"></script>

	<style type="text/css">
	html, body { margin:0; padding:0; }
	body, td, th, pre, code, select, option, input, textarea { font-family:verdana,arial,sans-serif; font-size:10px; }
	.tree, .tree input, .jstree-dnd-helper, #vakata-contextmenu { font-size:10px; font-family:Verdana; }
	#container { width:780px; margin:10px auto; overflow:hidden; position:relative; }
	#tree { width:auto; height:400px; overflow:auto; border:1px solid gray; }

	#text { margin-top:1px; }

	#alog { font-size:9px !important; margin:5px; border:1px solid silver; }
	</style>
</head>
<body>
<div id="container" style="left:10px; top:10px; width:500px; border:1px solid silver; min-height:160px;">
<div id="mmenu" style="height:30px; overflow:auto;">
<input type="button" id="close_select" value="Close Selected Tree" style="display:block; float:right;" />
<!--<input type="button" id="clear_search" value="clear" style="display:block; float:right;"/>--!>
<input type="button" id="close_all" value="Close All" style="display:block; float:right;" />
<input type="submit" id="search" value="search" style="display:block; float:right;"/>
<input type="text" id="text" value="" style="display:block; float:right;" />
</div>

<h1>MagicBullet Tree</h1>
<li>Folders require loading time.</li> 
<li>Search must be clicked (enter button doesn't work yet).</li>
<li>Use your browser's search function after searching the tree for more refinement.</li>
<li>Date above drive indicates date of last update</li>
<h5></h5>



<?php include ('./XML_DATA/_include/include.php');?>

</div>


</body>
</html>