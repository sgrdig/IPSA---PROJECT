
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {


    public static void main(String[] args) {
        int port = 8085;
        try {
            ServerSocket sSocket = new ServerSocket(port);
            while (true) { 
                Socket s = sSocket.accept();
                BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream())) ; 

                PrintWriter out = new PrintWriter(s.getOutputStream());
                System.out.println(in.readLine());
                out.println("Oth encule");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}