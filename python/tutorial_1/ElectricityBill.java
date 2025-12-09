/*
Electricity Bill Generate
    For first 100 units, Rs 1.5 per unit
    For second 100 units, Rs 2.5 per unit
    Beyond 200 units, each unit price is Rs 3.5

*/

import java.util.Scanner;

public class ElectricityBill {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int units = sc.nextInt();

        // if(units>200){
        //     System.out.println("Total Bill: "+(100*1.5 + 100*2.5 + (units-200)*3.5));
        // } else if(units<=200 && units > 100){
        //     System.out.println("Total Bill: "+(100*1.5 + (units-100)*2.5));
        // } else {
        //     System.out.println("Total Bill: "+(units*1.5));
        // }

        double totalBill = 0;
        if(units>200){
            totalBill = totalBill + (units-200)*3.5;
            units = 200;
        }
        if(units>100){
            totalBill = totalBill + (units-100)*2.5;
            units = 100;
        }
        if(units>0){
            totalBill = totalBill + (units)*1.5;
        }
        System.out.println("Total bill: "+totalBill);
    }    
}
