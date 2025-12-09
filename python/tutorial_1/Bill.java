import java.util.Scanner;

public class Bill {
    public static void main(String[] args) {

        int dosa_price = 60;
        int idli_price = 20;
        int cd_price = 50;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Sohan's Restaurant");
        System.out.println("******** Our menu ********");
        System.out.println("1. Dosa - Rs "+dosa_price);
        System.out.println("2. Idli - Rs "+idli_price);
        System.out.println("3. ColdDrink - Rs "+cd_price);
        System.out.println("Enter your choices: ");
        System.out.print("Dosa Quantity: ");
        int dosa_quantity = Integer.parseInt(scanner.nextLine());
        if(dosa_quantity<0){
            System.out.println("Invalid quantity. Try again");
            return;
        }
        System.out.print("Idli Quantity: ");
        int idli_quantity = Integer.parseInt(scanner.nextLine());
        System.out.print("ColdDrink Quantity: ");
        int cd_quantity = Integer.parseInt(scanner.nextLine());
        System.out.println("\n\n");
        System.out.println("===========Mohan's Bill=============");
        System.out.println("Dosa: "+dosa_quantity+"x Rs "+dosa_price+" = "+(dosa_quantity*dosa_price));
        System.out.println("Idli: "+idli_quantity+"x Rs "+idli_price+" = "+(idli_price*idli_quantity));
        System.out.println("ColdDrink: "+cd_quantity+"x Rs "+cd_price+" = "+(cd_price*cd_quantity));
        System.out.println("-------------------------------------");
        System.out.println("Total bill: Rs "+(dosa_quantity*dosa_price + idli_price*idli_quantity + cd_price*cd_quantity));
        // 5 * 50 + 25 * 2 + 3 * 30
        System.out.println("-------------------------------------");
        System.out.println("************* Thank you *************");
    }
}
