function ohayou() {
    alert("Hello!");

  }

function toggle(){
    flag1 = !flag1;
    document.getElementById("switch").value = flag1;
    if(flag1 == true){location.href='drone.html?1'};
    if(flag1 == false){location.href='drone.html?2'};
} 