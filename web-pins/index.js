			function controlCall(mode){
				console.log(mode);
																	//meta search start
				var control=new XMLHttpRequest();
				control.onreadystatechange = function(){
					if(this.readyState==4&&this.status==200){
						document.getElementById("lightStatus").innerHTML=this.responseText;
					}
				}
				control.open("GET","pi-write.php?mode="+mode+"&pin=17",true);
				control.send(); 
			}

