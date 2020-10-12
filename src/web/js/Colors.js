window.onload=()=>{
    var red_slider=document.getElementById("red_slider")
    var green_slider=document.getElementById("green_slider")
    var blue_slider=document.getElementById("blue_slider")
    var alpha_slider=document.getElementById("alpha_slider")
    change_new_color(red_slider.value,green_slider.value,blue_slider.value,alpha_slider.value)
    loadFavColors()
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
    static convert_to_hex=function({red,blue,green}){
        
    }
    static convert_single_to_hex(value){
        var tens=Colors.rgb_to_hex(value[0])*15
        var ones=Colors.rgb_to_hex(value[1])
        return parseInt(tens)+parseInt(ones)
    }
    static rgb_to_hex(value){
        var cols={"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
        if(parseInt(value)==NaN){
            return cols[value.toLowerCase()]
        }else{
            return value
        }
    }
}

const red_slider=document.getElementById("red_slider")
const green_slider=document.getElementById("green_slider")
const blue_slider=document.getElementById("blue_slider")
const alpha_slider=document.getElementById("alpha_slider")
var dragged_color=""

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
    var create_color=document.getElementById("color_box")
    create_color.classList.toggle("bounce")
    setTimeout(()=>{create_color.classList.toggle("bounce")},1000)
}

function loadFavColors(){
    var fav_colors=document.getElementById("favourite_colors")
    for(var i=0;i<10;i++){
        var d=document.createElement("div")
        d.classList.add("colors")
        d.draggable=true
        d.ondragstart=drag_start
        var col=Colors.generate_color()
        d.dataset['color']=col
        d.style="background:rgba("+col[0]+","+col[1]+","+col[2]+");"
        fav_colors.appendChild(d)
    }
}
function droped_color(event){
    //console.log(event.dataTransfer.getData("text"))
    var col=event.dataTransfer.getData("text")
    //console.log(col)
    var colors=col.split(',')
    change_new_color(colors[0],colors[1],colors[2],100)
    red_slider.value=parseInt(colors[0])
    green_slider.value=parseInt(colors[1])
    blue_slider.value=parseInt(colors[2])
    var create_color=document.getElementById("color_box")
    create_color.classList.toggle("bounce")
    setTimeout(()=>{create_color.classList.toggle("bounce")},1000)
}
function allowDrop(event) {
    event.preventDefault()
}
function drag_start(event){
    //console.log(event.target.dataset["color"])
    event.dataTransfer.setData("text",event.target.dataset["color"])
    //event.target.style="opacity:0.9;"
}