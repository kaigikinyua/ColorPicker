const red_slider=document.getElementById("red_slider")
const green_slider=document.getElementById("green_slider")
const blue_slider=document.getElementById("blue_slider")
const alpha_slider=document.getElementById("alpha_slider")



red_slider.oninput=()=>{
    change_new_color(red_slider.value,green_slider.value,blue_slider.value,alpha_slider.value)
}
green_slider.oninput=()=>{  
    change_new_color(red_slider.value,green_slider.value,blue_slider.value,alpha_slider.value)
}
blue_slider.oninput=()=>{
    change_new_color(red_slider.value,green_slider.value,blue_slider.value,alpha_slider.value)
}
alpha_slider.oninput=()=>{
    change_new_color(red_slider.value,green_slider.value,blue_slider.value,alpha_slider.value)
}


function change_new_color(r,g,b,a){
    var create_color=document.getElementById("color_box")
    //console.log(create_color)
    //console.log(r+":"+g+":"+b+":"+a)
    create_color.style="background:rgba("+r+","+g+","+b+","+parseInt(a)/100+");"
}

class Colors{}