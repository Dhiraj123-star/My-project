//this keyword 
class Mobile{ 
  //late used for late initialisation of the class attributes 
  late String model_name;
  late int man_year;

  //creating constructor
  Mobile(String model_name, int man_year){
    this.model_name=model_name;
    this.man_year=man_year;

    print("Model name is: $model_name");
    print("Manufacturing year: $man_year");
  }
}
main(List<String> args) {
  
  //creating object

  Mobile myobj=new Mobile("Tecno",2021);

}