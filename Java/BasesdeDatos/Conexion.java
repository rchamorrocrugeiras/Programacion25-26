package BasesdeDatos;

import java.sql.*;

public class Conexion {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://10.0.8.170:5432/usuarios";
        try {
            Connection conexion =
                    DriverManager.getConnection(
                            url,
                            "postgres",
                            "vboxuser"
                    );
            System.out.println("Conectado");
            Statement sentencia = conexion.createStatement();
            String crearTablaSql =
                    "CREATE TABLE IF NOT EXISTS persoas(" +
                            "nome VARCHAR(50)," +
                            "dni VARCHAR(9)," +
                            "edade INTEGER)";
            sentencia.executeUpdate(crearTablaSql);

            String sql =
                    "INSERT INTO persoas(nome,dni,edade) VALUES (?,?,?)";

            PreparedStatement sentenciaP =
                    conexion.prepareStatement(sql);

            sentenciaP.setString(1, "Roque");
            sentenciaP.setString(2, "9876D");
            sentenciaP.setInt(3, 41);

            sentenciaP.executeUpdate();

            sql = "SELECT nome, dni, edade FROM persoas";

            sentenciaP = conexion.prepareStatement(sql);

            ResultSet resultados = sentenciaP.executeQuery();

            while (resultados.next()) {
                String n = resultados.getString("nome");
                String d = resultados.getString("dni");
                int e = resultados.getInt("edade");
                System.out.println(
                        "Nome: " + n + ", " + d + ", " + e
                );
            }
            conexion.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}