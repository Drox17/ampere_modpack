import java.util.jar.*;
public class Verificar {
 public static void main(String[] args) throws Exception {
  int count=0;
  try (var jar=new JarFile(args[0])) {
   var entries=jar.entries();
   while(entries.hasMoreElements()) {
    String n=entries.nextElement().getName();
    if(n.startsWith("link/infra/packwiz/installer/") && n.endsWith(".class") && !n.contains("/deps/")) {
     Class.forName(n.substring(0,n.length()-6).replace('/', '.'),false,Verificar.class.getClassLoader()).getDeclaredMethods();count++;
    }
   }
  }
  System.out.println("OK: "+count+" clases verificadas sin descargar ni actualizar el pack.");
 }
}
