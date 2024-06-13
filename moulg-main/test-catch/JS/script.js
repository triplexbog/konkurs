function Validation(){
    
    try{
        num1 = parseInt(document.getElementById("num1").Value);
        console.log(num1);
        if(!isNaN(num1)){
            console.log('число');
            document.getElementById("number1").innerHTML = num1;
            
        }
        else{
            console.log('не число');
           throw new Error("Ошибка: введите пожалуйста в первое поле число")
        }
    }
    catch(ex){
        console.log('начало catch');
        document.getElementById("number1").innerHTML = ex.message;
        console.log("Завершил работу catch");

    }
    finally{
        console.log("Завершил работу");
    }


}