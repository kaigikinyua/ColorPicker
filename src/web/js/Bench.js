class Elements{
    element;
    constructor(element){this.element=element}
    changeBackground(newColor){
        if (newColor==undefined || newColor==null)return false
        this.element.background=newColor
        return true
    }
    changeTextColor(newColor){
        if (newColor==undefined || newColor==null)return false
        //check for text and change color
    }
}

