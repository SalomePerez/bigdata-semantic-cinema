import org.apache.jena.query.*;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.util.FileManager;

public class Main {
    
    public static void main(String[] args) {
        // Cargar el modelo RDF desde el archivo
        Model modelo = FileManager.get().loadModel("peliculas.rdf");
        
        System.out.println("=== BASE DE DATOS SEMÁNTICA - CINE COLOMBIA ===\n");
        
        // Consulta SPARQL: Obtener todas las películas con título y género
        String consulta = 
                "PREFIX cine: <http://www.cinecolombia.com/peliculas#> " +
                "SELECT ?titulo ?genero " +
                "WHERE { " +
                "  ?pelicula cine:titulo ?titulo ; " +
                "            cine:genero ?genero . " +
                "}";
        
        // Crear la consulta
        Query query = QueryFactory.create(consulta);
        
        // Ejecutar la consulta sobre el modelo
        QueryExecution qexec = QueryExecutionFactory.create(query, modelo);
        
        // Obtener resultados
        ResultSet resultados = qexec.execSelect();
        
        // Mostrar resultados formateados
        ResultSetFormatter.out(System.out, resultados, query);
        
        // Cerrar la ejecución
        qexec.close();
    }
}
