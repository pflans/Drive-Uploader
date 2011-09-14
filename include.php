<?php
foreach (glob("./XML_DATA/*.xml") as $filename)
{
echo date ("m/d/y", filemtime($filename));
$x++;
?>
<div id="<?php echo $x; ?>"> 
<script type="text/javascript">
$(function () {  
	var name = "<?php echo $x; ?>";
    var url =  "<?php echo $filename; ?>";
	
	$("#search").click(function () {
        $("#"+name).jstree("search",document.getElementById("text").value);
    });
    $('#close_all').click(function () {
        $("#"+name).jstree("close_all");
 	});
       
    
    
    $("#"+name)
	.jstree({ 
		"plugins" : [ "themes", "xml_data", "ui", "search", "types" ],

		"xml_data" : {"ajax" : {"url" : url},"xsl" : "nest"},
		  "search" : {"case_insensitive" : true,},
		   "types" : {"max_depth" : -2,"max_children" : -2,
		   	   "types" : {"default" : {"valid_children" : "none",
		    	"icon" : {"image" : "./file.png"}},
	 		  "folder" : {"icon" : {"image" : "./folder.png"}},
			   "drive" : {"icon" : {"image" : "./root.png"}},},},
		}); });	
</script>
</div>
<?php
}
?>

<script type="text/javascript">
  $('#close_select').click(function () {
       $.jstree._focused().close_all();
  });
</script>

