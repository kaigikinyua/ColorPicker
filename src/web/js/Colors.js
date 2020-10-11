window.onload=()=>{
    var red_slider=document.getElementById("red_slider")
    var green_slider=document.getElementById("green_slider")
    var blue_slider=document.getElementById("blue_slider")
    var alpha_slider=document.getElementById("alpha_slider")
    change_new_color(red_slider.value,green_slider.value,blue_slider.value,alpha_slider.value)
}
class Colors{
    constructor(){}
    static generate_color=function(){
        var r=Colors.gen_base_col()
        var g=Colors.gen_base_col()
        var b=Colors.gen_base_col()
        return [r,g,b]
    }
    static gen_base_col=function(){
        var x=Math.floor(Math.random()*255)
        while(x>256){
            x=Math.floor(Math.random()*255)
        }
        return x;
    }
}

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
    create_color.style="background:rgba("+r+","+g+","+b+","+parseInt(a)/100+");"
}

function randomize(){
    var colors=Colors.generate_color()
    change_new_color(colors[0],colors[1],colors[2],100)
    red_slider.value=colors[0]
    green_slider.value=colors[1]
    blue_slider.value=colors[2]
}