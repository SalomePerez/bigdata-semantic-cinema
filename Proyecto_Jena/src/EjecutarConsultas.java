import org.apache.jena.query.*;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.util.FileManager;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;

/**
 * Programa para ejecutar todas las consultas SPARQL automáticamente
 * Lee los archivos .rq de la carpeta consultas/ y ejecuta cada uno
 */
public class EjecutarConsultas {
    
    public static void main(String[] args) {
        // Cargar el modelo RDF
        System.out.println("=".repeat(70));
        System.out.println("BASE DE DATOS SEMÁNTICA - CINE COLOMBIA");
        System.out.println("Apache Jena + RDF/XML + SPARQL");
        System.out.println("=".repeat(70));
        System.out.println();
        
        Model modelo = FileManager.get().loadModel("peliculas.rdf");
        System.out.println("✓ Modelo RDF cargado exitosamente");
        System.out.println("✓ Total de tripletas: " + modelo.size());
        System.out.println();
        
        // Ejecutar cada consulta
        for (int i = 1; i <= 10; i++) {
            ejecutarConsulta(modelo, i);
        }
        
        System.out.println("=".repeat(70));
        System.out.println("TODAS LAS CONSULTAS EJECUTADAS EXITOSAMENTE");
        System.out.println("=".repeat(70));
    }
    
    /**
     * Ejecuta una consulta SPARQL desde un archivo .rq
     */
    private static void ejecutarConsulta(Model modelo, int numeroConsulta) {
        String archivoConsulta = "consultas/consulta" + numeroConsulta + ".rq";
        
        try {
            // Leer el archivo de consulta
            String consultaTexto = new String(Files.readAllBytes(Paths.get(archivoConsulta)));
            
            // Mostrar encabezado
            System.out.println("=".repeat(70));
            System.out.println("CONSULTA " + numeroConsulta);
            System.out.println("Archivo: " + archivoConsulta);
            System.out.println("=".repeat(70));
            
            // Mostrar la consulta (sin comentarios)
            String[] lineas = consultaTexto.split("\n");
            System.out.println("Consulta SPARQL:");
            for (String linea : lineas) {
                if (!linea.trim().startsWith("#") && !linea.trim().isEmpty()) {
                    System.out.println("  " + linea);
                }
            }
            System.out.println();
            
            // Crear y ejecutar la consulta
            Query query = QueryFactory.create(consultaTexto);
            QueryExecution qexec = QueryExecutionFactory.create(query, modelo);
            
            // Obtener y mostrar resultados
            System.out.println("Resultados:");
            ResultSet resultados = qexec.execSelect();
            ResultSetFormatter.out(System.out, resultados, query);
            
            // Cerrar la ejecución
            qexec.close();
            
            System.out.println();
            
        } catch (IOException e) {
            System.err.println("Error al leer el archivo: " + archivoConsulta);
            System.err.println(e.getMessage());
        } catch (Exception e) {
            System.err.println("Error al ejecutar la consulta " + numeroConsulta);
            System.err.println(e.getMessage());
        }
    }
}
