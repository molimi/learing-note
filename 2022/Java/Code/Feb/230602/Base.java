package com;

abstract class Base{
}

public class Derived extends Base{
    public static void main(String[] args){
        Base obj = new Derived();

        System.out.println(obj.getClass().getName());
        System.out.println(Base.class.getName());
    }
}