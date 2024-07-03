import java.sql.*;



public class test {

    public static void main(String[] args) {
        System.err.println("kkk");

        try {
            Class.forName("org.postgresql.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }


        
    }
}