package BasesdeDatos;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Conexion {
    public static void main(String[] args){
        Connection conexion;
        Statement sentencia;
        String sql;
        String url = "jdbc:postgresql://10.0.8.159:5432/postgres";
        try{
            conexion = DriverManager.getConnection(url, "postgres", "postgres");
            System.out.println("conectado");
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}