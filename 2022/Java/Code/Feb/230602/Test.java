 
public class Test {
    public static void main(String[] args){
        Father f = new Child();
        f.method();
    }
}


class Father{
    public void method(){
    System.out.println("Father.method()");
    }
}

class Child extends Father{
    public void method(){
        System.out.println("Child.method()");
    }
}
