window.onload()=function () {
    var templates=fetchTemplates();
    appendTemplates(templates);
}
var drawingBoard=document.getElementById("color_box")
function addToFavourite(){   
}
function saveColor() {
    
}

function localStorageSupport(){
    if(window.localStorage){
        return true
    }else{
        return false
    }
}
function saveValue(key,value){
    if(localStorageSupport()){
        try{
            localStorage.setItem(key,value);
        }catch(e){
            console.log("Error while saving value "+key)
        }
    }
}
function getValue(key) {
    if(localStorageSupport()){
        try{
            var item=localStorage.getItem(key)
            return item
        }catch(e){
            console.log("Error while fetching item "+key)
            return false
        }
    }    
}
/*
    templates schema
        {
            templates:[
                {"name":"template_name","colors":[{"value":"#aabbcc"},{"value":"#ff4321"}]}
            ]
        }
*/

function getTemplates(){
    if(localStorageSupport()){
        var x=JSON.parse(localStorage.getItem("templates"))
        return x["templates"]
    }return false
}

function newTemplate(template_name) {
    var templates=getTemplates()
    if(templates!=false){
        var new_templates=templates.push({"name":template_name,"colors":[]})
        saveValue("templates",new_templates)
    }
}
function addColorToTemplate(template_name,value){
    var templates=getTemplates()
    if(templates!=false){
        templates.forEach(element => {
            if(element.name==template_name){
               element.colors.push({"value":value})
            }
        });
    }
    return false
}
function deleteColor(template_name,value){
    var templates=getTemplates()
    if(templates!=false){
        templates.forEach(element => {
            if(element.name==template_name){
                element.colors.forEach(col=>{
                    if(col.value==value){
                        delete col.value
                        return true
                    }
                })
            }
        });
    }
    return false
}

function renderTemplate(templateName,colors){
    var temp_plate=document.getElementById("template_plate")
    var tmp=document.createElement("div")
    tmp.classList.append("class")
    colors.forEach(elm=>{
        var x=document.createElement("div")
        x.classList.add("class")
        x.style.background=elm+";";
        tmp.appendChild(x)
    });
    temp_plate.appendChild(tmp)
}